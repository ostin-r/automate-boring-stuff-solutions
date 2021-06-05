'''
main code for the sushi go round bot
'''
import webbrowser
import pyautogui
import logging as log

log.basicConfig(level=log.DEBUG, format='%(asctime)s: %(message)s')

# globals ------
x_pad = 227
y_pad = 599
# --------------


def waitForImage(img_name):
    # pauses program until image is identified (for loading webpages)
    while True:
        element = pyautogui.locateOnScreen(img_name)
        if element is not None: return

def waitForPixel(pos, color):
    # pauses program until pixel is identified
    # position & color are both tuples of len 2 and 3 respectively
    while True:
        im = pyautogui.screenshot()
        if im.getpixel(pos) == color: break

def mousePos(cords):
    # moves the mouse within the game play area
    pyautogui.moveTo(x_pad + cords[0], y_pad + cords[1])

def getCords():
    x,y = pyautogui.position()
    x = x - x_pad
    y = y - y_pad
    return [x, y]

def startGame():
    # open browser, wait for page to load
    webbrowser.open('https://www.miniclip.com/games/sushi-go-round/en/#')
    waitForImage('miniclip_img.PNG')

    # move the mouse then scroll
    pyautogui.moveTo(x=1000, y=1000) # moved mouse here because args not working for scroll method
    pyautogui.scroll(-410)

    # click big play button
    waitForPixel((929,940), (253,140,58))
    pyautogui.click()
    log.debug('click: big play button')

    # click play button
    waitForPixel((1226,756), (111,254,101))
    pyautogui.sleep(0.5)
    pyautogui.click()
    log.debug('click: play button')

    # click both continue buttons
    waitForPixel((887,1392), (255,179,246))
    pyautogui.click(x=887, y=1392)
    pyautogui.click()
    log.debug('click: continue buttons')

def main():
    startGame()

if __name__ == '__main__':
    main()