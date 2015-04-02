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