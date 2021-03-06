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

origin=$1
url=$2
tag=$3

pushd /home/learnreg/LearningRegistry
#sudo -u learnreg git checkout master
#sudo -u learnreg git branch -D ${origin}/${tag}
#sudo -u learnreg git remote add ${origin} ${url}
sudo -u learnreg git fetch --all
#sudo -u learnreg git fetch --tags
#sudo -u learnreg git checkout tags/${tag} -b ${origin}/${tag}
sudo -u learnreg git pull

popd
