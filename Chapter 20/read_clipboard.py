'''
Austin Richards 5/28/21

read_clipboard.py uses pyautogui and pyperclip to select
an open notepad and read the text that it contains. 

This program could be useful in automating text entry to a user,
where one may want to know if there is already text in the
box they are about to enter text into.
'''
import pyautogui
import pyperclip
import logging
logging.basicConfig(level=logging.DEBUG, format='%(asctime)s: %(message)s')


def main():
    # select active notepad
    textbox = pyautogui.getWindowsWithTitle('Notepad')[0]
    logging.debug(textbox.title)
    textbox.activate()
    #TODO check that the window opened correctly

    #TODO use hotkeys method to do ctrl-a, ctrl-c

    #TODO use pyperclip paste method to obtain the text, print it


main()
