# to generate log files and format of log files.

import logging

class LogGen:

    @staticmethod
    def loggen():
        handler = logging.FileHandler('.\\Logs\\automation.log',mode='a')
        formatter = logging.Formatter('%(asctime)s - %(name)s - %(levelname)s - %(message)s')
        handler.setFormatter(formatter)
        logger = logging.getLogger()
        logger.addHandler(handler)
        logger.setLevel(logging.INFO)
        return logger