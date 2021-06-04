'''
start_browser.py opens the sushi go round page
and scrolls to a specific point.  This helps to 
make the play area coordinates uniform throughout
the program.
'''
import webbrowser
import pyautogui

def waitForImage(img_name):
    '''
    waitForImage will pause the program until the 
    passed image file appears on the screen
    '''
    while True:
        element = pyautogui.locateOnScreen(img_name)
        if element is not None: return

def openGame():
    webbrowser.open('https://www.miniclip.com/games/sushi-go-round/en/#')
    pyautogui.sleep(5)
    pyautogui.scroll(300, x=1000, y=1000) #TODO figure out how to get this to work

def main():
    openGame()

if __name__ == '__main__':
    main()