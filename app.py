from numpy import *
#from PIL import ImageGrab,ImageOps
import pyautogui
import time

class Cord():
    ReplayBtn = (532,434)
    dinasaur = (275,448)

def restartGame():
    pyautogui.click(Cord.ReplayBtn)

def pressSpace():
    pyautogui.keyDown('space')
    time.sleep(0.05)
    pyautogui.keyUp('space')

def imageGrab():
    box = (Cord.dinasaur[0]+60,Cord.dinasaur[1],Cord.dinasaur[0]+100,Cord.dinasaur[1]+30)
    #x co-ordinate = 243
    #y co-ordinate = 613
    image = ImageGrab.grab(box)
    grayimage = ImageOps.grayscale(image)
    arr = array(grayimage.getcolors())
    return arr.sum()

def main():
    restartGame()
    while True:
        if(imageGrab() != 1447):
            pressSpace()
            #time.sleep(0.1)

main()

