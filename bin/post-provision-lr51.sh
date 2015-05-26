#!/bin/bash

KEYID=$1
HOST=$2

/vagrant/bin/provision-lr-branch.sh jimklo https://github.com/jimklo/LearningRegistry.git lr51_vagrant
sudo -u learnreg -i /vagrant/bin/install_signing_key.py -keyid $KEYID -hostname $HOST
sudo -u learnreg -i /vagrant/bin/set_loglevel.py -level INFO
/vagrant/bin/provision-fix-start-script.sh