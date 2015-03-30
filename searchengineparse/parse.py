# -*- coding:utf-8 -*-
from googlescraper.core import scrape_with_config
from googlescraper.scraping import GoogleSearchError
#from proxyparse import proxy
import operator

num_queries = 8

# FIX ME PLEASE
def to_str(keywords):
    str = ''
    i = num_queries
    for query in keywords:
        if i == num_queries:
            i = 0
            for word in query:
                str+=word+' '
            str+='\n'
        i += 1
    return str

def parse(keywords):

    str=to_str(keywords)
    # Make config fo scraping
    # FIX threads number
    config = {
        'SCRAPING': {
            'num_results_per_page': 10,
            'use_own_ip': 'True',
            'keywords': str,
            #'keyword_file': 'keywords.txt',
            'search_engines': 'bing',
            #'search_engines': 'google',
            'num_pages_for_keyword': 1,
            #'scrape_method': 'selenium',

            #'check_proxies': 'False',
            'scrape_method': 'http',
            'num_workers': 100,
        },
        'SELENIUM': {
            'sel_browser': 'phantomjs',
        },
        'GLOBAL': {
            'verbosity': 1,
            'do_caching': 'False',
            #'proxy_file': 'searchengineparse/proxy.txt',
        },
        'OUTPUT': {
            'output_filename': 'out.json',
        },
    }

    try:
        search = scrape_with_config(config)
    except GoogleSearchError as e:
        print(e)


    # And FIX this
    x = {}
    for serp in search.serps:
        for link in serp.links:
            if link.link in x:
                x[link.link] += 1
            else:
                x.update({link.link: 1})

    print(len(x))
    sorted_x = sorted(x.items(), key=operator.itemgetter(1), reverse=True)
    i = 1
    for x in range(0, 5):
        print("%d. %s"%(i,sorted_x[x]))
        i += 1

    # Mayde fix problem with search results
    config = {
        'SCRAPING': {
            'num_results_per_page': 1,
            'use_own_ip': 'True',
            'keywords': 'NONE',
            'search_engines': 'bing',
            'num_pages_for_keyword': 1,
            'scrape_method': 'selenium',
            'num_workers': 1,
        },
        'SELENIUM': {
            'sel_browser': 'phantomjs',
        },
        'GLOBAL': {
            'verbosity': 0,
            'do_caching': 'False',
        },
    }

    try:
        search = scrape_with_config(config)
    except GoogleSearchError as e:
        print(e)

    return