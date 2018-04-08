#!/usr/bin/env python3
# -*- coding: utf-8 -*- #

from __future__ import unicode_literals
import os


PUBLISH_MODE = os.getenv('PELICAN_PUBLISH', False)

AUTHOR = 'nCoda Contributors'
SITENAME = 'nCoda'
SITE_NAME = SITENAME
CONTACT_EMAIL = 'contact@ncodamusic.org'
SITEURL = os.getenv('URL', '')
RELATIVE_URLS = False
TIMEZONE = 'America/Toronto'
TIME_ZONE = TIMEZONE
DELETE_OUTPUT_DIRECTORY = False  # handled by the Makefile

DEFAULT_LANG = 'en'

PATH = 'content'


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
        'COPYRIGHT_ENTITY': 'nCoda und andere',
        # TODO: translate URLs
    },
    'fr': {
        'LOCALE': 'fr_FR',
        'AUTHORS_SAVE_AS': 'auteurs/index.html',
        'AUTHOR_SAVE_AS': 'auteurs/{slug}/index.html',
        'AUTHOR_URL': 'auteurs/{slug}/',
        'COPYRIGHT_ENTITY': 'nCoda et autres',
    },
    'pt': {
        'LOCALE': 'pt_PT',
        'COPYRIGHT_ENTITY': 'nCoda e outros',
    },
    'zh_cn': {
        'LOCALE': 'zh_CN',
        'COPYRIGHT_ENTITY': 'nCoda&nbsp;与他们',
        # TODO: translate URLs
    },
}

# translations for the theme
LANG_NAMES = {
    'de': 'Deutsch',
    'en': 'English',
    'fr': 'Français',
    'pt': 'Português',
    'zh_cn': '简体中文',
}
TRANS = {
    'Categories': {'en': 'Categories', 'fr': 'Catégories', 'de': 'TODO', 'pt': 'TODO', 'zh_cn': 'TODO'},
    'Menu': {'en': 'Menu', 'fr': 'Menu', 'de': 'TODO', 'pt': 'TODO', 'zh_cn': 'TODO'},
}


# Theme Settings
# --------------
THEME = 'ncoda_theme'
THEMEURL = '{0}/theme'.format(SITEURL)
SHOW_CODA_MENU = True  # make topbar logo a dropdown w links to nCoda sites; false is just link to homepage
URL_PREFIX_TO_ICONS = '{0}/img/icons'.format(THEMEURL)
TWITTER_ACCOUNT = 'ncodamusic'  # do NOT include the '@'
DEFAULT_DESCRIPTION = 'nCoda: Making Music Notation Open, Collaborative, and Scriptable'

# copyright line is "&copy; {{ COPYRIGHT_YEARS }} {{ COPYRIGHT_ENTITY }}"
COPYRIGHT_YEARS = '2018'
COPYRIGHT_ENTITY = 'nCoda and others'  # set this per language in I18N_SUBSITES
