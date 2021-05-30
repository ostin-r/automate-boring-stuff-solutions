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
    textboxes = pyautogui.getWindowsWithTitle('Notepad')
    text = [] # list for storing string data in each box

    for textbox in textboxes:
        logging.debug(textbox.title)
        textbox.activate()
        textbox.maximize() # the activate() method alone was unreliable at opening the window

        # check that the window opened correctly- this verifies the notepad icon is in the corner
        while True:
            im = pyautogui.screenshot()
            if im.getpixel((17, 28)) == (156, 209, 220): break

        # use hotkeys method to do ctrl-a, ctrl-c
        pyautogui.moveTo((200, 200))
        pyautogui.click()
        pyautogui.hotkey('ctrl', 'a')
        pyautogui.hotkey('ctrl', 'c')

        # use pyperclip paste method to obtain the text, print it
        text.append(pyperclip.paste())
        print(text)
        

main()
