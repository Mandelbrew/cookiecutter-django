from .default import *

DEBUG = False

# region apps

INSTALLED_APPS = (

    # Django PRE
    'flat_responsive',  # Mobile support for flat theme
    'flat',  # Admin flat theme
    'colorfield',  # colorpicker field for admin

    # Django
    'django.contrib.auth',
    'django.contrib.admin',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    'django.contrib.sites',
    'django.contrib.humanize',

    # Mandelbrew
    'core',
    'pages',
    'blog',

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
    'wagtail.contrib.wagtailsitemaps',
    'wagtail.contrib.table_block',

    # Django plugins
    'django_extensions',
    'django_markup',
    'meta',
    'wagtailmetadata',
    'modelcluster',
    'taggit',
    'honeypot',
    'overextends',
    'widget_tweaks',
    'analytical',
    'svg_templatetag',  # adds template tag to inline SVGs

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

    # Honeypot
    'honeypot.middleware.HoneypotMiddleware'

)

# endregion

INTERNAL_IPS = []
