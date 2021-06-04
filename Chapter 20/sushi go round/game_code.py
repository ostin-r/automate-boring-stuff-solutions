'''
main code for the sushi go round bot
'''
import webbrowser
import pyautogui


def waitForImage(img_name):
    # pauses program until image is identified (for loading webpages)
    while True:
        element = pyautogui.locateOnScreen(img_name)
        if element is not None: return


def startGame():
    # open browser and wait for game to load
    webbrowser.open('https://www.miniclip.com/games/sushi-go-round/en/#')
    waitForImage('miniclip_img.PNG')

    # move the mouse then scroll
    pyautogui.moveTo(x=1000, y=1000) # moved mouse here because args not working for scroll method
    pyautogui.scroll(-410)

def main():
    startGame()

if __name__ == '__main__':
    main()