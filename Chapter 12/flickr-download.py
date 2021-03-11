'''
Austin Richards 3/11/21

flickr-download will search flickr
and download the first 10 images
'''
import requests, os, bs4, webbrowser

# make directory for images to save
search_item = 'desert'
os.makedirs('flickr-' + search_item, exist_ok=True )

# get the webbpage
print('Downloading webpage...')
url = 'https://www.flickr.com/search/?text=' + search_item
res = requests.get(url)
res.raise_for_status()

soup = bs4.BeautifulSoup(res.text, 'html.parser')