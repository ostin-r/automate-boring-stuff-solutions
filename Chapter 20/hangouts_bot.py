'''
Austin Richards 5/30/21

hangouts_bot.py opens google hangouts and sends
a notification to a select group of people
'''
import webbrowser
import pyautogui
import friends


def main():
    # open google hangouts
    webbrowser.open('https://hangouts.google.com/')

    # press the new message button, groups button, then enter names
    # 1245,1011 255,255,255 #FFFFFF
    pyautogui.sleep(5)
    pyautogui.click(x=1245, y=1011)
    pyautogui.press(['tab', 'enter'])

    # create a group of friends - this will only work if friends have google accounts
    # TODO: figure out how to correctly enter names here- seems there is an error occuring
    for name in friends.names:
        pyautogui.write(name)
    pyautogui.press('enter')


main()
