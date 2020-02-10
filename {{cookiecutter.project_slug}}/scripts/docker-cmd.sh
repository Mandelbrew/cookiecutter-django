#!/usr/bin/env bash

set -efx

# Prep env
IFS=$(echo -en "\n\b")
GUNICORN_USER=nobody
GUNICORN_BIND_ADDRESS=0.0.0.0:8080
GUNICORN_WORKERS=3
GUNICORN_THREADS=3
GUNICORN_ACCESS_LOG=-
GUNICORN_ERROR_LOG=-
CRON_CONFIG=/etc/crontab
CRON_TASK_PREFIX='CRON_TASK_'

# Find manage if not given
if [ -z "${MANAGE_PATH}" ]; then
	MANAGE_PATH=`find . | egrep '[^/]*manage.py'`
fi

# Default wsgi if not given
if [ -z "${WSGI_MODULE}" ]; then
    WSGI_MODULE='config.wsgi'
fi

# Make env available to cron
echo "# Environment" >>${CRON_CONFIG}
for var in $(printenv); do
    echo ${var} >>${CRON_CONFIG}
done
echo "#" >>${CRON_CONFIG}

# Parse custom tasks
echo "# Custom tasks" >>${CRON_CONFIG}
for task in $(printenv | grep "${CRON_TASK_PREFIX}" | cut -d= -f2); do
    echo ${task} >>${CRON_CONFIG}
done
echo "# An empty line is required at the end of this file for a valid cron file." >>${CRON_CONFIG}

if [ ${DJANGO_DEBUG:-false} == "true" ]; then
    # Django server
    python ${MANAGE_PATH} runserver 0.0.0.0:8080
else
    # Collect static files
    python ${MANAGE_PATH} check
    python ${MANAGE_PATH} collectstatic --noinput

    # Ready
    gunicorn ${WSGI_MODULE} \
        --user ${GUNICORN_USER} \
        --bind ${GUNICORN_BIND_ADDRESS} \
        --workers ${GUNICORN_WORKERS} \
        --threads ${GUNICORN_THREADS} \
        --access-logfile ${GUNICORN_ACCESS_LOG} \
        --error-logfile ${GUNICORN_ERROR_LOG}
fi
