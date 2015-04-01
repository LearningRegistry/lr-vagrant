#!/bin/bash

sudo rm -rf /etc/udev/rules.d/70-persistent-net.rules
sudo mkdir /etc/udev/rules.d/70-persistent-net.rules
sudo rm -rf /dev/.udev/
sudo rm -rf /lib/udev/rules.d/75-persistent-net-generator.rules

cd ~
rm -rf .ssh
mkdir .ssh
wget --no-check-certificate https://raw.githubusercontent.com/mitchellh/vagrant/master/keys/vagrant.pub -O .ssh/authorized_keys
chmod 700 .ssh
chmod 600 .ssh/authorized_keys
chown -R vagrant:vagrant .ssh
