#!/bin/bash

$(/vagrant/bin/provision-lr-branch.sh jimklo https://github.com/jimklo/LearningRegistry.git 0.49.0_jimklo)
$(/vagrant/bin/provision-fix-start-script.sh)