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

import subprocess, argparse, os, re

if __name__ == "__main__":

	ap = argparse.ArgumentParser(description="Installs GPG signing keys")
	ap.add_argument("-keyid", help="gpg key id to install", type=str)
	ap.add_argument("-hostname", help="hostname of the server", type=str)
	ap.add_argument("--passphrase", help="gpg passphrase", default="vagrant")
	ap.add_argument("--keypath", help="dir where to look for keys", default="/vagrant/signing_keys")
	ap.add_argument("--response", help="node setup response file template", default="/vagrant/node_response_file.txt")
	ap.add_argument("--python", help="path to python", default="/home/learnreg/env/bin/python")
	args = ap.parse_args()

	for dirpath, dirnames, filenames in os.walk(args.keypath):
		for f in filenames:
			if re.search("{0}.*\.asc$".format(args.keyid[-8:]), f):
				path = os.path.join(dirpath, f)
				# $(gpg --textmode --with-fingerprint /tmp/lr49.asc | grep 'Key fingerprint =' | sed 's/^[^=]*=//g' | sed 's/ //g')
				fingerprint = subprocess.check_output("gpg --textmode --with-fingerprint {0} | grep 'Key fingerprint =' | sed 's/^[^=]*=//g' | sed 's/ //g'".format(path), shell=True).strip()
				signer = subprocess.check_output("""gpg --textmode --with-fingerprint {0} | grep -e "^sec" | sed 's/\s\+/ /g' | cut -d ' ' -f 4-""".format(path), shell=True).strip()

				proc = subprocess.Popen(["gpg", "--import", path],
					stdin=subprocess.PIPE, stdout=subprocess.PIPE, stderr=subprocess.PIPE)
				out = proc.communicate()
				print out

				with open(args.response, "rU") as rf:
					template = rf.read()

				response_text = template.format(hostname=args.hostname, privatekey=fingerprint[-16:], signer=signer, passphrase=args.passphrase)

				print response_text
				with open("/tmp/response", "w") as rf:
					rf.write(response_text)

				proc = subprocess.Popen([args.python, "/home/learnreg/LearningRegistry/config/setup_node.py"], 
					cwd="/home/learnreg/LearningRegistry/config",
					stdin=subprocess.PIPE, stdout=subprocess.PIPE, stderr=subprocess.PIPE)

				out = proc.communicate(response_text)
				print out






