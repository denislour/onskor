from django.db import models

from wagtail.core.models import Page
from wagtail.admin.edit_handlers import FieldPanel


class HomePage(Page):
    """
        Home page model.
    """

    templates = "home/home.html"

    # Only one home page instance at a time
    max_count = 1

    # Define django fields
    banner_title = models.CharField(max_length=100, blank=False, null=True)

    # Add django fields to content panels in Admin
    content_panels = Page.content_panels + [FieldPanel("banner_title")]

    class Meta:
        verbose_name = "Home Page"
        verbose_name_plural = "Home Pages"
