# -*- coding: utf-8 -*-

"""
I switched my motto; instead of saying "fuck tomorrow"
That buck that bought a bottle could've struck the lotto.
"""

__author__ = 'Nikolai Tschacher'
__updated__ = '22.01.2015'  # day.month.year
__home__ = 'incolumitas.com'

from googlescraper.proxies import Proxy
from googlescraper.config import get_config
from googlescraper.log import setup_logger

"""
All objects imported here are exposed as the public API of googlescraper
"""

from googlescraper.core import scrape_with_config
from googlescraper.scraping import GoogleSearchError, MaliciousRequestDetected

Config = get_config(parse_command_line=False)
setup_logger()
