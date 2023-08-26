from app.main import main
import logging
import sys
from logging.handlers import TimedRotatingFileHandler

logging.basicConfig(
	filename="mainlog.log",
	level=logging.INFO, 
	format="%(asctime)s: %(levelname)s : %(message)s ")

if __name__ == "__main__":
	logging.info(f"{'#'*100}")
	logging.info("Start the program.")
	main()