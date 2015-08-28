#!/bin/bash

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

echoerr() { cat <<< "$@" 1>&2; }

if [ "$1" == "lr49" ]; then
	SRC_NODE=lr49
	TGT_NODE=lr51
elif [ "$1" == "lr51" ]; then
	SRC_NODE=lr51
	TGT_NODE=lr49
else
	echoerr "USAGE: $0 [ lr49 | lr51 ]"
	exit 1
fi

PUBLISH_BIN=./bin/publish.py
NUM_ENV=1

vagrant ssh ${SRC_NODE} -c "/home/learnreg/env/bin/python /vagrant/bin/distribute.py -node http://${SRC_NODE}.local -target http://${TGT_NODE}.local -contact jim.klo@learningregistry.org"
vagrant ssh ${SRC_NODE} -c "sudo service learningregistry stop; sleep 60; sudo service learningregistry start"
vagrant ssh ${SRC_NODE} -c "curl -X POST http://${SRC_NODE}.local/distribute"

mkdir tmp
rm -f tmp/*

# publish documents on lr49.local (publish script changed)
${PUBLISH_BIN} --mode publish \
   --node ${SRC_NODE} --sign local --num ${NUM_ENV} \
   --outidfile "tmp/0_fournine.json" \
   --msg "This is a .49 resource." \
   --doc_version "0.49.0"

${PUBLISH_BIN} --mode publish \
   --node ${SRC_NODE} --sign local --num ${NUM_ENV} \
   --outidfile "tmp/0_fournine.json" \
   --msg "This is a .51 resource." \
   --doc_version "0.51.0"

vagrant ssh ${SRC_NODE} -c "curl -X POST http://${SRC_NODE}.local/distribute"


# verify documents on lr51.local (check in browser)
