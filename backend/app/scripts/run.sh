#!/bin/bash
/usr/local/bin/python manage.py migrate
/usr/local/bin/python manage.py collectstatic --noinput
/usr/local/bin/python manage.py compilemessages
/usr/local/bin/python manage.py update_translation_fields
exec /usr/local/bin/gunicorn  -c /scripts/gunicorn.conf.py project.wsgi
