from wagtail.core import blocks


class TitleAndTextBlock(blocks.StructBlock):
    """
    Title and text block
    """

    title = blocks.CharBlock(required=True, help_text="Add your title")
    text = blocks.TextBlock(required=True, help_text="Add your text")

    class Meta:
        template = "streams/title_and_text_block.html"
        icon = "edit"
        label = "Title & Text"


class FullRichTextBlock(blocks.RichTextBlock):
    """
    Rich text block with full features.
    """

    class Meta:
        template = "streams/rich_text_block.html"
        icon = "doc-full"
        label = "Full Rich Text"


class SimpleRichTextBlock(blocks.RichTextBlock):
    """
    Rich text block with limit features.
    """

    def __init__(
            self, required=True, help_text=None, editor='default',
            features=None, validators=(), **kwargs):
        """
        Override the features of Rich Text Block
        """

        super().__init__(**kwargs)
        self.features = ['bold', 'italic', 'link']

    class Meta:
        template = "streams/rich_text_block.html"
        icon = "edit"
        label = "Simple Rich Text"
