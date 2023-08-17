from tkinter.filedialog import askopenfilename
import pandas as pd
import tkinter as tk
import time

global INITIALWRITE, SECONDWRITE, WAITINGTIME
global X_MES, Y_MES, X_PROMPT, Y_PROMPT

def clickCursor(pag, x, y):
    pag.moveTo(x, y)
    pag.click()

def write(pag, message):
    pag.write('/imagine', interval=0.01)
    pag.press("enter")
    clickCursor(X_PROMPT, Y_PROMPT)
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

def loadFile(pag, data):
    rowNum = data.shape[0]
    startRow = 0
    init = INITIALWRITE
    
    while init > 0:
        if startRow > rowNum:
            return
        message = data.iloc[startRow, 1]
        clickCursor(pag, X_MES, Y_MES)
        write(pag, message)
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