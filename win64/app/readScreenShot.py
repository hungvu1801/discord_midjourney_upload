import pytesseract
import PIL.ImageGrab
import time
import cv2
import re
from math import ceil
import logging

# from app.init import loggerDecor
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
def screenShot():
    # Capture the screenshot
    time.sleep(1)
    screenshot = PIL.ImageGrab.grab()
    fileName = "Tmp/savedscreenshot.png"
    screenshot.save(fileName)
    return fileName

@loggerDecor
def checkPattern(pattern=None, text=None, count=None):
  # pattern = "(Your job queue)|(Please wait for)"
  # pattern2 = "(Please check the bottom of the channel)"
  if not pattern:
    raise TypeError
  if not text:
    with open("Tmp/textOnScreen.txt", "r") as rf:
      text = rf.readline()
  if not count:
    if re.search(pattern, text):
      return True
    return False
  else:
    print(text)
    lst = [x for x in re.findall(pattern, text) if x != ""]
    print(lst)
    if len(lst) == 0:
      return 0
    return ceil(len(lst) / 2)
  
@loggerDecor   
def readScreenShot(fileName=None):
  if not fileName:
    fileName = screenShot()
  # imageCv = cv2.imread(fileName)
  # Extract the text from the screenshot
  # custom_config = r'-l eng --oem 3 --psm 6'
  text = pytesseract.image_to_string(fileName)
  # text = pytesseract.image_to_string(fileName, config=custom_config)
  textCleaned = re.sub("\n", "", text)
  logger.debug(f"{textCleaned}")
  with open("Tmp/textOnScreen.txt", "w") as wf:
    wf.write(textCleaned)
  return textCleaned

################################### TEST ####################################################
# textscreen = readScreenShot("Tmp/1.png")
# print(textscreen)
# pattern = "(Job queue)|(this job will start)"
# isQueued = checkPattern(pattern, textscreen, True)
# print(isQueued)

# print(checkPattern(count=True))