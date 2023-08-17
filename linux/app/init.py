import os
import time
from app.readwritemessage import *
import logging

logger = logging.getLogger(__name__)
logger.setLevel(logging.INFO)

def readCoordinatesFile():
  currDir = os.getcwd()
  with open(os.path.join(currDir, "Tmp/coordinatesfile.txt"), "r") as rf:
    logger.info("Start reading file coordinatesfile.txt.")
    coordinates = rf.readlines()
    coordinates = [cor.split(" ") for cor in coordinates]
  return coordinates

def writeCoordinatesFile(xMes, yMes, xPrompt, yPrompt):
  logger.info("Start writing file coordinatesfile.txt.")
  currDir = os.getcwd()
  coordinates = [f"{xMes} {yMes}\n", f"{xPrompt} {yPrompt}"]
  try:
    os.mkdir("Tmp")
  except FileExistsError:
    pass
  with open(os.path.join(currDir, "Tmp/coordinatesfile.txt"), "w") as wf:
    logger.info("Start writing file to Tmp/coordinatesfile.txt.")
    wf.writelines(coordinates)

def checkIfCoordinatesFileExists():
  logger.info("Start Checking...")
  try:
    coordinates = readCoordinatesFile()
    if len(coordinates) <= 1:
        return 0
    elif len(coordinates[0]) <= 1 or len(coordinates[1]) <= 1:
        return 0
    else:
        return 1
  except FileNotFoundError:
      logger.error("Origin Coordinates file not exists.")
      return 0
       

def getCoorinatesOfCursor(pag):
  logger.info("Start getting coordinates...")
  time.sleep(5)
  messageCoordinate = pag.position()
  print(messageCoordinate)
  X_MES = messageCoordinate.x
  Y_MES = messageCoordinate.y
  clickCursor(pag, X_MES, Y_MES)

  pag.write('/imagine', interval=0.25)
  pag.press("enter")
  time.sleep(5)

  promptCoordinate = pag.position()
  X_PROMPT = promptCoordinate.x
  Y_PROMPT = promptCoordinate.y
  
  # Delete test prompt
  clickCursor(pag, X_PROMPT + 100, Y_PROMPT)
  pag.press("backspace", presses=11, interval=0.20)

  return X_MES, Y_MES, X_PROMPT, Y_PROMPT