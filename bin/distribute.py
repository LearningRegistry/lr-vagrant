#!/usr/bin/env python

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

