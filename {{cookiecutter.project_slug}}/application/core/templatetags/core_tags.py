from django import template
from django.utils.text import slugify

register = template.Library()


@register.assignment_tag(takes_context=True)
def get_site_root_page(context):
    """this returns a core.Page, not the implementation-specific model used
    so object-comparison to self will return false as objects would differ"""
    return context['request'].site.root_page


@register.simple_tag
def get_field_classes(field):
    classes = [
        'mb-field',
        'mb-field--{}'.format(slugify(field.name)),
    ]

    if field.errors:
        classes.append('mb-field--has-errors')

    return ' '.join(classes)


@register.assignment_tag
def get_page_title_for_navbar(page):
    if page.seo_title:
        return page.seo_title

    return page.title

