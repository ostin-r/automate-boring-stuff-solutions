'''
Follow along project in ch.12 of ATBS to practice
interacting with the webbrowser with programs
'''
import requests, sys, webbrowser, bs4

print('Searching...')

search_term = ''.join(sys.argv[1:])
res = requests.get(f'https://pypi.org/search/?q={search_term}&o=')
res.raise_for_status()

soup = bs4.BeautifulSoup(res.text, 'html.parser')
link_elem = soup.select('.package-snippet')

open_tabs = min(5, len(link_elem))
for i in range(open_tabs):
    url = 'https://pypi.org' + link_elem[i].get('href')
    print(f'opening {url}')
    webbrowser.open(url)