"""
main code for the sushi go round bot
"""
import os
import time
import webbrowser
import pyautogui
from PIL import ImageGrab
from PIL import ImageOps
from numpy import *
from contextlib import suppress
import logging as log

log.basicConfig(level=log.DEBUG, format="%(asctime)s: %(message)s")

# globals -----------------------------------------------------
x_pad = 39
y_pad = 618
ORDER_WIDTH = 123
ORDER_HEIGHT = 29

# dictionary to track food stock
foodStock = {"shrimp": 5, "rice": 10, "nori": 10, "roe": 10, "salmon": 5, "unagi": 5}

# summed grayscale IDs for sushi types
sushiTypes = {4411: "gunkan maki", 4405: "onigiri", 5050: "california roll"}

# list for storing if a customer is present & eating
isEating = [False, False, False, False, False, False]

# list for storing how long a customer is eating for
eatingTime = [time.time()] * 6
# --------------------------------------------------------------


class Blank:
    """
    summed grayscale ids for blank "thought bubbles" and blank
    seats
    """
    orders = [10477, 8315, 13310, 12542, 8931, 11823]

    seat = 2745


class Cords:
    # food coordinates
    f_shrimp = (56, 654)
    f_rice = (164, 653)
    f_nori = (48, 757)
    f_roe = (165, 760)
    f_salmon = (58, 868)
    f_unagi = (167, 866)

    # where to click when done with recipe
    roll = (326, 694)

    # where to click to clear all plates
    plates = [(180, 413), (381, 419), (592, 412), (786, 415), (984, 416), (1186, 416)]

    # phone menu options
    phone = (1127, 692)
    toppings = (1083, 544)
    menu_rice = (1085, 584)
    buy_rice = (1093, 560)
    cancel_rice = (1162, 659)
    cancel_topping = (1196, 667)
    back = (1119, 662)
    order = (1000, 583)
    express = (1172, 590)

    # toppings coordinates
    t_shrimp = (985, 440)
    t_unagi = (1140, 444)
    t_nori = (995, 550)
    t_roe = (1154, 551)
    t_salmon = (992, 671)

    # inactive buttons colors for checking availablity
    i_rice = [1093, 560, (127, 127, 127)]
    i_shrimp = [990, 444, (127, 71, 47)]
    i_unagi = [1161, 439, (94, 49, 8)]
    i_nori = [1040, 533, (109, 123, 127)]
    i_roe = [1152, 555, (101, 13, 13)]
    i_salmon = [979, 665, (127, 71, 47)]


def screenGrab():
    """
    returns an image of the play area
    """
    box = (x_pad + 1, y_pad + 1, x_pad + 1280, y_pad + 960)
    im = ImageGrab.grab(box)
    return im


def sushiGrab():
    """
    captures part of the game screen, grayscales it,
    then sums every value to get a unique value for
    different parts of the game
    """
    box = (x_pad + 1, y_pad + 1, x_pad + 1280, y_pad + 960)
    im = ImageOps.grayscale(ImageGrab.grab(box))
    a = array(im.getcolors())
    a = a.sum()
    return a


def get_order_one():
    x = 52 + x_pad
    y = 122 + y_pad
    box = (x, y, x + ORDER_WIDTH, y + ORDER_HEIGHT)
    im = ImageOps.grayscale(ImageGrab.grab(box))
    a = array(im.getcolors())
    a = a.sum()
    return a


def get_order_two():
    x = 254 + x_pad
    y = 122 + y_pad
    box = (x, y, x + ORDER_WIDTH, y + ORDER_HEIGHT)
    im = ImageOps.grayscale(ImageGrab.grab(box))
    a = array(im.getcolors())
    a = a.sum()
    return a


def get_order_three():
    x = 456 + x_pad
    y = 122 + y_pad
    box = (x, y, x + ORDER_WIDTH, y + ORDER_HEIGHT)
    im = ImageOps.grayscale(ImageGrab.grab(box))
    a = array(im.getcolors())
    a = a.sum()
    return a


def get_order_four():
    x = 658 + x_pad
    y = 122 + y_pad
    box = (x, y, x + ORDER_WIDTH, y + ORDER_HEIGHT)
    im = ImageOps.grayscale(ImageGrab.grab(box))
    a = array(im.getcolors())
    a = a.sum()
    return a


