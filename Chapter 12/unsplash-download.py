'''
Austin Richards 3/11/21

flickr-download will search flickr
and download the first 10 images
'''
import os, requests, bs4, webbrowser
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

'''
i = 0
for link in links:
    while i < 3:
        with suppress(KeyError):
            print(link['srcset'][0])
            i += 1
'''