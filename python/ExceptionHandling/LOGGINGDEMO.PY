'''import logging

logging.error("Error")
logging.critical("critical")
logging.warn("Warn")
logging.debug("Debug")
logging.info("Info")'''

#Logging configuration
import logging

logging.basicConfig(filename="mylog.log",level=logging.DEBUG)
logging.critical("Critical")
logging.error("Error")
logging.warn("Warning")
logging.debug("Debug")
logging.info("Info")
