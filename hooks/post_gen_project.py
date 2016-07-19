"""
Does the following:
1. Generates and saves random secret key
2. Removes the taskapp if celery isn't going to be used
3. Removes the .idea directory if PyCharm isn't going to be used
A portion of this code was adopted from Django's standard crypto functions and
utilities, specifically:
    https://github.com/django/django/blob/master/django/utils/crypto.py
"""
from __future__ import print_function
import os
import random
import shutil

import sys
from cookiecutter.main import cookiecutter

# Constants
PROJECT_DIRECTORY = os.path.realpath(os.path.curdir)
USER_HOME = os.path.expanduser('~')
USER_SECRETS = os.path.join(USER_HOME, '.secrets')
PROJECT_SECRETS = os.path.join(USER_SECRETS, '{{ cookiecutter.project_slug }}')


def get_random_string(
        length=50,
        allowed_chars='abcdefghijklmnopqrstuvwxyz0123456789!@#%^&*(-_=+)'):
    """
    Returns a securely generated random string.
    The default length of 12 with the a-z, A-Z, 0-9 character set returns
    a 71-bit value. log_2((26+26+10)^12) =~ 71 bits
    """

    return ''.join(random.SystemRandom().choice(allowed_chars) for i in range(length))


def generate_secrets():
    if os.path.exists(PROJECT_SECRETS):
        print('ERROR: {0} already exists. Refusing to overwrite.'.format(PROJECT_SECRETS))
        sys.exit(1)
    else:
        os.makedirs(PROJECT_SECRETS)

    base_secrets = [
        # Project
        "PROJECT_NAME='{{ cookiecutter.project_name }}'",
        "PROJECT_SLUG='{{ cookiecutter.project_slug }}'",

        # PostgreSQL
        "POSTGRES_DB='{{ cookiecutter.db_name }}'",
        "POSTGRES_USER='{{ cookiecutter.db_user }}'",
        "POSTGRES_PASSWORD='{{ cookiecutter.db_password }}'",

        # Django
        "DJANGO_DB_HOST='{{ cookiecutter.db_host }}'",
        "DJANGO_DB_PORT='{{ cookiecutter.db_port }}'",
        "DJANGO_DB_NAME='{{ cookiecutter.db_name }}'",
        "DJANGO_DB_USER='{{ cookiecutter.db_user }}'",
        "DJANGO_DB_PASSWORD='{{ cookiecutter.db_password }}'",  # TODO: generate a password for every env
        "DJANGO_EMAIL_HOST='{{ cookiecutter.email_host }}'",
        "DJANGO_EMAIL_PORT='{{ cookiecutter.email_port }}'",
        "DJANGO_EMAIL_USER='{{ cookiecutter.email_user }}'",
        "DJANGO_EMAIL_PASSWORD='{{ cookiecutter.email_password }}'",
        "DJANGO_DEFAULT_FROM_EMAIL='{{ cookiecutter.django_default_from_email }}'",
        "DJANGO_SECRET_KEY='{0}'".format(get_random_string()),
        "DJANGO_ALLOWED_HOSTS='.{{ cookiecutter.django_allowed_hosts }}'",

        # AWS
        "AWS_ACCESS_KEY_ID='{{ cookiecutter.aws_access_key_id }}'",
        "AWS_SECRET_ACCESS_KEY='{{ cookiecutter.aws_secret_access_key }}'",
        "AWS_STORAGE_BUCKET_NAME='{{ cookiecutter.aws_storage_bucket_name }}'",

        # uWSGI
        "UWSGI_NUM_PROCESSES='1'",
        "UWSGI_NUM_THREADS='15'",
    ]

    development = base_secrets + [
        "DJANGO_ENVIRONMENT='docker_development'",
    ]

    with open(os.path.join(PROJECT_SECRETS, 'development.env'), 'w') as f:
        f.write("".join(["{0}\n".format(x) for x in development]))

    with open(os.path.join(PROJECT_SECRETS, 'development.sh'), 'w') as f:
        f.write("".join(["export {0}\n".format(x) for x in development]))

    staging = base_secrets + [
        "DJANGO_ENVIRONMENT='docker_staging'",
    ]

    with open(os.path.join(PROJECT_SECRETS, 'staging.env'), 'w') as f:
        f.write("".join(["{0}\n".format(x) for x in staging]))

    with open(os.path.join(PROJECT_SECRETS, 'staging.sh'), 'w') as f:
        f.write("".join(["export {0}\n".format(x) for x in staging]))

    production = base_secrets + [
        "DJANGO_ENVIRONMENT='docker_production'",
    ]

    with open(os.path.join(PROJECT_SECRETS, 'production.env'), 'w') as f:
        f.write("".join(["{0}\n".format(x) for x in production]))

    with open(os.path.join(PROJECT_SECRETS, 'production.sh'), 'w') as f:
        f.write("".join(["export {0}\n".format(x) for x in production]))


generate_secrets()
