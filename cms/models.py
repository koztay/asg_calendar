from django.db import models
from django.utils import timezone
from wagtail.wagtailcore.models import Page
from wagtail.wagtailcore.fields import RichTextField
from wagtail.wagtailadmin.edit_handlers import FieldPanel
from wagtail.wagtailimages.edit_handlers import ImageChooserPanel


class HomePage(Page):
    body = RichTextField(blank=True)

    content_panels = Page.content_panels + [
        FieldPanel('body', classname="full")
    ]


class EventPage(Page):
    description = RichTextField(blank=True)
    poster = models.ForeignKey(
        'wagtailimages.Image',
        null=True,
        blank=True,
        on_delete=models.SET_NULL,
        related_name='+'
    )
    datetime = models.DateTimeField(default=timezone.now)
    link = models.URLField(blank=True)
    is_open = models.BooleanField(default=True)

    content_panels = Page.content_panels + [
        FieldPanel('description'),
        ImageChooserPanel('poster'),
        FieldPanel('datetime'),
        FieldPanel('link'),
        FieldPanel('is_open'),
    ]
