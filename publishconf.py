#!/usr/bin/env python
# -*- coding: utf-8 -*- #
from __future__ import unicode_literals

# This file is only used if you use `make publish` or
# explicitly specify it as your config file.

import os
import sys
sys.path.append(os.curdir)
from pelicanconf import *

SITEURL = 'https://ncodamusic.org'
# as the SITEURL changes, we have to update these too!
THEMEURL = '{0}/theme'.format(SITEURL)
URL_PREFIX_TO_ICONS = '{0}/img/icons'.format(THEMEURL)

DELETE_OUTPUT_DIRECTORY = True
