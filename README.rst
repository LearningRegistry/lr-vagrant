*****************
LR Vagrant Readme
*****************


Vagrant Box Details
===================

There are the basic Vagrant VMs as listed in the table below:

+-------------+---------------+--------------------------------------------------+
| Vagrant ID  | Hostname      | Description                                      |
+=============+===============+==================================================+
| lr49        | lr49.local    | This is a Learning Registry v.49 node with a     |
|             |               | base configuration using a sample GPG Key.       |
+-------------+---------------+--------------------------------------------------+
| lr51        | lr51.local    | This is a Learning Registry v.51 node with a     |
|             |               | base configuration using a sample GPG Key.       |
+-------------+---------------+--------------------------------------------------+
| lruser      | lruser.local  | This is a Linux Mint desktop VM. Can be used     |
|             |               | in-lieu of permitting the HOST's ``/etc/hosts``  |
|             |               | file from being modified.                        |
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
	    $ git clone https://bitbucket.org/jimklo/lr-vagrant.git lr-vagrant
	    $ cd lr-vagrant

4. Install some vagrant plugins.

 	**Using bash**

 	::

    	$ vagrant plugin install vagrant-hostmanager

5. Launch some VM's. Each line launches a different VM.
	
	**Using bash**

	::

		$ vagrant up lr49   ## this is a Learning Registry v.49 demo node.
		$ vagrant up lr51   ## this is a Learning Registry v.51 demo node.
		$ vagrant up lruser  ## this is a Linux Mint desktop that can be used as a client on the same network as the other VMs

6. VMs should be running.


Notes
-----
* You will need approximately 50 GB free on your host machine with 8GB RAM or more, 16+ preferred.
* The VMs will take quite a long time to download the base boxes the first time, but are then cached locally in ``$HOME/.vagrant``. You can get a list of these boxes by issuing the following command.

	**Using bash**

	::

		$ vagrant box list

* You may be prompted to enter your host machine admin password to update ``/etc/hosts`` or equivalent on Windows.
* When the box is launched, this directory is shared on the the vagrang box as ``/vagrant``
  

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



GPG Public and Private Keys
===========================

Signing keys for performing external document signing are located in ``./signing_keys``.

+------------------------------------------+------------+----------------------------------------+
| Key ID / Fingerprint                     | Passphrase | email                                  |
+==========================================+============+========================================+
| 175FBB7D5D6F5B9A504F95D8B7B49BA3A7409F8A | whitelist  | jim.klo+whitelist@learningregistry.org |
+------------------------------------------+------------+----------------------------------------+
| 01916AE1DC8F279352E3FE6705510FF20CC118C7 | vagrant    | jim.klo+vagrant@learningregistry.org   |
+------------------------------------------+------------+----------------------------------------+
| 59CB75D2C7D6F8FB649E30EF9E735BEE5AC53DD3 | vagrant    | jim.klo+test.51@learningregistry.org   |
+------------------------------------------+------------+----------------------------------------+
| 0180320D8A7698E0104790374212BA1AAF82338A | vagrant    | jim.klo+test.49@learningregistry.org   |
+------------------------------------------+------------+----------------------------------------+

