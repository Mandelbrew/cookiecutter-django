# Build paths inside the project like this: os.path.join(BASE_DIR, ...)
import os

BASE_DIR = os.path.dirname(
    os.path.dirname(
        os.path.dirname(
            os.path.abspath(__file__))))

# Quick-start development settings - unsuitable for production
# See https://docs.djangoproject.com/en/1.8/howto/deployment/checklist/

# SECURITY WARNING: keep the secret key used in production secret!
SECRET_KEY = os.environ['DJANGO_SECRET_KEY']

ALLOWED_HOSTS = ['*']

DEBUG = True

# region Applications

INSTALLED_APPS = (

    # Mandelbrew
    'core',

    # Mandelbrew POST
    'honeypot',
    'overextends',
    'widget_tweaks',

    # Wagtail PRE

    # Wagtail
    'wagtail.wagtailforms',
    'wagtail.wagtailredirects',
    'wagtail.wagtailembeds',
    'wagtail.wagtailsites',
    'wagtail.wagtailusers',
    'wagtail.wagtailsnippets',
    'wagtail.wagtaildocs',
    'wagtail.wagtailimages',
    'wagtail.wagtailsearch',
    'wagtail.wagtailadmin',
    'wagtail.wagtailcore',
    'wagtail.contrib.settings',

    # Wagtail POST
    'modelcluster',
    'taggit',

    # Django PRE
    'admin_bootstrapped_plus',
    'django_admin_bootstrapped',
    'django_comments_xtd',
    'django_comments',
    'django_markup',

    # Django
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    'django.contrib.sites',
    'django.contrib.humanize',

)

# endregion

# region Middleware

MIDDLEWARE_CLASSES = (

    # Django
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.auth.middleware.SessionAuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
    'django.middleware.security.SecurityMiddleware',

    # Whitenoise
    'whitenoise.middleware.WhiteNoiseMiddleware',

    # Wagtail
    'wagtail.wagtailcore.middleware.SiteMiddleware',
    'wagtail.wagtailredirects.middleware.RedirectMiddleware',

)

# endregion

ROOT_URLCONF = 'config.urls'

TEMPLATES = [
    {
        'BACKEND': 'django.template.backends.django.DjangoTemplates',
        'DIRS': [os.path.join(BASE_DIR, 'templates')],
        'APP_DIRS': True,
        'OPTIONS': {
            'context_processors': [
                # Django
                'django.template.context_processors.debug',
                'django.template.context_processors.request',
                'django.contrib.auth.context_processors.auth',
                'django.contrib.messages.context_processors.messages',
                # Wagtail
                'wagtail.contrib.settings.context_processors.settings',
            ],
        },
    },
]

WSGI_APPLICATION = 'config.wsgi.application'

# region Database

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.postgresql_psycopg2',
        'NAME': os.environ['DJANGO_DB_NAME'],
        'USER': os.environ['DJANGO_DB_USER'],
        'PASSWORD': os.environ['DJANGO_DB_PASSWORD'],
        'HOST': os.environ['DJANGO_DB_HOST'],
        'PORT': os.environ['DJANGO_DB_PORT'],
    }
}

# endregion


# region Internationalization

LANGUAGE_CODE = 'en-us'

TIME_ZONE = 'UTC'

USE_I18N = True

USE_L10N = True

USE_TZ = True

# endregion

# region AWS

AWS_ACCESS_KEY_ID = os.environ['AWS_ACCESS_KEY_ID']
AWS_SECRET_ACCESS_KEY = os.environ['AWS_SECRET_ACCESS_KEY']
AWS_STORAGE_BUCKET_NAME = os.environ['AWS_STORAGE_BUCKET_NAME']
AWS_HEADERS = {'Cache-Control': 'max-age=86400',}
AWS_QUERYSTRING_AUTH = False

# endregion

# region File Storage
DEFAULT_FILE_STORAGE = 'config.s3_storages.MediaStorage'

MEDIA_URL = '/media/'
MEDIA_ROOT = os.path.join(BASE_DIR, 'media')

STATIC_URL = '/static/'
STATIC_ROOT = os.path.join(BASE_DIR, 'static_collected')

STATICFILES_DIRS = [
    os.path.join(BASE_DIR, 'static'),
]

STATICFILES_FINDERS = (
    'django.contrib.staticfiles.finders.FileSystemFinder',
    'django.contrib.staticfiles.finders.AppDirectoriesFinder',
)

# endregion

# region Email

EMAIL_BACKEND = 'django.core.mail.backends.console.EmailBackend'
EMAIL_HOST = os.environ['DJANGO_EMAIL_HOST']
EMAIL_PORT = os.environ['DJANGO_EMAIL_PORT']
EMAIL_HOST_USER = os.environ['DJANGO_EMAIL_HOST_USER']
EMAIL_HOST_PASSWORD = os.environ['DJANGO_EMAIL_HOST_PASSWORD']
EMAIL_USE_TLS = True

DEFAULT_FROM_EMAIL = os.environ['DJANGO_DEFAULT_FROM_EMAIL']

# endregion

# region Sites

SITE_ID = 1

# endregion

# region Wagtail

WAGTAIL_SITE_NAME = os.environ['PROJECT_NAME']

# endregion

# region Comments XTD

COMMENTS_APP = "django_comments_xtd"
COMMENTS_XTD_MAX_THREAD_LEVEL = 4

# endregion
