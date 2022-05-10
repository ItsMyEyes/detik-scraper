# -*- coding: utf-8 -*-

#   __
#  /__)  _  _     _   _ _/   _
# / (   (- (/ (/ (- _)  /  _)
#          /

"""
Detik Scrapping
~~~~~~~~~~~~~~~~~~~~~

detik scraping, written in Python, for human beings.
Basic List hot product usage:

   >>> import detik
   >>> r = detik.getListCategory()

The other HTTP methods are supported - see `requests.api`. Full documentation
is at <https://github.com/ItsMyEyes>.

:copyright: (c) 2022 by Kiyora dev.
:license: Apache 2.0, see LICENSE for more details.
"""

from detik.utils import *
from detik.__version__ import *

def version() -> str:
    return __version__

def getListCategory() -> dict:
    return listCategory()

def getListNews(category: str) -> dict:
    return ListNews(category)

def getListHotNews() -> dict:
    return HotNewsList()

def getDetailNews(link: str) -> dict:
    return DetailNews(link)
