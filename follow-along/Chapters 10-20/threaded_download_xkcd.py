'''
Follow-along project from ch. 17 of ATBS.

A multi-threaded version of the xkcd downloader
from chapter 12 follow-along
'''
import time
import threading
import requests, os, bs4
import logging as log

log.basicConfig(level=log.DEBUG, format='%(asctime)s: %(message)s')
log.disable(log.CRITICAL)


def download_comics(start_comic, end_comic):
    for url_num in range(start_comic, end_comic):
        print(f'Downloading page https://xkcd.com/{url_num}...')
        res = requests.get(f'https://xkcd.com/{url_num}')
        res.raise_for_status()

        soup = bs4.BeautifulSoup(res.text, 'html.parser')

        comic_elem = soup.select('#comic img')
        if comic_elem == []:
            print('could not find image.')
            continue
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

start_time = time.time()

# create and start the thread objects
download_threads = []
for i in range(2411, 2451, 10):
    start = i
    end = i + 9
    if start == 0: start = 1
    download_thread = threading.Thread(target=download_comics, args=(start, end))
    download_threads.append(download_thread)
    download_thread.start()
    log.debug(i)
log.debug(download_threads)

for download_thread in download_threads:
    download_thread.join()

end_time = time.time()
print(f'Done in {end_time - start_time} seconds')
# takes about 14 seconds