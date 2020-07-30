from django.db import models
from wagtail.admin.edit_handlers import FieldPanel
from wagtail.core.models import Page


class FlexPage(Page):
    """
    Flex page model
    """

    template = "flex/flex.html"

    # Django model
    subtitle = models.CharField(max_length=100, null=True, blank=True)

    # Wagtail panels
    content_panels = Page.content_panels + [FieldPanel("subtitle")]

    class Meta:
        verbose_name = "Flex page"
        verbose_name_plural = "Flex pages"
