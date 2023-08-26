from tkinter.filedialog import askopenfilename
import pandas as pd
import tkinter as tk
import time
from app.readScreenShot import readScreenShot, checkPattern
from app.cursorController import *
from app import config
import logging
from functools import wraps
# global INITIALWRITE, SECONDWRITE, WAITINGTIME
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
def openPromptFile():
	root = tk.Tk()
	root.withdraw()
	fileDir = askopenfilename()
	if not fileDir:
			return pd.DataFrame()
	data = pd.read_excel(fileDir, header=None)
	return data

@loggerDecor
def imageGeneratorEngine(pag, data):
	"""
		Use file to generate pictures.
	"""
	rowNum = data.shape[0]
	countRow = 0
	# initWrite = config.INITIALWRITE
	# secondWrite = config.SECONDWRITE
	currentQueuedRow = [0] * rowNum
	currentErroredRow = [0] * rowNum
	patternQueue = "(Job queue)|(this job will start)"
	patternError = "(Your job queue)|(Please wait for)"
	while True:
		if countRow > rowNum - 1:
			return
		message = data.iloc[countRow, 0]
		logger.debug(f"Starting writing row number: {countRow} .")
		# currentRow = countRow
		writeInPrompt(pag, message)
		time.sleep(5)
		_ = readScreenShot()
		isQueued = checkPattern(pattern=patternQueue)
		isErrored = checkPattern(pattern=patternError)
		if isQueued:
			logger.debug(f"Job {countRow} is Queued.")
			currentQueuedRow[countRow] += 1
			pass
		if isErrored:
			currentErroredRow[countRow] += 1
			logger.debug(f"Job {countRow} is Cancelled n={currentErroredRow[countRow]} times.")
			if currentErroredRow[countRow] == 1:
				time.sleep(config.WAITINGTIME)
				continue
			else:
				offSetFromRow = checkPattern(pattern=patternError, count=True)
				if offSetFromRow > 1:
					time.sleep(60)
					continue
		# 	countRow -= 1
		countRow += 1

	# while initWrite > 0:
	# 	if countRow > rowNum - 1:
	# 		return
	# 	message = data.iloc[countRow, 0]
	# 	print(message)
	# 	writeInPrompt(pag, message)
	# 	isQueued = readScreenShot()
	# 	if isQueued:
	# 		offSetFromRow = checkPattern(count=True)

	# 		countRow -= offSetFromRow
	# 		# time.sleep(config.WAITINGTIME)
	# 	time.sleep(5)
	# 	initWrite -= 1
	# 	countRow += 1
	
	# while True:
	# 	if countRow > rowNum - 1:
	# 		return
	# 	isQueued = readScreenShot()
	# 	if isQueued:
	# 		offSetFromRow = checkPattern(count=True)
	# 		countRow -= offSetFromRow
	# 		time.sleep(config.WAITINGTIME)
	# 	while secondWrite > 0:
	# 		message = data.iloc[countRow, 0]
	# 		writeInPrompt(pag, message)
	# 		time.sleep(5)
	# 		countRow += 1
	# 		secondWrite -= 1
	# 		if countRow > rowNum - 1:
	# 			return