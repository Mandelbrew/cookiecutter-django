FROM       python:3.6
MAINTAINER {{cookiecutter.project_author}} <{{cookiecutter.project_email}}>

# Prep env
ENV        PYTHONUNBUFFERED       1
ENV        DEBIAN_FRONTEND        noninteractive
ENV        UWSGI_NUM_THREADS      15
ENV        UWSGI_UID              uwsgi
ENV        UWSGI_GID              uwsgi

# Operating System
RUN        apt-get update -y \
           && apt-get install -y --no-install-recommends \
             supervisor \
           && apt-get autoremove -y \
           && apt-get clean -y \
           && rm -rf /var/lib/apt/lists/* \
           && pip3 install --no-cache-dir --upgrade pip setuptools wheel

# Supervisor
ADD        docker/supervisor-docker.conf /etc/supervisor/conf.d/
ADD        docker/docker-cmd.sh /

# Application
ADD        ./application /opt/django
RUN        pip3 install -r /opt/django/requirements.txt

# UWSGI
RUN        pip3 install uwsgi && useradd uwsgi -s /bin/false

EXPOSE     8080
WORKDIR	   /opt/django

CMD        ["supervisord", "-n"]