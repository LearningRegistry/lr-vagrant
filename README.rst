*****************
LR Vagrant Readme
*****************

License
=======

Copyright 2015 Jim Klo <jim@arkitec.com>

Licensed under the Apache License, Version 2.0 (the "License");
you may not use this file except in compliance with the License.
You may obtain a copy of the License at

    http://www.apache.org/licenses/LICENSE-2.0

Unless required by applicable law or agreed to in writing, software
distributed under the License is distributed on an "AS IS" BASIS,
WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
See the License for the specific language governing permissions and
limitations under the License.


Vagrant Box Detailas
====================

There are the basic Vagrant VMs as listed in the table below:

+-------------+---------------+--------------------------------------------------+
| Vagrant ID  | Hostname      | Description                                      |
+=============+===============+==================================================+
| lr          | lr.local      | This is a Learning Registry node with a base     |
|             |               | configuration, running latest stable LR code.    |
+-------------+---------------+--------------------------------------------------+
| lr51        | lr51.local    | **Optional VM.** This is a Learning Registry     |
|             |               | v.51 node with a base configuration.             |
+-------------+---------------+--------------------------------------------------+
| lr49        | lr49.local    | **Optional VM.** This is a Learning Registry     |
|             |               | v.49 node with a base configuration.             |
+-------------+---------------+--------------------------------------------------+
| lruser      | lruser.local  | **Optional VM.** This is a Linux Mint desktop VM.|
|             |               | Can be used to access the apps running on lr51   |
|             |               | VM. Alternative to using this is updating host's |
|             |               | hosts file to point to IP's of the VMs.          |
+-------------+---------------+--------------------------------------------------+


Instructions
============

1. Install VirtualBox https://www.virtualbox.org
2. Install Vagrant https://www.vagrantup.com
3. Open a Terminal, shell, or command prompt and clone this repository.

	**Using bash**

	::

	    $ mkdir -p /<some work path>/
	    $ cd /<some work path>/
	    $ git clone https://github.com/LearningRegistry/lr-vagrant.git lr-vagrant
	    $ cd lr-vagrant

4. Install some vagrant plugins.

 	**Using bash**

 	::

    	$ vagrant plugin install vagrant-hostmanager

5. Launch the VM's. Each line launches a different VM.

	**Using bash**

	::

		$ vagrant up lr ## this is a Learning Registry demo node, using latest stable code
		$ vagrant up lruser  ## this is a Linux Mint desktop that can be used as a client on the same network as the other VMs

6. Optional LR User VM

    **Using bash**

    ::

        $ vagrant up lruser  ## this is a Linux Mint desktop that can be used as a client on the same network as the other VMs


7. VMs should be running... http://lr.local/


Notes
-----
* You will need approximately 10 GB free on your host machine with 2GB RAM or more, 8+ preferred... for each VM you want to run.
* The VMs will take quite a long time to download the base boxes the first time, but are then cached locally in ``$HOME/.vagrant``. You can get a list of these boxes by issuing the following command.

	**Using bash**

	::

		$ vagrant box list

* You can set an environment variable in your profile if you want to use an external drive to store VMs: ``export VAGRANT_HOME=/Volumes/MyExternalDrive/vagrant``
* You may be prompted to enter your host machine admin password to update ``/etc/hosts`` or equivalent on Windows.
* When the box is launched, this directory is shared on the the vagrant box as ``/vagrant``
* This project was initially developed to test distribution between nodes running v0.49 and v0.51 and use of admin whitelisted keys. Information on those setups can be found in ``test/LRv49-51_ReadMe.rst``

Setup for development from the host machine
-----
Using a vagrant synced folder you can do development on your local (host) machine while running the code on the virtual machine. To implement this setup (only needs to be done once):

1. Shutdown the node if it's running: ``vagrant halt lr``

2. Uncomment and update the ``lr.vm.synced_folder`` in Vagrantfile with your local LearningRegistry src folder location

   * If you are running on Windows, you will need to escape your file path. i.e.: 
 
    ::

		"G:\\LearningRegistry\\source"
		
3. Start the node, and then run the ``bin/setup_local_dev.sh`` script

    **Using bash**

    ::

        $ vagrant up lr
        $ vagrant ssh lr -c '/vagrant/bin/setup_local_dev.sh'



Scripts
=======

The ``bin`` directory contains a list of misc scripts that can be run via

	**Using bash**

	::

	    $ vagrant ssh <boxname> -c '/vagrant/bin/<script name>'

+-------------------------------------------------------------+----------------------------------------------------------------------------------------------+
| Script Name                                                 | Description                                                                                  |
+=============================================================+==============================================================================================+
| ``set-insecure-key.sh``                                     | Preps a vagrant box for repackaging.                                                         |
+-------------------------------------------------------------+----------------------------------------------------------------------------------------------+
| ``provision-lr-branch.sh <remote_name> <remote_url> <tag>`` | Adds a new remote to the existing checked out LR code base and                               |
|                                                             | checks out the specified tag.                                                                |
+-------------------------------------------------------------+----------------------------------------------------------------------------------------------+
| ``provision-fix-start-script.sh``                           | Runs the LR ``service_util.py`` with default options and then                                |
|                                                             | replaces the existing script in ``/etc/init.d/`` with the newly                              |
|                                                             | generated one.                                                                               |
+-------------------------------------------------------------+----------------------------------------------------------------------------------------------+
| ``install_whitelist_key.py``                                | Configures ``/vagrant/signing_keys/pub_keys/`` as the Admin Whitelist Public Keys directory. |
+-------------------------------------------------------------+----------------------------------------------------------------------------------------------+
| ``setup_local_dev.sh``                                      | Sets LR_HOME to /lr_src synced_folder for local dev (see instructions above)                 |
+-------------------------------------------------------------+----------------------------------------------------------------------------------------------+



GPG Public and Private Keys
===========================

Signing keys for performing external document signing are located in ``./signing_keys``.

+------------------------------------------+------------+------------------------------------------+
| Key ID / Fingerprint                     | Passphrase | email                                    |
+==========================================+============+==========================================+
| 175FBB7D5D6F5B9A504F95D8B7B49BA3A7409F8A | whitelist  | jim.klo+whitelist@learningregistry.org   |
+------------------------------------------+------------+------------------------------------------+
| 01916AE1DC8F279352E3FE6705510FF20CC118C7 | vagrant    | administratory+test@learningregistry.org |
+------------------------------------------+------------+------------------------------------------+
| 01916AE1DC8F279352E3FE6705510FF20CC118C7 | vagrant    | jim.klo+vagrant@learningregistry.org     |
+------------------------------------------+------------+------------------------------------------+
| 59CB75D2C7D6F8FB649E30EF9E735BEE5AC53DD3 | vagrant    | jim.klo+test.51@learningregistry.org     |
+------------------------------------------+------------+------------------------------------------+
| 0180320D8A7698E0104790374212BA1AAF82338A | vagrant    | jim.klo+test.49@learningregistry.org     |
+------------------------------------------+------------+------------------------------------------+
