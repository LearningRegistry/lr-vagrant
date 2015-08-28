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

Workflows
=========

Test .49 to .51 distribution
----------------------------

Steps
^^^^^

0. Provision 2 nodes

     a) lr49.local (node A)
     b) lr51.local (node B)

1. Configure node distribution
	 
	 a) lr49.local --> lr51.local
	    
2. Publish .49 document to node A. (expect success)

3. Publish .51 document to node A. (expect failure)
   
4. Trigger distribution on node A.

5. Validate .49 document is on node B.

6. Destroy all nodes

7. Provision 2 nodes

     a) lr49.local (node A)
     b) lr51.local (node B)

8. Configure node distribution
	 
	 a) lr51.local --> lr49.local
	    
9. Publish .49 document to node B. (expect success)

10. Publish .51 document to node B. (expect success)
   
11. Trigger distribution on node B.

12. Validate .49 document is on node A.

13. Validate .51 document is on node A.


Commands
^^^^^^^^

.. code-block:: bash

    vagrant up lr49 lr51
    vagrant ssh lr49 -c "/home/learnreg/env/bin/python /vagrant/bin/distribute.py -node http://lr49.local -target http://lr51.local -contact jim.klo@learningregistry.org"
	vagrant ssh lr49 -c "sudo service learningregistry stop; sleep 60; sudo service learningregistry start"
	vagrant ssh lr49 -c "curl -X POST http://lr49.local/distribute"
	# publish documents on lr49.local (publish script changed)
	# verify documents on lr51.local (check in browser)
	vagrant destroy lr49 lr51

	vagrant up lr49 lr51
    vagrant ssh lr51 -c "/home/learnreg/env/bin/python /vagrant/bin/distribute.py -node http://lr51.local -target http://lr49.local -contact jim.klo@learningregistry.org"
	vagrant ssh lr51 -c "sudo service learningregistry stop; sleep 60; sudo service learningregistry start"
	vagrant ssh lr51 -c "curl -X POST http://lr51.local/distribute"
	# publish documents on lr51.local (publish script changed)
	# verify documents on lr49.local (check in browser)
	vagrant destroy lr49 lr51



Test .51 Whitelist Keys
-----------------------

Steps
^^^^^

0. Create new GPG keys

     a) 2 keys will be installed as whitelist keys
     b) 1 key will be installed as node signing key
     c) 1 key will be used as a local signing key

1. Provision 3 nodes:

     a) lr51a.local (node A)

          0. install node signing key
          1. install whitelist key A 

     b) lr51b.local (node B)

          0. install whitelist key B

     c) lr51c.local (node C)

          0. install whitelist key A

2. Configure node distribution
	 
	 a) lr51a.local --> lr51b.local
	 b) lr51a.local --> lr51c.local
	    
3. Publish a series of documents and replacments to lr51a.local

	 a) local signed original doc and local signed replacement
	 	  
	 	  0. this should always work (nodes A, B and C)
	 	  
	 b) local signed original doc and whitelist key A signed replacement
		  
		  0. this should work on nodes trusting whitelist key A (nodes A and C)
	
	 c) node signed original doc and whitelist key A signed replacement

	      0. this should work on nodes trusting whitelist key A (nodes A and C)
	      
	 d) node signed original doc and whitelist key B signed replacement

	      0. this should work on nodes trusting whitelist key B (node B)
             
4. Trigger distribution on node A.

5. Verify each nodes' distribution content.
   

Commands
^^^^^^^^

.. code-block:: bash

    vagrant up lr51a lr51b lr51c; ./test/test_distribute_whitelist.sh; ./test/test_whitelist.sh; vagrant ssh lr51a -c "curl -X POST http://lr51a.local/distribute"