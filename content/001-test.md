Title: My First (Test) Article Using Pelican
Date: 2019-09-19
Modified: 2019-09-19
Category: Testing
Tags: Testies
Slug: test-this
Author: Tobias Reaper
Summary: Here's a brief summary of my test - it's a test.

## here's a header

Here's some body content of the article.

Here's some more content—regular paragraph content.

### Here's a Code Snippet Test

    #!python
    from django.db import models

    from wagtail.core.models import Page
    from wagtail.core.fields import RichTextField
    from wagtail.admin.edit_handlers import FieldPanel


    class HomePage(Page):
        body = RichTextField(blank=True)

        content_panels = Page.content_panels + [FieldPanel("body", classname="full")]

Now time for some `inline_code = snip(pets)`.

How about [an external link?](https://docs.getpelican.com/en/stable/content.html)

### Visuals Are Good®

Here's an image test. First with a `.png` file.

![tobias fyi logo]({static}/images/19-09-tobias-fyi-logo.png)

Here's with the `{attach}` syntax:

![tobias fyi logo]({attach}/images/19-09-tobias-fyi-logo.png)

And now with an svg.

![tobias fyi logo - now in svg!]({static}/images/19-09-tobias-fyi-logo.svg)

## Some Other Pages

Testing out some [internal linkages]({filename}/pages/about.md).
