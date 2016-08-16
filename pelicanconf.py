#!/usr/bin/env python
# -*- coding: utf-8 -*- #
from __future__ import unicode_literals

AUTHOR = 'nCoda Contributors'
SITENAME = 'nCoda'
CONTACT_EMAIL = 'contact@ncodamusic.org'
SITEURL = 'http://localhost:8000'  # changed in publishconf.py
RELATIVE_URLS = False

PATH = 'content'

TIMEZONE = 'America/Toronto'

DEFAULT_LANG = 'en'

# turn off feed generation
FEED_ALL_ATOM = None
CATEGORY_FEED_ATOM = None
TRANSLATION_FEED_ATOM = None
AUTHOR_FEED_ATOM = None
AUTHOR_FEED_RSS = None

LINKS = (('Pelican', 'http://getpelican.com/'),
         ('Python.org', 'http://python.org/'),
         ('Jinja2', 'http://jinja.pocoo.org/'),
         ('this is LINKS in pelicanconf.py', '#'),)

SOCIAL = (('this is SOCIAL in pelicanconf.py', '#'),
          ('Another social link', '#'),)

DEFAULT_PAGINATION = 10

# this preserves a git repository in the "output" directory
DELETE_OUTPUT_DIRECTORY = False
OUTPUT_RETENTION = ('.git', 'README.md')

PLUGIN_PATHS = ['pelican-plugins']
PLUGINS = [
    # 'cjk-auto-spacing',  # TODO: see if we can get this to work; not vital
    'i18n_subsites',
    'sitemap',
]

SITEMAP = {
    'format': 'xml',
}

DISPLAY_CATEGORIES_ON_MENU = False
DISPLAY_PAGES_ON_MENU = False


# These settings determine the pathname used to generate, and the URLs used to point to, the
# different kinds of pages. These can be translated in the I18N_SUBSITES dictionary.
ARTICLE_SAVE_AS = '{date:%Y}/{date:%m}/{slug}/index.html'
ARTICLE_URL = '{date:%Y}/{date:%m}/{slug}/'
PAGE_SAVE_AS = '{slug}/index.html'
PAGE_URL = '{slug}/'
YEAR_ARCHIVE_SAVE_AS = '{date:%Y}/index.html'
MONTH_ARCHIVE_SAVE_AS = '{date:%Y}/{date:%m}/index.html'
CATEGORIES_SAVE_AS = 'categories/index.html'
CATEGORY_SAVE_AS = 'categories/{slug}/index.html'
CATEGORY_URL = 'categories/{slug}/'
TAGS_SAVE_AS = 'tags/index.html'
TAG_SAVE_AS = 'tags/{slug}/index.html'
TAG_URL = 'tags/{slug}/'
AUTHORS_SAVE_AS = 'authors/index.html'
AUTHOR_SAVE_AS = 'authors/{slug}/index.html'
AUTHOR_URL = 'authors/{slug}/'


# l10n/i18n settings
# ------------------
# mapping: language_code -> settings_overrides_dict
LOCALE = 'en_US'
# by default, untranslated pages are still outputted
I18N_UNTRANSLATED_ARTICLES = 'keep'
I18N_UNTRANSLATED_PAGES = 'keep'
# locale-specific overrides
I18N_SUBSITES = {
    'de': {
        'LOCALE': 'de_DE',
        # TODO: translate URLs
    },
    'fr': {
        'LOCALE': 'fr_FR',
        'AUTHORS_SAVE_AS': 'auteurs/index.html',
        'AUTHOR_SAVE_AS': 'auteurs/{slug}/index.html',
        'AUTHOR_URL': 'auteurs/{slug}/',
    },
    'zh_cn': {
        'LOCALE': 'zh_CN',
        # TODO: translate URLs
    },
}

# translations for the theme
LANG_NAMES = {
    'de': 'Deutsch',
    'en': 'English',
    'fr': 'Français',
    'zh_cn': '简体中文',
}
TRANS = {
    'Categories': {'en': 'Categories', 'fr': 'Catégories', 'de': 'TODO', 'zh_cn': 'TODO'},
    'Menu': {'en': 'Menu', 'fr': 'Menu', 'de': 'TODO', 'zh_cn': 'TODO'},
}


# Theme Settings
# --------------
THEME = 'ncoda_theme'
COPYRIGHT_YEARS = '2016'
THEMEURL = '{0}/theme'.format(SITEURL)
