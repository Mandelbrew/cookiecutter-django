"""config URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/1.8/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  url(r'^$', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  url(r'^$', Home.as_view(), name='home')
Including another URLconf
    1. Add a URL to urlpatterns:  url(r'^blog/', include('blog.urls'))
"""
from django.conf import settings
from django.conf.urls import include, url
from django.conf.urls.static import static
from django.contrib import admin
from wagtail.wagtailcore import urls as wagtail_urls
from wagtail.wagtailadmin import urls as wagtailadmin_urls
from wagtail.wagtailsearch import urls as wagtailsearch_urls
from wagtail.wagtaildocs import urls as wagtaildocs_urls

admin.site.site_header = 'Site Administration'

urlpatterns = [
                  url(r'^django-admin/', include(admin.site.urls)),
                  url(r'^admin/', include(wagtailadmin_urls)),
                  url(r'^search/', include(wagtailsearch_urls)),
                  url(r'^documents/', include(wagtaildocs_urls)),
                  url(r'', include(wagtail_urls)),

              ] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
