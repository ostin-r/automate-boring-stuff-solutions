'''
Austin Richards 5/30/21

hangouts_bot.py opens google hangouts and sends
a notification to a select group of people
'''
import webbrowser
import pyautogui
import friends
import os


def waitForImage(img_name):
    '''
    waitForImage will pause the program until the 
    passed image file appears on the screen
    '''
    while True:
        element = pyautogui.locateOnScreen(img_name)
        if element is not None: return


def main():
    # open google hangouts, initialize pyautogui
    webbrowser.open('https://hangouts.google.com/?authuser=4')
    pyautogui.PAUSE = 0.5

    # wait until page is loaded, select new message, then new group
    waitForImage('convo_button.PNG')
    pyautogui.click(x=1245, y=1011)
    pyautogui.press(['tab', 'enter'])

    # create a group of friends - this will only work if friends have google accounts
    for name in friends.names:
        pyautogui.write(name)
        pyautogui.sleep(5)
        pyautogui.press('enter')
    pyautogui.press('enter')

    # wait for conversation box to open, then send message!
    waitForImage('message_box.PNG')
    msg = 'Hello everyone!'
    pyautogui.write(msg)
    pyautogui.press('enter')


main()
