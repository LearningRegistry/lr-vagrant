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

set -v

pushd /home/learnreg/LearningRegistry

lr_pid=$(cat /var/run/learningregistry/uwsgi.pid)
sudo service learningregistry stop

sudo killall -9 uwsgi

sudo sh -c 'cat /dev/null > /var/log/learningregistry/uwsgi.log'

echo 'Updating '

pushd ./config

echo 'Waiting 30 seconds to give couch a chance to start before running LR setup'
sleep 30

sudo -u learnreg bash -c 'source /home/learnreg/env/bin/activate; python ./service_util.py < /vagrant/bin/typescript_service_util.txt ; deactivate'

sudo cp -f ./learningregistry.sh /etc/init.d/learningregistry

popd

sudo chmod +x /etc/init.d/learningregistry

echo 'Waiting 60 seconds for ports to clear.'

sleep 60

echo 'Setting Learning Registry boot order'

sudo update-rc.d  -f learningregistry remove

sudo update-rc.d learningregistry defaults 99

sudo service learningregistry start

echo 'Waiting 10 seconds for log to generate.'

sleep 10

sudo cat /var/log/learningregistry/uwsgi.log