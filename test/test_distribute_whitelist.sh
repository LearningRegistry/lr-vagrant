#!/bin/bash

vagrant ssh lr51a -c "/home/learnreg/env/bin/python /vagrant/bin/distribute.py -node http://lr51a.local -target http://lr51b.local -contact jim.klo@learningregistry.org"
vagrant ssh lr51a -c "/home/learnreg/env/bin/python /vagrant/bin/distribute.py -node http://lr51a.local -target http://lr51c.local -contact jim.klo@learningregistry.org"
vagrant ssh lr51a -c "sudo service learningregistry stop; sleep 60; sudo service learningregistry start"
vagrant ssh lr51a -c "curl -X POST http://lr51a.local/distribute"