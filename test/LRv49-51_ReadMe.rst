Setting up Learning Registry 0.49 VM
====================================
+-------------+---------------+--------------------------------------------------+
| Vagrant ID  | Hostname      | Description                                      |
+=============+===============+==================================================+
| lr49        | lr49.local    | This is a legacy Learning Registry v.49 node     |
|             |               | with a base configuration using a sample GPG Key.|
+-------------+---------------+--------------------------------------------------+

1. Complete steps 1-4 on the main page Readme first.
2. Launch lr49 VM. Each line launches a different VM.
	**Using bash**
	::

		$ vagrant up lr49   ## this is a Learning Registry v.49 demo node.

Workflows
---------

Test .49 to .51 distribution
^^^^^^^^^^^^^^^^^^^^^^^^^^^^
**Steps**


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
