#!/bin/bash

origin=$1
url=$2
tag=$3

pushd /home/learnreg/LearningRegistry
sudo -u learnreg git checkout master
sudo -u learnreg git branch -D ${origin}/${tag}
sudo -u learnreg git remote add ${origin} ${url}
sudo -u learnreg git fetch --all
sudo -u learnreg git fetch --tags
sudo -u learnreg git checkout tags/${tag} -b ${origin}/${tag}

popd

