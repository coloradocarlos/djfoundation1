#!/bin/bash
# Run once after vagrant provisioning
pushd foundation
npm install
bower install
foundation build
popd
# Then use 'workon djfoundation1' to get to this environments
source /usr/share/virtualenvwrapper/virtualenvwrapper.sh
mkvirtualenv -a /vagrant -r requirements.txt --python=`which python3` djfoundation1
# Run database initialization
python --version
./manage.py migrate
# Create superuser if none exist
superusers=`echo "select count(*)>0 from auth_user;" | psql -P "tuples_only=on" djfoundation1`
if [ "$superusers" = " f" ]; then
	./manage.py createsuperuser
fi
echo -e "\nTo run manage.py enter 'workon djfoundation1'\n"
