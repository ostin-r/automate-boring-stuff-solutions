'''
Austin Richards 3/11/21

flickr-download will search flickr
and download the first 10 images
'''
import os, requests, bs4, re
import logging as log
from contextlib import suppress

log.basicConfig(level=log.DEBUG, format='%(asctime)s: %(message)s')

search_term = 'canyon'
url = 'https://unsplash.com/s/photos/' + search_term
os.chdir('Chapter 12')
os.makedirs('unsplash-' + search_term, exist_ok=True)

res = requests.get(url)
res.raise_for_status()
soup = bs4.BeautifulSoup(res.text, 'html.parser')
links = soup.select('img')

for link in links:
    with suppress(KeyError):
        log.debug( '\nDownloading image link: ' + link['srcset'] + '\n' )

# TODO: Make a regex object that can sort through these massive links
# TODO: maybe they can be indexed but I couldn't figure it out