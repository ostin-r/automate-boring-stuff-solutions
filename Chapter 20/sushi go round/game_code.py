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


class Cord:
    f_shrimp = (56, 654)
    f_rice = (164, 653)
    f_nori = (48, 757)
    f_roe = (165, 760)
    f_salmon = (58, 868)
    f_unagi = (167, 866)

    plates = [(180, 413),
        (381, 419),
        (592, 412),
        (786, 415),
        (984, 416),
        (1186, 416)]

'''
plate cords:
[180, 413, (238, 219, 169)]
[381, 419, (238, 219, 169)]
[592, 412, (238, 219, 169)]
[786, 415, (238, 219, 169)]
[984, 416, (238, 219, 169)]
[1186, 416, (238, 219, 169)]
'''

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
    waitForPixel([709, 360, (253, 136, 58)])
    pyautogui.click()

    # press little play button
    waitForPixel([779, 412, (75, 205, 245)])
    pyautogui.click()

    # press the continue button
    waitForPixel([743, 776, (255, 45, 236)])
    mousePos((743, 776))
    pyautogui.click()

    # press the skip button (skip tutorial)
    waitForPixel([1160, 902, (255, 203, 46)])
    mousePos((1160, 902))
    pyautogui.click()

    # press continue button again
    waitForPixel([629, 748, (255, 179, 246)])
    mousePos((629, 748))
    pyautogui.click()


def clearTables():
    pass

def main():
    startGame()

if __name__ == '__main__':
    main()