def get_order_five():
    x = 860 + x_pad
    y = 122 + y_pad
    box = (x, y, x + ORDER_WIDTH, y + ORDER_HEIGHT)
    im = ImageOps.grayscale(ImageGrab.grab(box))
    a = array(im.getcolors())
    a = a.sum()
    return a


def get_order_six():
    x = 1062 + x_pad
    y = 122 + y_pad
    box = (x, y, x + ORDER_WIDTH, y + ORDER_HEIGHT)
    im = ImageOps.grayscale(ImageGrab.grab(box))
    a = array(im.getcolors())
    a = a.sum()
    return a


def get_all_orders():
    return [
        get_order_one(),
        get_order_two(),
        get_order_three(),
        get_order_four(),
        get_order_five(),
        get_order_six(),
    ]


def waitForImage(img_name):
    # pauses program until image is identified (good for loading webpages)
    while True:
        element = pyautogui.locateOnScreen(img_name)
        if element is not None:
            return


def waitForPixel(pixel):
    # pauses program until correct pixel is identified in play area
    # pixel = [x, y, (R, G, B)]
    while True:
        im = screenGrab()
        if im.getpixel((pixel[0], pixel[1])) == pixel[2]:
            break


def checkPixel(pixel):
    im = screenGrab()
    return im.getpixel((pixel[0], pixel[1])) == pixel[2]


def mousePos(cords):
    # moves the mouse within the game play area and clicks
    pyautogui.moveTo(x_pad + cords[0], y_pad + cords[1])
    pyautogui.click()


def gamePixel():
    """
    returns the color and relative game position of the cursor
    """
    x, y = pyautogui.position()
    im = pyautogui.screenshot()
    color = im.getpixel((x, y))

    x = x - x_pad
    y = y - y_pad
    return [x, y, color]


def startGame():
    # move the mouse then scroll
    webbrowser.open("https://www.miniclip.com/games/sushi-go-round/en/#")
    pyautogui.sleep(10)
    pyautogui.moveTo(
        x=500, y=1000
    )  # moved mouse here because args not working for scroll method
    pyautogui.scroll(-410)

    # press big play button
    waitForPixel([499, 406, (253, 122, 59)])
    pyautogui.click()

    # press little play button
    waitForPixel([684, 400, (75, 215, 245)])
    mousePos((684, 400))

    # press the continue button
    waitForPixel([743, 776, (255, 45, 236)])
    mousePos((743, 776))

    # press the skip button (skip tutorial)
    waitForPixel([1160, 902, (255, 203, 46)])
    mousePos((1160, 902))

    # press continue button again
    waitForPixel([644, 754, (255, 45, 236)])
    mousePos((644, 754))


def setup():
    webbrowser.open("https://www.miniclip.com/games/sushi-go-round/en/#")
    pyautogui.sleep(4)
    pyautogui.moveTo(
        x=500, y=1000
    )  # moved mouse here because args not working for scroll method
    pyautogui.scroll(-410)


def clearPlates():
    # clears every plate
    for pos in Cords.plates:
        mousePos(pos)


def checkFood():
    # checks the current stock of food
    for item, count in foodStock.items():
        if item in ["rice", "nori", "roe"] and count < 3:
            buyFood(item)


def makeRoll(recipe):
    if recipe == "onigiri":
        mousePos(Cords.f_rice)
        mousePos(Cords.f_rice)
        mousePos(Cords.f_nori)
        mousePos(Cords.roll)

        # account for decreased stock
        foodStock["rice"] -= 2
        foodStock["nori"] -= 1

    elif recipe == "california roll":
        mousePos(Cords.f_rice)
        mousePos(Cords.f_roe)
        mousePos(Cords.f_nori)
        mousePos(Cords.roll)

        foodStock["rice"] -= 1
        foodStock["roe"] -= 1
        foodStock["nori"] -= 1

    elif recipe == "gunkan maki":
        mousePos(Cords.f_rice)
        mousePos(Cords.f_roe)
        mousePos(Cords.f_roe)
        mousePos(Cords.f_nori)
        mousePos(Cords.roll)

        foodStock["rice"] -= 1
        foodStock["roe"] -= 2
        foodStock["nori"] -= 1

    pyautogui.sleep(1)  # allows mat rolling animation to finish


