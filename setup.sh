#!/bin/bash
# Run once after vagrant provisioning
# TODO: move this to the Ansible provisioner
pushd foundation
npm install
bower install
foundation build
popd
# Then use 'workon djsite' to get to this environments
# TODO: move this to the Ansible provisioner
source /usr/share/virtualenvwrapper/virtualenvwrapper.sh
mkvirtualenv -a /vagrant -r requirements.txt --python=`which python3` djsite
# Run database initialization
python --version
./manage.py migrate
./manage.py loaddata foods.json
# Create superuser if none exist
superusers=`echo "select count(*)>0 from auth_user;" | psql -P "tuples_only=on" djsite`
if [ "$superusers" = " f" ]; then
	echo "Creating Django superuser..."
	./manage.py createsuperuser
fi
echo -e "\nTo run manage.py enter 'workon djsite'\n"
