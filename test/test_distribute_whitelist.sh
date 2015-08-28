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

vagrant ssh lr51a -c "/home/learnreg/env/bin/python /vagrant/bin/distribute.py -node http://lr51a.local -target http://lr51b.local -contact jim.klo@learningregistry.org"
vagrant ssh lr51a -c "/home/learnreg/env/bin/python /vagrant/bin/distribute.py -node http://lr51a.local -target http://lr51c.local -contact jim.klo@learningregistry.org"
vagrant ssh lr51a -c "sudo service learningregistry stop; sleep 60; sudo service learningregistry start"
vagrant ssh lr51a -c "curl -X POST http://lr51a.local/distribute"