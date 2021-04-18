'''
Follow-along project from ch. 17 of ATBS.

A multi-threaded version of the xkcd downloader
from chapter 12 follow-along
'''
import requests, os, bs4
import logging as log

log.basicConfig(level=log.DEBUG, format='%(asctime)s: %(message)s')


def download_comic(start_comic, end_comic):
    for url_num in range(start_comic, end_comic):
        print(f'Downloading page https://xkcd.com/{url_num}...')
        res = requests.get(f'https://xkcd.com/{url_num}')
        res.raise_for_status()

        soup = bs4.BeautifulSoup(res.text, 'html.parser')

        comic_elem = soup.select('#comic img')
        if comic_elem == []:
            print('could not find image.')
            return
        else:
            comic_url = 'https:' + comic_elem[0].get('src')
            res = requests.get(comic_url)
            res.raise_for_status()

        file_name = os.path.join('xkcd_threaded', os.path.basename(comic_url))
        with open(file_name, 'wb') as image_file:
            for chunk in res.iter_content(100000):
                image_file.write(chunk)


os.chdir('follow-along/Chapters 10-20')
os.makedirs('xkcd_threaded', exist_ok=True)
download_comic(1000, 1001)