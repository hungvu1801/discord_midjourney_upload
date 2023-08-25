from tkinter.filedialog import askopenfilename
import pandas as pd
import tkinter as tk
import time
from app.readScreenShot import readScreenShot, checkPattern
from app.cursorController import *
from app import config
# global INITIALWRITE, SECONDWRITE, WAITINGTIME


def openPromptFile():
	root = tk.Tk()
	root.withdraw()
	fileDir = askopenfilename()
	if not fileDir:
			return pd.DataFrame()
	data = pd.read_excel(fileDir, header=None)
	return data


def imageGenerator(pag, data):
	"""
		Use file to generate pictures.
	"""
	rowNum = data.shape[0]
	countRow = 0
	initWrite = config.INITIALWRITE
	secondWrite = config.SECONDWRITE
	while initWrite > 0:
		if countRow > rowNum - 1:
			return
		message = data.iloc[countRow, 0]
		print(message)
		writeInPrompt(pag, message)
		isQueued = readScreenShot()
		if isQueued:
			offSetFromRow = checkPattern(count=True)

			countRow -= offSetFromRow
			# time.sleep(config.WAITINGTIME)
		time.sleep(5)
		initWrite -= 1
		countRow += 1
	
	while True:
		if countRow > rowNum - 1:
			return
		isQueued = readScreenShot()
		if isQueued:
			offSetFromRow = checkPattern(count=True)
			countRow -= offSetFromRow
			time.sleep(config.WAITINGTIME)
		while secondWrite > 0:
			message = data.iloc[countRow, 0]
			writeInPrompt(pag, message)
			time.sleep(5)
			countRow += 1
			secondWrite -= 1
			if countRow > rowNum - 1:
				return