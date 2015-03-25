# -*- coding: utf-8 -*-

"""
I switched my motto; instead of saying "fuck tomorrow"
That buck that bought a bottle could've struck the lotto.
"""

__author__ = 'Nikolai Tschacher'
__updated__ = '22.01.2015'  # day.month.year
__home__ = 'incolumitas.com'

from GoogleScraper.proxies import Proxy
from GoogleScraper.config import get_config
from GoogleScraper.log import setup_logger

"""
All objects imported here are exposed as the public API of GoogleScraper
"""

from GoogleScraper.core import scrape_with_config
from GoogleScraper.scraping import GoogleSearchError, MaliciousRequestDetected

Config = get_config(parse_command_line=False)
setup_logger()
