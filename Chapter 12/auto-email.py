'''
Austin Richards 3/9/21

auto-email.py is a basic emailer that sends emails via the selenium python module.
'''
import sys
from selenium import webdriver

# TODO: Open a webbrowser, navigate to the login page
chrome = webdriver.Chrome()
chrome.get('https://gmail.com')

email = sys.argv[1]
email_elem = chrome.find_by_css_selector(#identifierId)
email_elem.send_keys(email)

# TODO: Create + send an email