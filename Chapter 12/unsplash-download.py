'''
Austin Richards 3/11/21

unsplash-download will search unsplash.com, an
image sharing website and download the first 3 images
'''
import os, requests, bs4
import logging as log
from contextlib import suppress

log.basicConfig(level=log.DEBUG, format='%(asctime)s: %(message)s')
log.disable(log.CRITICAL)

search_term = 'canyon'
url = 'https://unsplash.com/s/photos/' + search_term
new_directory = 'unsplash-' + search_term

os.chdir('Chapter 12')
os.makedirs(new_directory, exist_ok=True)

res = requests.get(url)
res.raise_for_status()
soup = bs4.BeautifulSoup(res.text, 'html.parser')
links = soup.select('img')

i = 1
for link in links[0:4]:
    with suppress(KeyError):

        if link['src'].startswith('https://images'):
            log.debug('downloading... ' + link['src'][:70])
            res = requests.get(link['src'])
            res.raise_for_status()

            filename = 'image-' + str(i) + '.jpg'
            filepath = os.path.join(new_directory, filename)
            log.debug(filepath)

            with open(filepath, 'wb') as file:
                for chunk in res.iter_content(100000):
                    file.write(chunk)
            
            print('successfully downloaded image ' + str(i))
            i += 1