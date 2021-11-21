import logging

class logger:

    def loggen():
        logging.basicConfig(filename=".\\Logs\\automation.log", format="%(asctime)s: %(levelname)s: %(message",
                            datefmt="%Y-%m-%d %H:%M:%S")
        logger=logging.getLogger()
        logger.setLevel(logging.INFO)
        return logger