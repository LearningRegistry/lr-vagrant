#!/bin/bash

KEYID=$1
HOST=$2

/vagrant/bin/provision-lr-branch.sh jimklo https://github.com/jimklo/LearningRegistry.git lr49_vagrant
sudo -u learnreg -i /vagrant/bin/install_signing_key.py -keyid $KEYID -hostname $HOST
/vagrant/bin/provision-fix-start-script.sh