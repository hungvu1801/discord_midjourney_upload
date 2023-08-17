from app.main import main
import logging
import sys

logging.basicConfig(
    level=logging.INFO, 
    format="%(asctime)s: %(levelname)s: %(funcName)s : %(message)s ", 
    stream=sys.stdout)

if __name__ == "__main__":

    logging.info("Start the program.")
    main()
