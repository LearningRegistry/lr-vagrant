#!/usr/bin/env python

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

headers = {
	"Content-Type": "application/json"
}

def add_distribution(nodeUrl, contact, destUrl, username, password):
	data = {
		"contact": contact,
		"destUrl": destUrl,
		"username": username,
		"password": password
	}

	r = requests.post("{0}/register/create".format(nodeUrl), data=data)
	response = json.loads(r.text)
	return "okay" == response["status"]


if __name__ == "__main__":

	import argparse

	ap = argparse.ArgumentParser()
	ap.add_argument("-node", help="Source node URL", required=True)
	ap.add_argument("-contact", help="Target node contact email", required=True, default="jim.klo@learningregistry.org")
	ap.add_argument("-target", help="Target node URL", required=True)
	ap.add_argument("--username", help="Target node username", default="")
	ap.add_argument("--password", help="Target node password", default="")
	args = ap.parse_args()


	print add_distribution(args.node, args.contact, args.target, args.username, args.password)

