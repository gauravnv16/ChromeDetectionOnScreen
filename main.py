import pyautogui as pt
from time import sleep

def OpenLinkedIn():
    sleep(5)
    b1 = pt.locateOnScreen("img.png",confidence=0.5)
    pt.moveTo(b1.left+20, b1.top)
    pt.click()

def openChrome():
    pt.click()
    # setting up 90% accuracy

    sleep(10)
    b1 = pt.locateOnScreen("search_field.png", confidence=0.5)
    pt.moveTo(b1.left, b1.top)
    pt.click()
    pt.typewrite("Gaurav N V",interval=0.5)
    pt.typewrite("\n")
    OpenLinkedIn()

def DetectChrome():
    b = pt.locateOnScreen("chrome.png", confidence=0.9)
    pt.moveTo(b.left,b.top)
    openChrome()

DetectChrome()
