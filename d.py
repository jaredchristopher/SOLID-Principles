# Created by: Jared Christopher
# File: d.py

from abc import ABC, abstractmethod
from loguru import logger

# Define abstract logging interface
class Logger(ABC):
    @abstractmethod
    def debug(self, message):
        pass
    
    @abstractmethod
    def info(self, message):
        pass
    
    @abstractmethod
    def warning(self, message):
        pass
    
    @abstractmethod
    def error(self, message):
        pass

# Concrete implementation of logger using the loguru library
class LoguruLogger(Logger):
    def debug(self, message):
        logger.debug(message)
    
    def info(self, message):
        logger.info(message)
    
    def warning(self, message):
        logger.warning(message)
    
    def error(self, message):
        logger.error(message)

def main():
    environment = "Quiz4"

    # Dynamically configure logging behavior based on environment or user preferences
    if environment == "Quiz4":
        logger = LoguruLogger()

    # Use the logger
    logger.debug("This is a dubugging message")
    logger.info("This is an info message")
    logger.warning("This is a warning message")
    logger.error("This is an error message")

if __name__ == "__main__":
    main()
