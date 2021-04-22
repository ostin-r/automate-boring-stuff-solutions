'''
Austin Richards 4/22/21

scheduled_comic.py is a program that downloads new comics
posted on common web comic sites.  It is meant to be used
with the operating system's scheduler to be run periodically.
'''
import os, requests, bs4

def download_new(page):

    #TODO get the latest webpage (homepage)

    #TODO parse the html for comic or image

    #TODO figure out how to detect a new comic here...

    pass

download_new('https://xkcd.com')