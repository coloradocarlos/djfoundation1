#!/bin/bash
# Run once after vagrant provisioning
pushd foundation
npm install
bower install
popd
# Then use 'workon djfoundation1' to get to this environments
source /usr/share/virtualenvwrapper/virtualenvwrapper.sh
mkvirtualenv -a /vagrant -r requirements.txt --python=`which python3` djfoundation1
echo -e "\nTo run manage.py enter 'workon djfoundation1'\n"
