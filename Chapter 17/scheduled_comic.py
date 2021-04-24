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
log.disable(log.CRITICAL)


def get_all_paths(directory):
    file_paths = []
    for path, dirs, files in os.walk(directory):
        for filename in files:
            filepath = os.path.join(path, filename)
            file_paths.append(filepath)
    return file_paths


def download_new():
    # get the page
    page = 'http://www.lunarbaboon.com'
    res = requests.get(page)
    res.raise_for_status()

    # parse for the first comic, get the title and image link
    soup = bs4.BeautifulSoup(res.text, 'html.parser')
    first_comic = soup.select('div.journal-entry-text > h2 > a')[0]
    comic_title = first_comic.get_text()
    comic_file = comic_title + '.png'

    # check if the comic name is on the desktop already
    # first, get files from the the desktop
    desk_path = os.path.abspath(os.path.join(os.environ['HOMEPATH'], 'OneDrive/Desktop'))
    file_names = [Path(path).stem for path in get_all_paths(desk_path) if path.endswith('.png')]

    # if the file isn't present, download it
    if comic_title not in file_names:
        # get the link
        download_comic = soup.select('div.journal-entry-text > div.body > p:nth-child(1) > span > span > img')[0]
        download_link = page + download_comic['src']

        # get the page
        res = requests.get(download_link)
        res.raise_for_status()

        # download the image
        filepath = os.path.join(desk_path, comic_file)
        with open(filepath, 'wb') as file:
            for chunk in res.iter_content(100000):
                file.write(chunk)
        print('New comic available!')

    else:
        print('No new comic')


download_new()