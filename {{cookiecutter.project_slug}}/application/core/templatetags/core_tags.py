from django import template
from django.utils.text import slugify
from widget_tweaks.templatetags.widget_tweaks import widget_type

from core.models import DesignSettings

register = template.Library()


# region Filters

@register.filter
def get_type(value):
    return type(value)


# endregion

# region Simple Tags

# endregion

# region Assignment Tags

@register.assignment_tag(takes_context=True)
def get_site_header(context):
    if 'request' in context:
        settings = DesignSettings.for_site(context['request'].site)
        if settings.header:
            return settings.header.contents
    return ''


@register.assignment_tag(takes_context=True)
def get_site_footer(context):
    if 'request' in context:
        settings = DesignSettings.for_site(context['request'].site)
        if settings.footer:
            return settings.footer.contents
    return ''


@register.assignment_tag(takes_context=True)
def get_root_page(context):
    """this returns a core.Page, not the implementation-specific model used
    so object-comparison to self will return false as objects would differ"""
    return context['request'].site.root_page

# endregion

# region Inclusion Tags

# endregion
