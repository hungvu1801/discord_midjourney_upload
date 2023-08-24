import pyautogui as pag
import time
import logging

from app.init import (
    checkIfCoordinatesFileExists, 
    getCoorinatesOfCursor, 
    readCoordinatesFile, 
    writeCoordinatesFile, 
    getCoorinatesMessageWindow,
    loggerDecor,
    mkdirTmp)

from app.readWriteMessages import *
from app.readScreenShot import readScreenShot



logger = logging.getLogger(__name__)
logger.setLevel(logging.DEBUG)

@loggerDecor
def main():
    global X_MES, Y_MES, X_PROMPT, Y_PROMPT
    
    # Make directory Tmp
    _ = mkdirTmp()

    # Check if file coordinates exists
    isFileExists = checkIfCoordinatesFileExists()
    if not isFileExists:
        X_MES, Y_MES, X_PROMPT, Y_PROMPT = getCoorinatesOfCursor(pag)
        writeCoordinatesFile(X_MES, Y_MES, X_PROMPT, Y_PROMPT)
    else:
        coordinates = readCoordinatesFile()
        X_MES, Y_MES = map(lambda a: int(a.strip()), coordinates[0])
        X_PROMPT, Y_PROMPT = map(lambda a: int(a.strip()), coordinates[1])
    logger.debug(f"{X_MES}, {Y_MES}")
    logger.debug(f"{X_PROMPT}, {Y_PROMPT}")



    # getCoorinatesMessageWindow(pag)
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
    return 1
