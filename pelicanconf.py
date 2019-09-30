#!/Users/Tobias/.vega/tobias-fyi/bin python

# #!/usr/bin/env python
# -*- coding: utf-8 -*- #
from __future__ import unicode_literals

AUTHOR = "Tobias Reaper"
SITENAME = "tobias.fyi"
SITEURL = ""

PATH = "content"

TIMEZONE = "America/Denver"

DEFAULT_LANG = "en"

# Theme settings
THEME = "medius"

MEDIUS_AUTHORS = {
    "Tobias Reaper": {
        "description": "Data Science Student",
        "cover": "https://avatars1.githubusercontent.com/u/45893143?s=460&v=4",
        "image": "https://avatars1.githubusercontent.com/u/45893143?s=460&v=4",
        "links": [("github", "https://github.com/tobias-fyi"), ("twitter", "https://twitter.com/tobiasfyi")],
    }
}

MEDIUS_CATEGORIES = {
    "Sci-Fi IRL": {
        "description": "A series of data-driven essays exploring the relationship between science-fiction and IRL (in real life) science, technology, and philosophy.",
        "logo": "images/space-silhouette.jpg",
        "thumbnail": "images/space-silhouette.jpg",
    }
}

# Feed generation is usually not desired when developing
FEED_ALL_ATOM = None
CATEGORY_FEED_ATOM = None
TRANSLATION_FEED_ATOM = None
AUTHOR_FEED_ATOM = None
AUTHOR_FEED_RSS = None

# Blogroll
LINKS = (("GitHub", "https://github.com/tobias-fyi"),)

# Social widget
SOCIAL = ("Twitter", "https://twitter.com/tobiasfyi")

DEFAULT_PAGINATION = 5

# DEFAULT_METADATA = {
#     "status": "draft",
# }

# Uncomment following line if you want document-relative URLs when developing
# RELATIVE_URLS = True

