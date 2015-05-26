#!/usr/bin/env python

# /_config/section/key

import requests, json
from requests.auth import HTTPBasicAuth

headers = {
	"Content-Type": "application/json"
}

def set_oauth_audience(hostUrl, audience, username, password):

	res = requests.put("{0}/_config/browserid/audience".format(hostUrl), 
		data='"{0}"'.format(audience), auth=HTTPBasicAuth(username, password),
		headers=headers)

	return res.status_code == requests.codes.ok



if "__main__" == __name__:

	import argparse

	ap = argparse.ArgumentParser()
	ap.add_argument("-audience", help="OAuth Audience")
	ap.add_argument("--couchUrl", help="URL of CouchDB", default="http://localhost:5984")
	ap.add_argument("--admin", help="CouchdDB admin", default="admin")
	ap.add_argument("--password", help="CouchdDB admin password", default="password")
	args = ap.parse_args()


	print json.dumps(set_oauth_audience(args.couchUrl, args.audience, args.admin, args.password))