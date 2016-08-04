from .base import *

DEBUG = True

# region Applications

INSTALLED_APPS = (

    # Mandelbrew
    'core',
    'debug_toolbar',  # Development only!

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
    'wagtail.contrib.wagtailstyleguide',  # Development only!

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

# region Misc Apps

INTERNAL_IPS = ['192.168.99.1', '127.0.0.1', '0.0.0.0']

# endregion
