import pyautogui as pag
import time
from app.init import checkIfCoordinatesFileExists, getCoorinatesOfCursor, readCoordinatesFile, writeCoordinatesFile
import logging
import time

global INITIALWRITE, SECONDWRITE, WAITINGTIME


INITIALWRITE = 7
SECONDWRITE = 5
WAITINGTIME = 500

logger = logging.getLogger(__name__)
logger.setLevel(logging.DEBUG)

# def writeProgram():
#     print(X_MES, Y_MES)
#     print(X_PROMPT, Y_PROMPT)
#     return

def main():
    global X_MES, Y_MES, X_PROMPT, Y_PROMPT
    logger.debug("Start flow main.")
    isFileExists = checkIfCoordinatesFileExists()
    if not isFileExists:
        X_MES, Y_MES, X_PROMPT, Y_PROMPT = getCoorinatesOfCursor(pag)
        writeCoordinatesFile(X_MES, Y_MES, X_PROMPT, Y_PROMPT)
    else:
        coordinates = readCoordinatesFile()
        X_MES, Y_MES = map(lambda a: int(a.strip()), coordinates[0])
        X_PROMPT, Y_PROMPT = map(lambda a: int(a.strip()), coordinates[1])
    print(X_MES, Y_MES)
    print(X_PROMPT, Y_PROMPT)
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

