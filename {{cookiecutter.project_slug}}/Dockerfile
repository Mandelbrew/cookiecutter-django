FROM       python:3.6-slim
MAINTAINER Mandelbrew <contact@mandelbrew.com>

# Prep env
ENV        PYTHONUNBUFFERED=1 \
           DEBIAN_FRONTEND=noninteractive

WORKDIR	   /opt/docker

# Operating System
ADD        application/requirements.txt requirements.txt
RUN        set -ex \
           && build_deps='' \
           && apt-get update -y \
           && apt-get install -y --no-install-recommends \
                  ${build_deps} \
                  cron \
                  supervisor \
           && pip3 install --no-cache-dir --upgrade \
                  pip \
                  setuptools \
                  wheel \
           && pip3 install --no-cache-dir -r requirements.txt \
           && apt-get purge -y --auto-remove ${build_deps} \
           && apt-get autoremove -y \
           && apt-get clean -y \
           && rm -rf /var/lib/apt/lists/*

# Application
ADD        application .
ADD        scripts/supervisor-docker.conf /etc/supervisor/conf.d/
ADD        scripts/docker-cmd.sh /docker-cmd.sh

EXPOSE     8080

CMD        ["supervisord"]