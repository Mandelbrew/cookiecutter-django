"""
http://docs.wagtail.io/en/latest/reference/hooks.html#editor-interface`
"""
from django.contrib.staticfiles.templatetags.staticfiles import static
from django.utils.html import format_html, format_html_join
from django.conf import settings
from wagtail.wagtailcore import hooks
from wagtail.wagtailcore.whitelist import attribute_rule, check_url, allow_without_attributes


@hooks.register('construct_whitelister_element_rules')
def whitelister_element_rules():
    return {
        'sup': allow_without_attributes,
        'sub': allow_without_attributes,
        'strong': allow_without_attributes,
        'small': allow_without_attributes,
    }


@hooks.register('insert_editor_js')
def editor_js():
    html = ''
    html += format_html('<script src="{}"></script>', static('core/js/hallo_superscript_plugin.js'))
    html += format_html('<script src="{}"></script>', static('core/js/hallo_subscript_plugin.js'))
    html += format_html('<script src="{}"></script>', static('core/js/hallo_strong_plugin.js'))
    html += format_html('<script src="{}"></script>', static('core/js/hallo_small_plugin.js'))
    html += format_html('<script src="{}"></script>', static('core/js/wagtail-page-editor.js'))

    return html


@hooks.register('insert_editor_css')
def editor_css():
    html = ''
    return html
