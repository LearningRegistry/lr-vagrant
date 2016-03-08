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


# setup a sym link to /lr_src (configured lr.vm.synced_folder in Vagrantfile)
sudo -H -u learnreg bash -c 'ln -s /lr_src /home/learnreg/lr_src'

# copy the development.ini from the old LR_HOME to your new LR_HOME (since it has the proper gpg keys and such)
echo 'copying development.ini from old LR_HOME to /lr_src'
sudo cp /home/learnreg/LearningRegistry/LR/development.ini /home/learnreg/lr_src/LR/development.ini

# change the LR_HOME parameter on the init script
echo 'Setting LR_HOME to /lr_src in init script'
sudo sed -i s:home/learnreg/LearningRegistry:home/learnreg/lr_src:g /etc/init.d/learningregistry

echo 'Restarting LR service'
sudo service learningregistry stop
sleep 10
sudo service learningregistry start
