#!/bin/bash

set -v

pushd /home/learnreg/LearningRegistry

lr_pid=$(cat /var/run/learningregistry/uwsgi.pid)
sudo service learningregistry stop

sudo killall -9 uwsgi

sudo sh -c 'cat /dev/null > /var/log/learningregistry/uwsgi.log'

echo 'Updating '

pushd ./config

sudo -u learnreg bash -c 'source /home/learnreg/env/bin/activate; python ./service_util.py < /vagrant/bin/typescript_service_util.txt ; deactivate'

sudo cp -f ./learningregistry.sh /etc/init.d/learningregistry

popd

sudo chmod +x /etc/init.d/learningregistry

echo 'Waiting 60 seconds for ports to clear.'

sleep 60

sudo service learningregistry start

echo 'Waiting 10 seconds for log to generate.'

sleep 10

sudo cat /var/log/learningregistry/uwsgi.log