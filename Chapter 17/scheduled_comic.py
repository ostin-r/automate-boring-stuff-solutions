'''
Austin Richards 4/22/21

scheduled_comic.py is a program that downloads new comics
posted on common web comic sites.  It is meant to be used
with the operating system's scheduler to be run periodically.
'''
import os, requests, bs4
from pathlib import Path
import logging as log
log.basicConfig(level=log.DEBUG, format='%(asctime)s: %(message)s')


def get_all_paths(directory):
    file_paths = []
    for path, dirs, files in os.walk(directory):
        for filename in files:
            filepath = os.path.join(path, filename)
            file_paths.append(filepath)
    return file_paths


def download_new(page):
    # get the page
    res = requests.get(page)
    res.raise_for_status()

    # parse for the first comic, get the title
    soup = bs4.BeautifulSoup(res.text, 'html.parser')
    first_comic = soup.select('div.journal-entry-text > h2 > a')[0]
    comic_title = first_comic.get_text()

    #TODO check if the comic name is on the desktop already
    desk_path = os.path.abspath(os.path.join(os.environ['HOMEPATH'], 'OneDrive/Desktop'))
    file_names = [Path(path).stem for path in get_all_paths(desk_path) if path.endswith('.png')]

    if comic_title not in file_names:
        #TODO save the file!
        pass

download_new('http://www.lunarbaboon.com/')