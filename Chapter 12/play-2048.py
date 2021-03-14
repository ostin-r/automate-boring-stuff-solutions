'''
Austin Richards 3/13/21

play-2048.py navigates to https://play2048.co/ and 
automatically plays the game by simply repeating
up, right, down, left until the game is over
'''
import logging
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.common.exceptions import NoSuchElementException

logging.basicConfig(level=logging.DEBUG, format=' %(asctime)s -  %(levelname)s -  %(message)s')

url = 'https://play2048.co/'
driver = webdriver.Chrome()
driver.get(url)
html_elem = driver.find_element_by_tag_name('html')

while True:
    html_elem.send_keys(Keys.UP)
    html_elem.send_keys(Keys.RIGHT)
    html_elem.send_keys(Keys.DOWN)
    html_elem.send_keys(Keys.LEFT)

    try:
        selector = 'body > div.container > div.game-container > div.game-message.game-over'
        game_over = driver.find_element_by_css_selector(selector)
        break
    except NoSuchElementException:
        pass