def buyFood(food):
    if food == "rice":
        mousePos(Cords.phone)
        mousePos(Cords.menu_rice)
        if not checkPixel(Cords.i_rice):
            # rice is available
            mousePos(Cords.buy_rice)
            mousePos(Cords.order)
            foodStock["rice"] += 10
            pyautogui.sleep(3)
        else:
            # rice is not available, try again in 3 seconds
            mousePos(Cords.cancel_rice)
            pyautogui.sleep(3)
            buyFood(food)

    if food == "nori":
        mousePos(Cords.phone)
        mousePos(Cords.toppings)
        if not checkPixel(Cords.i_nori):
            # nori is available
            print("nori is available. buying...")
            mousePos(Cords.t_nori)
            mousePos(Cords.order)
            foodStock["nori"] += 10
            pyautogui.sleep(3)
        else:
            # nori is not available, try again in 3 seconds
            print("nori is not available. trying again...")
            mousePos(Cords.cancel_topping)
            pyautogui.sleep(3)
            buyFood(food)

    if food == "roe":
        mousePos(Cords.phone)
        mousePos(Cords.toppings)
        if not checkPixel(Cords.i_roe):
            # nori is available
            print("roe is available. buying...")
            mousePos(Cords.t_roe)
            mousePos(Cords.order)
            foodStock["roe"] += 10
            pyautogui.sleep(3)
        else:
            # nori is not available, try again in 3 seconds
            print("roe is not available. trying again...")
            mousePos(Cords.cancel_topping)
            pyautogui.sleep(3)
            buyFood(food)

    # TODO update the rest of the topping features.
    if food == "salmon":
        mousePos(Cords.phone)
        mousePos(Cords.toppings)
        if not checkPixel(Cords.i_salmon):
            # nori is available
            print("nori is available. buying...")
            mousePos(Cords.t_salmon)
            mousePos(Cords.order)
            pyautogui.sleep(2.5)
        else:
            # nori is not available, try again in 3 seconds
            print("nori is not available. trying again...")
            mousePos(Cords.cancel_topping)
            pyautogui.sleep(3)
            buyFood(food)

    if food == "shrimp":
        mousePos(Cords.phone)
        mousePos(Cords.toppings)
        if not checkPixel(Cords.i_shrimp):
            # shrimp is available
            print("shrimp is available. buying...")
            mousePos(Cords.t_shrimp)
            mousePos(Cords.order)
            pyautogui.sleep(2.5)
        else:
            # nori is not available, try again in 3 seconds
            print("shrimp is not available. trying again...")
            mousePos(Cords.cancel_topping)
            pyautogui.sleep(3)
            buyFood(food)
            pass

    if food == "unagi":
        mousePos(Cords.phone)
        mousePos(Cords.toppings)
        if not checkPixel(Cords.i_unagi):
            # unagi is available
            print("unagi is available. buying...")
            mousePos(Cords.t_unagi)
            mousePos(Cords.order)
            pyautogui.sleep(2.5)
        else:
            # unagi is not available, try again in 3 seconds
            print("unagi is not available. trying again...")
            mousePos(Cords.cancel_topping)
            pyautogui.sleep(3)
            buyFood(food)
            pass


def playGame():
    orders = get_all_orders()
    clearPlates()

    for i, order in enumerate(orders):

        # if the customer is ordering something and is not currently eating, make the roll
        if order != Blank.orders[i] and not isEating[i]:
            # check ingredients, make roll
            with suppress(KeyError):  # pixels from "customer payment" upredictably & rarely throw this off, so suppress KeyErrors
                print(f"customer at seat {i + 1} wants {sushiTypes[order]}...")
                checkFood()
                makeRoll(sushiTypes[order])

                # set eat tracking parameters
                isEating[i] = True
                eatingTime[i] = time.time()

        # reset customer seat after 15 seconds
        elif time.time() - eatingTime[i] > 15:
            print(f"customer at {i+1} is done eating.")
            isEating[i] = False


def main():
    startGame()
    while True:
        playGame()


if __name__ == "__main__":
    main()
