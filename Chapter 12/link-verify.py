'''
Austin Richards 3/14/21
'''
import requests, bs4
import logging as log

log.basicConfig(level=log.DEBUG, format='%(asctime)s: %(message)s')
log.disable(log.CRITICAL)


def verify_links(url):
    '''
    checks that all links on a page are valid by downloading
    them with the requests module.  Returns True if all sites
    are valid.
    '''
    try:
        res = requests.get(url)
        res.raise_for_status()
        soup = bs4.BeautifulSoup(res.text, 'html.parser')
        links = soup.select('a')

        for link in links:
            new_url = link['href']

            if new_url.startswith('/'):
                new_url = url + new_url[1:]
                new_res = requests.get(new_url)
                new_res.raise_for_status()

            elif new_url.startswith('https://'):
                new_res = requests.get(new_url)
                new_res.raise_for_status()

    except Exception as e:
        print(e)
        return False

    return True

url = 'https://www.google.com/'
results = verify_links(url)
print(results) #True