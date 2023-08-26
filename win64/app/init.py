import os
import time
from app.readWriteMessages import *
# from readwritemessage import *
import logging
from functools import wraps

logger = logging.getLogger(__name__)
logger.setLevel(logging.DEBUG)

def loggerDecor(func):
	@wraps(func)
	def wrapper(*agrs, **kwargs):
		logger.debug(f" {func.__name__} Start func.")
		result = func(*agrs, **kwargs)
		logger.debug(f" {func.__name__} End func.")
		return result
	return wrapper

@loggerDecor
def mkdirTmp():
	try:
		os.mkdir("Tmp")
	except FileExistsError:
		pass

@loggerDecor
def readCoordinatesFile():
	currDir = os.getcwd()
	with open(os.path.join(currDir, "Tmp/coordinatesfile.txt"), "r") as rf:
		logger.info("Start reading file coordinatesfile.txt.")
		coordinates = rf.readlines()
		coordinates = [cor.split(" ") for cor in coordinates]
	return coordinates

@loggerDecor
def writeCoordinatesFile(xMes, yMes, xPrompt, yPrompt):
	logger.info("Start writing file coordinatesfile.txt.")
	currDir = os.getcwd()
	coordinates = [f"{xMes} {yMes}\n", f"{xPrompt} {yPrompt}"]
	# try:
	#   os.mkdir("Tmp")
	# except FileExistsError:
	#   pass
	with open(os.path.join(currDir, "Tmp/coordinatesfile.txt"), "w") as wf:
		logger.info("Start writing file to Tmp/coordinatesfile.txt.")
		wf.writelines(coordinates)

@loggerDecor
def checkIfCoordinatesFileExists():
	try:
		coordinates = readCoordinatesFile()
	except FileNotFoundError:
			logger.error("Origin Coordinates file not exists.")
			return 0
	else:
		if len(coordinates) <= 1:
			return 0
		elif len(coordinates[0]) <= 1 or len(coordinates[1]) <= 1:
			return 0
		else:
			return 1
       
@loggerDecor
def getCoorinatesOfCursor(pag):
	logger.info("Start getting coordinates...")
	time.sleep(5)
	messageCoordinates = pag.position()

	X_MES = messageCoordinates.x
	Y_MES = messageCoordinates.y
	clickCursor(pag, X_MES, Y_MES)

	pag.write('/imagine', interval=0.25)
	pag.press("enter")
	time.sleep(5)

	promptCoordinates = pag.position()
	X_PROMPT = promptCoordinates.x
	Y_PROMPT = promptCoordinates.y

	# Delete test prompt
	clickCursor(pag, X_PROMPT + 100, Y_PROMPT)
	pag.press("backspace", presses=11, interval=0.20)

	return X_MES, Y_MES, X_PROMPT, Y_PROMPT

@loggerDecor
def getCoorinatesMessageWindow(pag):
	logger.info("Start getting coordinates...")
	msgGetTopLeft = "Put the cursor at the top left window."
	msgGetBottomRight = "Put the cursor at the bottom right window."
	time.sleep(2)
	pag.write(msgGetTopLeft, interval=0.15)

	topLeftCoordinates = pag.position()
	X_TL = topLeftCoordinates.x
	Y_TL = topLeftCoordinates.y
	logger.debug(f"Top left:  {X_TL}, {Y_TL}")
	pag.press("backspace", presses=len(msgGetTopLeft), interval=0.15)

	pag.write(msgGetBottomRight, interval=0.15)
	time.sleep(6)
	rightBottomCoordinates = pag.position()
	X_BR = rightBottomCoordinates.x
	Y_BR = rightBottomCoordinates.y
	logger.debug(f"Bottom right: {X_BR}, {Y_BR}")
	pag.press("backspace", presses=len(msgGetBottomRight), interval=0.15)
