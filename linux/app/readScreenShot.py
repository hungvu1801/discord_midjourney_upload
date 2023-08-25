import pytesseract
import PIL.ImageGrab
import time
import cv2
import re
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
def checkPattern(text=None, count=False):
  pattern1 = "(Your job queue)|(Please wait for)"
  # pattern2 = "(Please check the bottom of the channel)"
  if not count:
    if re.search(pattern1, text):
      return True
    return False
  else:
    with open("Tmp/textOnScreen.txt", "r") as rf:
      text = rf.readline()
    print(text)
    lst = [x for x in re.findall(pattern1, text) if x != ""]
    print(lst)
    if len(lst) == 0:
      return 0
    return round(len(lst) / 2)
  
@loggerDecor   
def readScreenShot():
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
  if checkPattern(text=textCleaned):
     return True
  return False


# print(readScreenShot())
# print(checkPattern(count=True))