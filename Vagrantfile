# -*- mode: ruby -*-
# vi: set ft=ruby :

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

# All Vagrant configuration is done below. The "2" in Vagrant.configure
# configures the configuration version (we support older styles for
# backwards compatibility). Please don't change it unless you know what
# you're doing.
Vagrant.configure(2) do |config|

  config.hostmanager.enabled = true
  config.hostmanager.manage_host = true
  config.hostmanager.include_offline = true

  config.vm.define "lr51", primary: true  do |lr51|
    lr51.vm.box = "learningregistry/lr-ubuntu-51"
    lr51.vm.host_name = "lr51.local"

    lr51.vm.network "private_network", ip: "10.0.1.51"
    lr51.vm.network "forwarded_port", guest: 80, host: 8080, auto_correct: true
    # lr51.vm.network "forwarded_port", guest: 5984, guest_ip: "127.0.0.1", host: 5984, auto_correct: true
    lr51.ssh.insert_key = false
    lr51.vm.provider "virtualbox" do |vb|
      # Display the VirtualBox GUI when booting the machine
      vb.gui = false

      # Customize the amount of memory on the VM:
      vb.memory = "1024"

      vb.name = "LR Node v.51"
    end

    lr51.vm.provision "shell", path: "bin/post-provision-lr51.sh",
      args: ["5AC53DD3", "lr51.local"]

  end

  config.vm.define "lr49", primary: false  do |lr49|
    # lr49.vm.box = "lr-49b"
    lr49.vm.box = "learningregistry/lr-ubuntu-49"
    lr49.vm.host_name = "lr49.local"

    lr49.vm.network "private_network", ip: "10.0.1.49"
    lr49.vm.network "forwarded_port", guest: 80, host: 8080, auto_correct: true
    # lr49.vm.network "forwarded_port", guest: 5984, guest_ip: "127.0.0.1", host: 5984, auto_correct: true
    lr49.ssh.insert_key = false
    lr49.vm.provider "virtualbox" do |vb|
      # Display the VirtualBox GUI when booting the machine
      vb.gui = false

      # Customize the amount of memory on the VM:
      vb.memory = "1024"

      vb.name = "LR Node v.49"
    end

    lr49.vm.provision "shell", path: "bin/post-provision-lr49.sh",
      args: ["AF82338A", "lr49.local"]

  end


  otherlr51Nodes = {
    "lr51a" =>
      {
        ip: 52,
        keydir: "a",
        signkey: "5AC53DD3"
      },
    "lr51b" =>
      {
        ip: 53,
        keydir: "b",
        signkey: "5AC53DD3"
      },
    "lr51c" =>
      {
        ip: 54,
        keydir: "a",
        signkey: "5AC53DD3"
      }
  }


  otherlr51Nodes.each_pair do |nodename, node_info|
    base_ip = node_info[:ip]
    key_dir = node_info[:keydir]
    signkey = node_info[:signkey]

    config.vm.define nodename do |lr51|
      # lr51.vm.box = "lr-51b"
      lr51.vm.box = "learningregistry/lr-ubuntu-51"
      lr51.vm.host_name = "#{nodename}.local"

      lr51.vm.network "private_network", ip: "10.0.1.#{base_ip}"
      lr51.vm.network "forwarded_port", guest: 80, host: 8080, auto_correct: true
      # lr51.vm.network "forwarded_port", guest: 5984, guest_ip: "127.0.0.1", host: 5985, auto_correct: true
      lr51.ssh.insert_key = false

      lr51.vm.provision "shell", path: "bin/post-provision-lr51.sh",
          args:["#{signkey}", "#{nodename}.local"]

      if ["lr51a", "lr51b", "lr51c"].include?(nodename)
        lr51.vm.provision "configure-whitelist", type:"shell", path: "bin/install_whitelist_key.py",
          args:["-keydir", "/vagrant/signing_keys/pub_keys_#{key_dir}/"]

        lr51.vm.provision "restart-node", type:"shell", inline: <<-SCRIPT
          sudo service learningregistry stop
          sleep 60
          sudo service learningregistry start
          sleep 10
          sudo cat /var/log/learningregistry/uwsgi.log
        SCRIPT

        lr51.vm.provision "fix-couchdb", type:"shell", inline: <<-SCRIPT
          /home/learnreg/env/bin/python /vagrant/bin/fix_couch.py -audience #{nodename}.local
        SCRIPT
      end

      lr51.vm.provider "virtualbox" do |vb|
        # Display the VirtualBox GUI when booting the machine
        vb.gui = false

        # Customize the amount of memory on the VM:
        vb.memory = "1024"

        vb.name = "LR Node v.51 #{nodename}"
      end
    end

  end


  config.vm.define "lruser" do |lruser|
    # lruser.vm.box = "rjkernick/linuxMint17Xfce"
    # lruser.vm.box = "lruserb"
    lruser.vm.box = "learningregistry/lr-user"
    lruser.vm.host_name = "lruser.local"

    # lruser.vm.network "private_network", ip: "10.0.0.5"
    lruser.vm.network "private_network", type: "dhcp"
    lruser.ssh.insert_key = false

    lruser.vm.provider "virtualbox" do |vb|
      # Display the VirtualBox GUI when booting the machine
      vb.gui = true

      # Customize the amount of memory on the VM:
      vb.memory = "2048"

      vb.name = "LR User"
    end
  end

  # The most common configuration options are documented and commented below.
  # For a complete reference, please see the online documentation at
  # https://docs.vagrantup.com.

  # Every Vagrant development environment requires a box. You can search for
  # boxes at https://atlas.hashicorp.com/search.
  # config.vm.box = "ubuntu-couchdb"

  # config.vm.host_name = "lr49.local"
  # Disable automatic box update checking. If you disable this, then
  # boxes will only be checked for updates when the user runs
  # `vagrant box outdated`. This is not recommended.
  # config.vm.box_check_update = false

  # Create a forwarded port mapping which allows access to a specific port
  # within the machine from a port on the host machine. In the example below,
  # accessing "localhost:8080" will access port 80 on the guest machine.
  # config.vm.network "forwarded_port", guest: 80, host: 8080

  # Create a private network, which allows host-only access to the machine
  # using a specific IP.
  # config.vm.network "private_network", ip: "192.168.33.10"

  # Create a public network, which generally matched to bridged network.
  # Bridged networks make the machine appear as another physical device on
  # your network.
  # config.vm.network "public_network"

  # Share an additional folder to the guest VM. The first argument is
  # the path on the host to the actual folder. The second argument is
  # the path on the guest to mount the folder. And the optional third
  # argument is a set of non-required options.
  # config.vm.synced_folder "../data", "/vagrant_data"

  # Provider-specific configuration so you can fine-tune various
  # backing providers for Vagrant. These expose provider-specific options.
  # Example for VirtualBox:
  #
   # config.vm.provider "virtualbox" do |vb|
   #   # Display the VirtualBox GUI when booting the machine
   #   vb.gui = true

   #   # Customize the amount of memory on the VM:
   #   vb.memory = "2048"
   # end
  #
  # View the documentation for the provider you are using for more
  # information on available options.

  # Define a Vagrant Push strategy for pushing to Atlas. Other push strategies
  # such as FTP and Heroku are also available. See the documentation at
  # https://docs.vagrantup.com/v2/push/atlas.html for more information.
  # config.push.define "atlas" do |push|
  #   push.app = "YOUR_ATLAS_USERNAME/YOUR_APPLICATION_NAME"
  # end

  # Enable provisioning with a shell script. Additional provisioners such as
  # Puppet, Chef, Ansible, Salt, and Docker are also available. Please see the
  # documentation for more information about their specific syntax and use.
  # config.vm.provision "shell", inline: <<-SHELL
  #   sudo apt-get update
  #   sudo apt-get install -y apache2
  # SHELL
end