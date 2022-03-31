from loguru import logger
 
logger.add("logs.log")
 
logger.debug("Debug message")
logger.info("Info message")
logger.warning("Warning messange")
logger.error("Error message")
logger.critical("Critical message")