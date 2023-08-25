from app import config
import logging

logger = logging.getLogger(__name__)
logger.setLevel(logging.DEBUG)
def clickCursor(pag, x, y):
  pag.moveTo(x, y)
  pag.click()

def writeInPrompt(pag, message):
  writeInMessage(pag, message="/imagine")
  pag.press("enter")
  clickCursor(pag, x=config.X_PROMPT, y=config.Y_PROMPT)
  logger.debug(f"Message: {message}")
  pag.write(message, interval=0.01)
  pag.press("enter")

def writeInMessage(pag, message):
  clickCursor(pag, x=config.X_MES, y=config.Y_MES)
  pag.write(message, interval=0.1)