cd /opt/miracle
export WORKON_HOME=/opt/virtualenvs
source /usr/bin/virtualenvwrapper.sh
workon miracle
python manage.py makemigrations
python manage.py migrate
deactivate
#uwsgi --http :8888 deploy/uwsgi/miracle.ini
uwsgi deploy/uwsgi/miracle.ini