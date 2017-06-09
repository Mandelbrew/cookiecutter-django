#!/bin/bash

UWSGI_NUM_PROCESSES=1
UWSGI_NUM_THREADS=15
UWSGI_UID=uwsgi
UWSGI_GID=uwsgi

cd /opt/django

# Find manage if not given
if [ -z "$MANAGE_PATH" ]; then
	MANAGE_PATH=`find /opt/django | egrep '/opt/django/[^/]*manage.py'`
fi

# Find wsgi if not given
if [ -z "$WSGI_PATH" ]; then
	WSGI_PATH=`find /opt/django | egrep '/opt/django/[^/]+/wsgi.py'`
fi

[ -n "$WSGI_MODULE" ] && UWSGI_MODULE="--module $WSGI_MODULE"

# Collect static files
python ${MANAGE_PATH} collectstatic --noinput

uwsgi --http :8080 \
	--chdir /opt/django \
	--wsgi-file $WSGI_PATH $UWSGI_MODULE \
	--master --processes $UWSGI_NUM_PROCESSES \
	--threads $UWSGI_NUM_THREADS \
	--uid $UWSGI_UID \
	--gid $UWSGI_GID

