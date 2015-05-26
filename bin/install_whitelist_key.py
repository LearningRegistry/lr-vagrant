#!/usr/bin/env python
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
