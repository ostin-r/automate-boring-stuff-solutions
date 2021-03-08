'''
Another follow-along project in ch. 12 (web scraping)
This project downloads all comics from xkcd.com
'''
import requests, os, bs4

url = 'https://xkcd.com'
os.chdir('follow-along/Chapters 10-20')
os.makedirs('xkcd', exist_ok=True)

i = 0

#while not url.endswith('#'): # original author's code, but didn't want to download this much
while i < 3:
    print(f'downloading page {url}...')
    res = requests.get(url)
    res.raise_for_status()

    soup = bs4.BeautifulSoup(res.text, 'html.parser')
    comic_element = soup.select('#comic > img')

    if comic_element == []:
        print('Could not find comic image.')
    else:
        comic_url = 'https:' + comic_element[0].get('src')
        print(f'Downloading image {comic_url}...')
        res = requests.get(comic_url)
        res.raise_for_status()

        image_file = os.path.join('xkcd', os.path.basename(comic_url))
        
        with open(image_file, 'wb') as file:
            for chunk in res.iter_content(100000):
                file.write(chunk)

    prev_link = soup.select('#middleContainer > ul:nth-child(4) > li:nth-child(2) > a')[0]
    url = 'https://xkcd.com' + prev_link.get('href')
    print(url)
    
    i += 1