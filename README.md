# djfoundation1

An experiment in integrating Zurb Foundation and Django together.

Uses a Vagrant virtual machine for software development.

# Install VirtualBox, Vagrant, and Ansible on host box

## Ubuntu 14.04 LTS

    $ sudo apt-get install vagrant
    $ sudo apt-get install virtualbox
    $ sudo apt-get install ansible

## Mac OS X Yosimite

1) Download and install VirtualBox (http://www.virtualbox.org)
2) Download and install Vagrant (http://www.vagrantup.com)
3) Install Python 2.7 and PIP

    $ sudo easy_install pip

4) Install Ansible

    $ sudo pip install ansible

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

    vagrant@xyz $ cd /vagrant/djfoundation1/foundation
    vagrant@xyz $ foundation watch
