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
PROJECT_DIR = os.path.realpath(os.path.curdir)
SECRETS_DIR = os.path.join(PROJECT_DIR, 'secrets')
COMMON_SECRETS = {
    # Project
    "PROJECT_NAME": "{{ cookiecutter.project_name }}",
    "PROJECT_SLUG": "{{ cookiecutter.project_slug }}",
    "PROJECT_STATIC_ROOT": "application/static/",

    # Docker
    "DOCKER_IMAGE": "{{ cookiecutter.project_slug }}",

    # Webpack
    "WEBPACK_OUTPUT_PATH": "./application/static/assets",

    # Django
    "DJANGO_SETTINGS_MODULE": "config.settings",
    "DJANGO_EMAIL_HOST": "smtp.{{ cookiecutter.project_domain }}",
    "DJANGO_EMAIL_PORT": "587",
    "DJANGO_EMAIL_HOST_USER": "{{ cookiecutter.project_slug }}@{{ cookiecutter.project_domain }}",
    "DJANGO_DEFAULT_FROM_EMAIL": "contact@{{ cookiecutter.project_domain }}",

    # AWS
    "AWS_ACCESS_KEY_ID": "{{cookiecutter.project_slug|upper()}}_KEY_ID",
    "AWS_SECRET_ACCESS_KEY": "{{cookiecutter.project_slug|upper()}}_ACCESS_KEY",
    "AWS_S3_REGION": "us-west-2",
    "AWS_S3_BUCKET": "{{ cookiecutter.project_slug }}-assets",

    # DB
    "DB_NAME": "{{ cookiecutter.project_slug }}",
    "DB_USER": "{{ cookiecutter.project_slug }}",
    "DB_HOST": "postgres",
    "DB_PORT": "5432",

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


def write_secrets(path, name, secrets):
    env_f = os.path.join(path, '{0}.env'.format(name))
    exp_f = os.path.join(path, '{0}.export'.format(name))

    if not os.path.exists(path):
        os.makedirs(path)

    if os.path.exists(env_f):
        print('ERROR: {0} already exists. Refusing to overwrite.'.format(env_f))
    else:
        with open(env_f, 'w') as f:
            f.write("".join(["{0}={1}\n".format(x, secrets[x]) for x in sorted(secrets)]))

    if os.path.exists(exp_f):
        print('ERROR: {0} already exists. Refusing to overwrite.'.format(exp_f))
    else:
        with open(exp_f, 'w') as f:
            f.write("".join(["export {0}='{1}'\n".format(x, secrets[x]) for x in sorted(secrets)]))


def generate_secrets():
    # Development

    dev_secrets = COMMON_SECRETS.copy()
    dev_secrets.update({
        # Project
        "PROJECT_DEBUG": "true",

        # Webpack
        "WEBPACK_CONFIG": "./assets/webpack.development.config.js",

        # Docker
        "DOCKER_COMPOSE_CONFIG": "./docker/docker-compose.development.yml",
        "DOCKER_PROJECT_NAME": "{{ cookiecutter.project_slug }}-development",

        # Django
        "DJANGO_EMAIL_HOST_PASSWORD": get_random_string(64, string.ascii_letters + string.digits),
        "DJANGO_SECRET_KEY": get_random_string(),
        "DJANGO_HONEYPOT_FIELD_NAME": get_random_string(16, string.ascii_letters + string.digits),
        "DJANGO_DEFAULT_FILE_STORAGE": "config.s3_storages.MediaStorage",

        # AWS
        "AWS_S3_MEDIA_PATH": "/development/media/",
        "AWS_S3_STATIC_PATH": "/development/static/",
        "AWS_S3_BACKUPS_PATH": "'/development/backups/'",

        # DB
        "DB_PASSWORD": get_random_string(64, string.ascii_letters + string.digits),
    })

    write_secrets(SECRETS_DIR, 'development', dev_secrets)

    # Staging

    stg_secrets = COMMON_SECRETS.copy()
    stg_secrets.update({
        # Webpack
        "WEBPACK_CONFIG": "./assets/webpack.production.config.js",

        # Docker
        "DOCKER_COMPOSE_CONFIG": "./docker/docker-compose.production.yml",
        "DOCKER_PROJECT_NAME": "{{ cookiecutter.project_slug }}-staging",

        # Django
        "DJANGO_EMAIL_HOST_PASSWORD": get_random_string(64, string.ascii_letters + string.digits),
        "DJANGO_SECRET_KEY": get_random_string(),
        "DJANGO_HONEYPOT_FIELD_NAME": get_random_string(16, string.ascii_letters + string.digits),
        "DJANGO_STATICFILES_STORAGE": "config.s3_storages.StaticStorage",
        "DJANGO_DEFAULT_FILE_STORAGE": "config.s3_storages.MediaStorage",

        # AWS
        "AWS_S3_MEDIA_PATH": "/staging/media/",
        "AWS_S3_STATIC_PATH": "/staging/static/",
        "AWS_S3_BACKUPS_PATH": "'/staging/backups/'",

        # DB
        "DB_PASSWORD": get_random_string(64, string.ascii_letters + string.digits),
    })

    write_secrets(SECRETS_DIR, 'staging', stg_secrets)

    # Production

    prod_secrets = stg_secrets.copy()  # Notice this difference
    prod_secrets.update({
        # Docker
        "DOCKER_PROJECT_NAME": "{{ cookiecutter.project_slug }}-production",

        # AWS
        "AWS_S3_MEDIA_PATH": "/production/media/",
        "AWS_S3_STATIC_PATH": "/production/static/",
        "AWS_S3_BACKUPS_PATH": "'/production/backups/'",
    })

    write_secrets(SECRETS_DIR, 'production', prod_secrets)


generate_secrets()
