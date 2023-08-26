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
from app.cursorController import *
from app.readWriteMessages import *
from app.readScreenShot import readScreenShot
from app.config import settings
from app import config


logger = logging.getLogger(__name__)
logger.setLevel(logging.DEBUG)

@loggerDecor
def main():
	# INITIATE THE GLOBAL VARIABLES
	settings()
	# Make directory Tmp
	_ = mkdirTmp()

	# Check if file coordinates exists
	isFileExists = checkIfCoordinatesFileExists()
	if not isFileExists:
		config.X_MES, config.Y_MES, config.X_PROMPT, config.Y_PROMPT = getCoorinatesOfCursor(pag)
		writeCoordinatesFile(config.X_MES, config.Y_MES, config.X_PROMPT, config.Y_PROMPT)
	else:
		coordinates = readCoordinatesFile()
		config.X_MES, config.Y_MES = map(lambda a: int(a.strip()), coordinates[0])
		config.X_PROMPT, config.Y_PROMPT = map(lambda a: int(a.strip()), coordinates[1])
	
	logger.debug(f"{config.X_MES}, {config.Y_MES}")
	logger.debug(f"{config.X_PROMPT}, {config.Y_PROMPT}")
	# Open file prompt
	data = openPromptFile()
	count = 3
	while data.empty:
			if count == 0:
					return
			data = openPromptFile()
			count -= 1

	imageGeneratorEngine(pag, data)
