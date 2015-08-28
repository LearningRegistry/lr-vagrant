#! /usr/bin/env python

#
#   Copyright 2015 Jim Klo <jim@arkitec.com>
#
#   Licensed under the Apache License, Version 2.0 (the "License");
#   you may not use this file except in compliance with the License.
#   You may obtain a copy of the License at
#
#       http://www.apache.org/licenses/LICENSE-2.0
#
#   Unless required by applicable law or agreed to in writing, software
#   distributed under the License is distributed on an "AS IS" BASIS,
#   WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
#   See the License for the specific language governing permissions and
#   limitations under the License.
#

import requests, uuid, json, os
from datetime import datetime
from requests_oauthlib import OAuth1
from LRSignature.sign.Sign import Sign_0_51

credentials = {
	"client_key": "jim.klo@learningregistry.org",
	"client_secret": "szJG02nx8PAbAUAEmXJ5k6T1aktNd4lf",
	"resource_owner_key": "node_sign_token",
	"resource_owner_secret": "3p3qEkcNwdATFf9d5p8oXbpbzcl72Qxd"
}

# lr51
lr51 = {
   "consumer_keys": {
       "jim.klo@learningregistry.org": "dc0pQG9shUbaFIqrLwvuDyIY6SNA0aXN"
   },
   "tokens": {
       "node_sign_token": "BIPBFfAXUv+u5z81M+q/lhfkIhJYk7eh"
   }
}

credentials.update({
	"client_secret": lr51["consumer_keys"]["jim.klo@learningregistry.org"],
	"resource_owner_secret": lr51["tokens"]["node_sign_token"]
	})

def make_test_envelope(version=1, mode="publish", msg="This is a Test", doc_version="0.51.0"):
	doc_id = uuid.uuid1()
	ts = datetime.utcnow()
	template = {
		"doc_type": "resource_data",
		"doc_version": "0.51.0",
		"doc_ID": doc_id.urn,
		"resource_data_type": "paradata",
		"active": True,
		"identity": {
		    "submitter_type": "agent",
		    "submitter": "jim.klo@learningregistry.org"
		},
		"create_timestamp": "{0}Z".format(ts.isoformat("T")),
		"TOS": {
		    "submission_TOS": "http://creativecommons.org/publicdomain/zero/1.0/legalcode"
		},
		"payload_schema": ["test-data"],
		"resource_locator": "http://arkitec.com/learningregistry/test-data/{0}/{1}".format(doc_id.hex, version),
		"payload_placement": "inline",
		"resource_data": msg
	}

	if "replace" == mode and len(last_doc_id_list) > 0:
		template.update({
			"replaces": [last_doc_id_list.pop()]
		})


	return template

def publish_envelope(node, envelope=None, envelope_list=[]):
	oauth = OAuth1(**credentials)
	docs = []
	if envelope is not None:
		docs.append(envelope)

	docs += envelope_list
	r = requests.post("{0}/publish".format(node), json={ "documents":docs}, auth=oauth)
	print r.content


def sign_envelope(envelope, key_id, passphrase, key_url):
    # def __init__(self, privateKeyID=None, passphrase=None, gnupgHome=os.path.expanduser(os.path.join("~", ".gnupg")), gpgbin="/usr/local/bin/gpg", publicKeyLocations=[], sign_everything=True):
	opts = {
		"privateKeyID": key_id, 
		"passphrase": passphrase, 
		"gnupgHome": os.path.expanduser(os.path.join("~", ".gnupg")), 
		"gpgbin":"gpg", 
		"publicKeyLocations":[key_url], 
		"sign_everything": True
	}

	signer = Sign_0_51(**opts)
	return signer.sign(envelope)


if __name__ == "__main__":

	import argparse

	ap = argparse.ArgumentParser(description="Publish test data to node.")
	ap.add_argument('--mode', choices=["publish", "replace"], default="publish")
	ap.add_argument('--node', choices=["lr51", "lr51a", "lr51b", "lr51c"], default="lr51")
	ap.add_argument('--sign', choices=["proxy", "local", "whitelist", "rogue"], default="local")
	ap.add_argument('--idfile', default="idfile.json")
	ap.add_argument('--outidfile', default="idfile.json")
	ap.add_argument('--num', type=int, default=10)
	ap.add_argument('--msg', type=str, default="This is a test")
	ap.add_argument('--doc_version', type=str, default="0.51.0")




	args = ap.parse_args()

	host = "{0}.local".format(args.node)

	


	if "whitelist" == args.sign:
		opts = {
			"key_id": "B7B49BA3A7409F8A",
			"passphrase": "whitelist",
			"key_url": "http://hkps.pool.sks-keyservers.net/pks/lookup?op=get&search=0xB7B49BA3A7409F8A"
		}
	elif "local" == args.sign:
		opts = {
			"key_id": "05510FF20CC118C7",
			"passphrase": "vagrant",
			"key_url": "http://hkps.pool.sks-keyservers.net/pks/lookup?op=get&search=0x05510FF20CC118C7"
		}
	elif "rogue" == args.sign:
		opts = {
			"key_id": "4212BA1AAF82338A",
			"passphrase": "vagrant",
			"key_url": "http://hkps.pool.sks-keyservers.net/pks/lookup?op=get&search=0x4212BA1AAF82338A"
		}

	last_doc_id_list = []
	try:
		with open(args.idfile, "rb") as last:
			last_doc_id_list += json.load(last)
	except IOError as e:
		if e.errno == 2:
			print "Input file {0} doesn't exist".format(args.idfile)
		else:
			raise e;

	doc_id_list = []

	def sign_and_drive(envelope_list):
		if "proxy" != args.sign and len(envelope_list) > 0:
			def sign_it(envelope):
				doc_id_list.append(envelope["doc_ID"])
				return sign_envelope(envelope, **opts)

			envelope_list = map(sign_it, envelope_list)
		else:
			map(lambda e: doc_id_list.append(e["doc_ID"]), envelope_list)

		print json.dumps(envelope_list, indent=4)

		publish_envelope("http://{0}".format(host), None, envelope_list)
		print "Published Envelope Set #{0} to {1}".format(i, host)


	envelope_list = []
	for i in range(0, args.num):
		
		env = make_test_envelope(mode=args.mode, msg=args.msg, doc_version=args.doc_version)
		envelope_list.append(env)
		# print json.dumps(env, indent=4)

		if len(envelope_list) % 10 == 10:
			sign_and_drive(envelope_list)
			envelope_list = []

	sign_and_drive(envelope_list)
	

	with open(args.outidfile, "wb") as out:
		json.dump(doc_id_list, out)



