#!/bin/bash

cd /opt/django


if [ -z "$MANAGE_PATH" ]; then
	MANAGE_PATH=`find /opt/django | egrep '/opt/django/[^/]*manage.py'`
fi

python $MANAGE_PATH collectstatic --noinput
until python $MANAGE_PATH migrate --noinput; do
	echo "Postgres is unavailable - sleeping";
	sleep 1;
done
python $MANAGE_PATH loaddata init

# wsgi path
if [ -z "$WSGI_PATH" ]; then
	WSGI_PATH=`find /opt/django | egrep '/opt/django/[^/]+/wsgi.py'`
fi

[ -n "$WSGI_MODULE" ] && UWSGI_MODULE="--module $WSGI_MODULE"

uwsgi --http :8080 \
	--chdir /opt/django \
	--wsgi-file $WSGI_PATH $UWSGI_MODULE \
	--master --processes $UWSGI_NUM_PROCESSES \
	--threads $UWSGI_NUM_THREADS \
	--uid $UWSGI_UID \
	--gid $UWSGI_GID \
	--logto2 $UWSGI_LOG_FILE
