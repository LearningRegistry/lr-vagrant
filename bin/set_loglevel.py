#!/usr/bin/env python
import ConfigParser, shutil, time, argparse, re

if __name__ == "__main__":

    ap = argparse.ArgumentParser()
    ap.add_argument("-level", type=str, choices=["CRITICAL", "ERROR", "WARNING", "INFO", "DEBUG", "NOTSET"], default="ERROR")
    args = ap.parse_args()

    lr_config_file = "/home/learnreg/LearningRegistry/LR/development.ini"


    shutil.copyfile(lr_config_file, "{0}.bak_{1}".format(lr_config_file, int(time.time())))

    cp = ConfigParser.ConfigParser()
    cp.read(lr_config_file)

    for section in cp.sections():
        if re.match("^logger_", section) and cp.has_option(section, "level"):
            cp.set(section, "level", value=args.level)


    with open(lr_config_file, 'wb') as configfile:
        cp.write(configfile)
