'''
Austin Richards 3/9/21

auto-email.py is a basic emailer that sends emails via the selenium python module.
'''
import sys
from selenium import webdriver

chrome = webdriver.Chrome()
chrome.get('https://accounts.google.com/signin')

password = sys.argv[1]
send_address = sys.argv[2]
send_string = ''.join(sys.argv[3:])

user_elem = chrome.find_element_by_id('identifierId')

chrome.quit()