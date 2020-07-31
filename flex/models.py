from django.db import models
from wagtail.admin.edit_handlers import FieldPanel, StreamFieldPanel
from wagtail.core.models import Page
from wagtail.core.fields import StreamField
from streams import blocks


class FlexPage(Page):
    """
    Flex page model
    """

    template = "flex/flex.html"

    # Django models
    subtitle = models.CharField(max_length=100, null=True, blank=True)

    # Wagtail models
    content = StreamField(
        [
            ("title_and_text", blocks.TitleAndTextBlock()),
            ("full_rich_text", blocks.FullRichTextBlock()),
            ("simple_rich_text", blocks.SimpleRichTextBlock()),
            ("cards_blocks", blocks.CardBlock()),
        ], blank=True, null=True
    )

    # Add the all of fields to Wagtail panels
    content_panels = Page.content_panels + [
        FieldPanel("subtitle"),
        StreamFieldPanel("content"),
    ]

    class Meta:
        verbose_name = "Flex page"
        verbose_name_plural = "Flex pages"
