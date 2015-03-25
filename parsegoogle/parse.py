from GoogleScraper import scrape_with_config, GoogleSearchError
from GoogleScraper.utils import get_some_words
from datetime import datetime
startTime = datetime.now()


keywords = get_some_words(4)
with open('keywords.txt', 'wt') as f:
    for word in keywords:
        f.write(word + '\n')

config = {
    'SCRAPING': {
        'use_own_ip': 'False',
        'keyword_file': 'keywords.txt',
        'search_engines': 'google',
        'num_pages_for_keyword': 1,
        #'scrape_method': 'selenium',

        #'check_proxies': 'True',
        'scrape_method': 'http',
        'num_workers': 1,
    },
    'SELENIUM': {
        'sel_browser': 'chrome',
    },
    'GLOBAL': {
        'verbosity': 2,
        'do_caching': 'False',
        'proxy_file': 'proxy.txt',
    },
    'OUTPUT': {
        'output_filename': 'out.csv',
    },
}

try:
    search = scrape_with_config(config)
except GoogleSearchError as e:
    print(e)


for serp in search.serps:
    print(serp)
    for link in serp.links:
        print(link)

print(datetime.now() - startTime)