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
# x_pad and y_pad are the top corner of the game play area
# these can easily be changed if the computer the bot is being
# run on is of a different resolution.
# --------------


def waitForImage(img_name):
    # pauses program until image is identified (good for loading webpages)
    while True:
        element = pyautogui.locateOnScreen(img_name)
        if element is not None: return


def waitForPixel(pixel):
    # pauses program until correct pixel is identified in play area
    # pixel = [x, y, (R, G, B)]
    pixel[0] += x_pad
    pixel[1] += y_pad
    while True:
        im = pyautogui.screenshot()
        if im.getpixel((pixel[0], pixel[1])) == pixel[2]: break


def mousePos(cords):
    # moves the mouse within the game play area
    pyautogui.moveTo(x_pad + cords[0], y_pad + cords[1])


def gamePixel():
    '''
    returns the color and relative game position of the cursor
    '''
    x, y = pyautogui.position()
    im = pyautogui.screenshot()
    color = im.getpixel((x, y))

    x = x - x_pad
    y = y - y_pad
    return [x, y, color]


def startGame():
    # move the mouse then scroll
    webbrowser.open('https://www.miniclip.com/games/sushi-go-round/en/#')
    waitForImage('miniclip_menu.PNG')
    pyautogui.moveTo(x=1000, y=1000) # moved mouse here because args not working for scroll method
    pyautogui.scroll(-410)

    # press big play button
    # [709, 360, (253, 136, 58)]

    # press little play button
    # [779, 412, (75, 205, 245)]

    # press the continue button
    # [743, 776, (255, 45, 236)]

    # press the skip button (skip tutorial)
    # [1160, 902, (255, 203, 46)]

    # press continue button again
    # [629, 748, (255, 179, 246)]


def main():
    startGame()

if __name__ == '__main__':
    main()