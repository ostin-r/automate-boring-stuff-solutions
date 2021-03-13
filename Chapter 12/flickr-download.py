'''
Austin Richards 3/11/21

flickr-download will search flickr
and download the first 10 images
'''
import os, requests, bs4, logging
from selenium import webdriver

logging.basicConfig(level=logging.DEBUG, format=' %(asctime)s -  %(levelname)s -  %(message)s')
logging.disable(logging.CRITICAL)

# search flickr, make a directory for the images
search_item = 'mountains'
url = f'https://www.flickr.com/search/?text={search_item}' 
os.chdir('Chapter 12')
os.makedirs(f'flickr-{search_item}', exist_ok=True )

# open chrome, find the image
chrome = webdriver.Chrome()
chrome.get(url)
elems = chrome.find_element_by_class_name('overlay')

# click the image
try:
    print(elems)
    elems.click()
    url = chrome.current_url
except:
    print('Image not found')