import logging
 
logging.basicConfig(filename="logs.log", level=logging.INFO)
 
logging.debug("This is a debug message")
logging.info("Informational message")
logging.error("An error has happened!")