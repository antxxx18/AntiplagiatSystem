from GoogleScraper.core import scrape_with_config
from GoogleScraper.scraping import GoogleSearchError
import operator

def to_str(keywords):
    str = ''
    for query in keywords:
        for word in query:
            str+=word+' '
        str+='\n'
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
            'num_pages_for_keyword': 1,
            #'scrape_method': 'selenium',

            #'check_proxies': 'True',
            'scrape_method': 'http',
            'num_workers': 1000,
        },
        'SELENIUM': {
            'sel_browser': 'chrome',
        },
        'GLOBAL': {
            'verbosity': 1,
            'do_caching': 'True',
            #'proxy_file': 'parsegoogle/proxy.txt',
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
        print(str(i) + '.' + str(sorted_x[x]))
        i += 1