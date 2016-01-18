# djfoundation1

An experiment in integrating Zurb Foundation and Django.

Uses a Vagrant virtual machine for software development for Foundation Sass (front-end) and Django (back-end).

# Install VirtualBox, Vagrant, and Ansible on host box

We are using Ansible 2.0 and playbooks may not work with earlier versions.

## Ubuntu 14.04 LTS

Note: ansible 1.8 in apt has a bug and does not handle npm dependencies correctly. Use the latest 2.0.0 in pip (ansible requires pip2 / python2).

    $ sudo apt-get install vagrant
    $ sudo apt-get install virtualbox
    $ sudo pip2 install ansible==2.0.0.2

## Mac OS X Yosimite

1) Download and install VirtualBox (http://www.virtualbox.org)
2) Download and install Vagrant (http://www.vagrantup.com)
3) Install Python 2.7 and PIP

    $ sudo easy_install pip

4) Install Ansible

Note: Ansible needs Python2.7.

    $ sudo pip install ansible==2.0.0.2

# Start Vagrant

    $ cd djfoundation1
    $ vagrant up

# Post vagrant up steps

## Build Zurb Foundation CSS

    $ vagrant ssh
    vagrant@xyz $ cd /vagrant
    vagrant@xyz $ cd foundation
    vagrant@xyz $ npm install
    vagrant@xyz $ bower install
    vagrant@xyz $ foundation build

 # Run Foundation Sass auto-rebuild

Runs a minimal web server on port 8080, with additional service on port 35729 for LiveReload browser plugin:

    vagrant@xyz $ cd /vagrant/foundation
    vagrant@xyz $ foundation watch
