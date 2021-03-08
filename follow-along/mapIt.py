'''
mapIt.py is a follow along project on web scraping in chapter 11 of ATBS
'''
import webbrowser, sys, pyperclip

if len(sys.argv) > 1:
    address = ' '.join(sys.argv[1:])

else:
    address = pyperclip.paste()

webbrowser.open('https://www.google.com/maps/place/' + address)