import pyautogui as pag
import time
import pandas as pd
import tkinter as tk
from tkinter.filedialog import askopenfilename
import time

global INITIALWRITE, SECONDWRITE, WAITINGTIME
INITIALWRITE = 7
SECONDWRITE = 5
WAITINGTIME = 500


def click(x, y):
    pag.moveTo(x, y)
    pag.click()

def write(message):
    pag.write('/imagine', interval=0.01)
    pag.press("enter")
    click(X_PROMPT, Y_PROMPT)
    pag.write(message, interval=0.001)
    pag.press("enter")

def readFile():
    root = tk.Tk()
    root.withdraw()
    fileDir = askopenfilename()
    if not fileDir:
        return
    data = pd.read_excel(fileDir)
    return data

def loadFile(data):
    rowNum = data.shape[0]
    startRow = 0
    init = INITIALWRITE
    
    while init > 0:
        if startRow > rowNum:
            return
        message = data.iloc[startRow, 1]
        click(X_MES, Y_MES)
        write(message)
        init -= 1
        startRow +=1
        
    while True:
        if startRow > rowNum:
            return
        secondWrite = SECONDWRITE
        time.sleep(WAITINGTIME)
        while secondWrite > 0:
            secondWrite -= 1
            startRow +=1
            if startRow > rowNum:
                return
            pass
        
    return

def testCoordinate():
    global X_MES, Y_MES, X_PROMPT, Y_PROMPT
    X_MES = 0
    Y_MES = 0
    X_PROMPT = 0 
    Y_PROMPT = 0
    time.sleep(5)
    messageCoordinate = pag.position()
    print(messageCoordinate)
    X_MES = messageCoordinate.x
    Y_MES = messageCoordinate.y
    click(X_MES, Y_MES)

    pag.write('/imagine', interval=0.25)
    pag.press("enter")
    time.sleep(5)
    promptCoordinate = pag.position()
    X_PROMPT = promptCoordinate.x
    Y_PROMPT = promptCoordinate.y
 
    return 1

def writeProgram():
    print(X_MES, X_PROMPT)
    print(Y_MES, Y_PROMPT)
    return

def main():
    testCoordinate()
    print(X_MES, X_PROMPT)
    print(Y_MES, Y_PROMPT)
    # writeProgram()

    # print(pag.size())
    # # print(pag.position())
    # pag.moveTo(485, 1029)
    # pag.click()
    # # pag.write('Hello world!', interval=0.25)
    # pag.write('/imagine', interval=0.25)
    # pag.press("enter")
    # time.sleep(1)
    # pag.moveTo(603, 1038)
    # pag.click()

    # # pag.write(r"https://s.mj.run/dAewiDMdcaI, Colorful A Fish Watercolor Sublimation Clipart, Clipart, white background, no watermark, no text, no word, --v 5 -")
    # pag.write(r"https://s.mj.run/mfVX6TpPUmE, Medieval Ruin Sublimation Clipart, Clipart, white background, no watermark, no text, no word, --v 5 -")
    # pag.press("enter")

