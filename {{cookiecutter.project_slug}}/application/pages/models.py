import six
from django.db import models

# Create your models here.
from wagtail.wagtailcore.models import Page, PageBase
from wagtailmetadata.models import MetadataPageMixin


class HomePage(six.with_metaclass(PageBase, MetadataPageMixin, Page)):
    content_panels = Page.content_panels + [
    ]
    promote_panels = Page.promote_panels + MetadataPageMixin.panels
