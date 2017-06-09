"""
Does the following:
- Generates and saves random secret key

A portion of this code was adopted from Django's standard crypto functions and
utilities, specifically:
    https://github.com/django/django/blob/master/django/utils/crypto.py
"""
from __future__ import print_function
import os
import random
import shutil
import string

import sys
from cookiecutter.main import cookiecutter

# Constants
PROJECT_DIRECTORY = os.path.realpath(os.path.curdir)

COMMON_SECRETS = {
        # Project
        "PROJECT_NAME": "{{ cookiecutter.project_name }}",
        "PROJECT_SLUG": "{{ cookiecutter.project_slug }}",

        # Webpack
        "WEBPACK_OUTPUT": "./application/static",

        # Django
        "DJANGO_EMAIL_HOST": "smtp.{{ cookiecutter.project_domain }}",
        "DJANGO_EMAIL_PORT": "587",
        "DJANGO_EMAIL_HOST_USER": "{{ cookiecutter.project_name }}@{{ cookiecutter.project_domain }}",
        "DJANGO_DEFAULT_FROM_EMAIL": "contact@{{ cookiecutter.project_domain }}",

        # AWS
        "AWS_ACCESS_KEY_ID": "{{cookiecutter.project_slug|upper()}}_KEY_ID",
        "AWS_SECRET_ACCESS_KEY": "{{cookiecutter.project_slug|upper()}}_ACCESS_KEY",
        "AWS_S3_HOST": "s3.amazonaws.com",
        "AWS_S3_BUCKET": "{{ cookiecutter.project_slug }}-assets",

        # DB
        "DB_NAME": "{{ cookiecutter.project_slug }}",
        "DB_USER": "{{ cookiecutter.project_slug }}",
        "DB_HOST": "postgres",
        "DB_PORT": "5432",

        # Analytics
        "GOOGLE_ANALYTICS_PROPERTY_ID": "UA-XXXXXX-2",
    }


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

    # Development

    dev_target = os.path.join(PROJECT_DIRECTORY, 'development.env')
    dev_secrets = COMMON_SECRETS.copy()
    dev_secrets.update({
        # Webpack
        "WEBPACK_CONFIG": "./assets/webpack.development.config.js",

        # Docker
        "DOCKER_IMAGE": "{{ cookiecutter.project_name }}-development",
        "DOCKER_COMPOSE": "./docker/docker-compose.development.yml",

        # Django
        "DJANGO_SETTINGS_MODULE": "config.settings.default",
        "DJANGO_EMAIL_HOST_PASSWORD": get_random_string(64, string.ascii_letters + string.digits),
        "DJANGO_SECRET_KEY": "={0}".get_random_string(),
        "DJANGO_HONEYPOT_FIELD_NAME": get_random_string(16, string.ascii_letters + string.digits),
        "DJANGO_MEDIA_URL": "=/development/media/",

        # DB
        "DB_PASSWORD": get_random_string(64, string.ascii_letters + string.digits),

        # Unison
        "UNISON_ROOT1": "./application/",
        "UNISON_ROOT2": "socket://localhost:5000/",
        "UNISON_IGNORE": "Name {.DS_Store,*.pyc}",
    })

    if os.path.exists(dev_target):
        print('ERROR: {0} already exists. Refusing to overwrite.'.format(dev_target))
        sys.exit(1)
    else:
        with open(dev_target, 'w') as f:
            f.write("".join(["{0}={1}\n".format(x, dev_secrets[x]) for x in dev_secrets]))


generate_secrets()
