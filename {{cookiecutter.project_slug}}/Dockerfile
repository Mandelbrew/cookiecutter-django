FROM       python
MAINTAINER Carlos Avila <cavila@mandelbrew.com>

ENV        PYTHONUNBUFFERED       1
ENV        DEBIAN_FRONTEND        noninteractive

RUN        apt-get update -y \
           && apt-get install -y \
             logrotate \
           && apt-get autoremove -y \
           && apt-get clean -y \
           && rm -rf /var/lib/apt/lists/* \
           && pip install --no-cache-dir --upgrade pip setuptools wheel

EXPOSE     8080
WORKDIR    /opt/django

ADD        ./application /opt/django
RUN        pip install -r /opt/django/requirements.txt

ENV        UWSGI_NUM_PROCESSES    1
ENV        UWSGI_NUM_THREADS      15
ENV        UWSGI_UID              uwsgi
ENV        UWSGI_GID              uwsgi
ENV        UWSGI_LOG_FILE         /var/log/uwsgi/uwsgi.log

ADD        .docker/django/uwsgi.logrotate /etc/logrotate.d/uwsgi
RUN        pip install uwsgi && \
           useradd ${UWSGI_UID} -s /bin/false && \
           mkdir -p $(dirname ${UWSGI_LOG_FILE}) && \
           chown -R ${UWSGI_UID}:${UWSGI_GID} $(dirname ${UWSGI_LOG_FILE})

ADD        .docker/django/uwsgi-start.sh /
CMD        ["/uwsgi-start.sh"]