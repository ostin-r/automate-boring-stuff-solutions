'''
Austin Richards 5/30/21

hangouts_bot.py opens google hangouts and sends
a notification to a select group of people
'''
import webbrowser
import pyautogui


def main():
    # open google hangouts
    webbrowser.open('https://hangouts.google.com/?authuser=4')

    # check that the correct user is selected
    pyautogui.sleep(3) # wait for page to load
    im = pyautogui.screenshot()
    if im.getpixel((2595, 254)) != (236, 64, 122):
        print('Error: wrong user selected.')
        return

    # press the new message button
    pyautogui.write(['\t'] * 5 + ['enter'])

    #TODO figure out different paths for users


main()
