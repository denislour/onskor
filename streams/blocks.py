from wagtail.core import blocks
from wagtail.images.blocks import ImageChooserBlock


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


class CardBlock(blocks.StructBlock):
    """
    List Block is a block can be `ADD MORE` in one specify block
    For ex in card block when we created in Wagtail:
        - Only one `title` block can be added
        - Multi `card` block can be added 
    """

    title = blocks.CharBlock(required=True, help_text='Single Block title')

    # List Block
    cards = blocks.ListBlock(blocks.StructBlock([
        ('image', ImageChooserBlock(required=True)),
        ('title', blocks.CharBlock(required=True, max_length=40)),
        ('text', blocks.TextBlock(required=True, max_length=200)),
        ('button_page', blocks.PageChooserBlock(required=False)),
        ('button_url', blocks.URLBlock(
            required=False,
            help_text="If button page above is selected, that will be used."
        ))
    ]))

    class Meta:
        template = "streams/card_block.html"
        icon = "placeholder"
        label = "Card Staff"


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
