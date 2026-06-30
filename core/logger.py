"""
core/logger.py
--------------

Central logging system for Karen.
"""

import logging

from config import LOG_FILE, LOG_LEVEL


class Logger:

    def __init__(self):

        self.logger = logging.getLogger("Karen")

        if self.logger.handlers:
            return

        self.logger.setLevel(LOG_LEVEL)

        formatter = logging.Formatter(

            "%(asctime)s | %(levelname)-8s | %(message)s"

        )

        file_handler = logging.FileHandler(LOG_FILE)

        file_handler.setFormatter(formatter)

        self.logger.addHandler(file_handler)

    # -----------------------------------------

    def info(self, message: str):

        self.logger.info(message)

    # -----------------------------------------

    def warning(self, message: str):

        self.logger.warning(message)

    # -----------------------------------------

    def error(self, message: str):

        self.logger.error(message)

    # -----------------------------------------

    def debug(self, message: str):

        self.logger.debug(message)