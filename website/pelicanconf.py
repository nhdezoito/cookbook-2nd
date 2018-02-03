#!/usr/bin/env python
# -*- coding: utf-8 -*- #
from __future__ import unicode_literals

AUTHOR = 'Cyrille Rossant'
SITENAME = 'IPython Cookbook (2018)'
SITEURL = ''
THEME = 'themes/pure'
TWITTER = 'https://twitter.com/cyrillerossant'
GITHUB = 'https://github.com/ipython-books/cookbook-2nd'
CODE = 'https://github.com/ipython-books/cookbook-2nd-code'
AUTHOR_WEBSITE = 'http://cyrille.rossant.net'
MINIBOOK = 'https://github.com/ipython-books/minibook-2nd-code'

PATH = 'content'

TIMEZONE = 'Europe/Paris'

DEFAULT_LANG = 'en'


MENUITEMS = (('home', '/'),
             ('Jupyter notebooks', CODE),
             ('minibook', MINIBOOK),
             ('author', AUTHOR_WEBSITE),
             )

# PAGE_PATHS = ('../',)


# Social widget
SOCIAL = (('twitter', TWITTER),
          ('github', GITHUB),
          )

# Feed generation is usually not desired when developing
FEED_ALL_ATOM = None
CATEGORY_FEED_ATOM = None
TRANSLATION_FEED_ATOM = None
AUTHOR_FEED_ATOM = None
AUTHOR_FEED_RSS = None

DEFAULT_PAGINATION = False

# Uncomment following line if you want document-relative URLs when developing
#RELATIVE_URLS = True