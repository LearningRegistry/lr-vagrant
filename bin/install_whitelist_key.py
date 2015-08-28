#!/usr/bin/env python

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

import ConfigParser, shutil, time, argparse

if __name__ == "__main__":

    ap = argparse.ArgumentParser()
    ap.add_argument("-keydir", type=str, default="/vagrant/signing_keys/pub_keys_a/")
    args = ap.parse_args()

    lr_config_file = "/home/learnreg/LearningRegistry/LR/development.ini"
    ini_key = ("app:main", "lr.tombstone.admin_signed.key_directory")
    ini_value = args.keydir

    shutil.copyfile(lr_config_file, "{0}.bak_{1}".format(lr_config_file, int(time.time())))

    cp = ConfigParser.ConfigParser()
    cp.read(lr_config_file)

    exist = cp.get(*ini_key)
    print exist

    cp.set(*ini_key, value=ini_value)

    with open(lr_config_file, 'wb') as configfile:
        cp.write(configfile)
