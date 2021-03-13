'''
Austin Richards 3/11/21

flickr-download will search flickr
and download the first 10 images
'''
import os, requests, bs4, logging

logging.basicConfig(level=logging.DEBUG, format=' %(asctime)s -  %(levelname)s -  %(message)s')
#logging.disable(logging.CRITICAL)

url = 'https://imgur.com/'
os.chdir('Chapter 12')
os.makedirs('imgur-test', exist_ok=True )

print(f'Downloading {url}...')
page = requests.get(url)
page.raise_for_status()

soup = bs4.BeautifulSoup(page.text, 'lxml')
print(soup.a)