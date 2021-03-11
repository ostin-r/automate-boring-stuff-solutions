'''
Austin Richards 3/11/21

flickr-download will search flickr
and download the first 10 images
'''
import requests, os, bs4

search_item = 'mountains'
url = 'https://www.flickr.com/'
os.makedirs('flickr-' + search_item, exist_ok=True )

# TODO: Download the home page, find the search bar and use send_keys to search the the item
res = requests.get(url)
res.raise_for_status()

# TODO: Click the first image link

# TODO: Download the image, then click next

# TODO: once this works, put it in a loop and do it the desired amount of times