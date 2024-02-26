# Created by: Jared Christopher
# File: d.py

# I created the the class Logger to provide the abstract methods for the logging interface.
# This maintains DIP by allowing my main() funciton to witch between the different logging
# methods without needing any changes. Allowign my main() function to interact with the abstract
# interface instead of LoguruLogger directly, it allows for more flexability.

from abc import ABC, abstractmethod
from loguru import logger

# Define abstract logging interface
class Logger(ABC):
    @abstractmethod
    def debug(self, message):
        print("Debug Message")
    
    @abstractmethod
    def info(self, message):
        print("Info Message")
    
    @abstractmethod
    def warning(self, message):
        print("Warning Message")
    
    @abstractmethod
    def error(self, message):
        print("Error Message")

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
    environment = "Quiz6"

    # Dynamically configure logging behavior based on environment or user preferences
    if environment == "Quiz6":
        logger = LoguruLogger()

    # Use the logger
    logger.debug("This is a dubugging message")
    logger.info("This is an info message")
    logger.warning("This is a warning message")
    logger.error("This is an error message")

if __name__ == "__main__":
    main()
