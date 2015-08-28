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