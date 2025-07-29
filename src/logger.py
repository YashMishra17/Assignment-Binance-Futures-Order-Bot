import logging

def setup_logger(logfile="bot.log"):
    logger = logging.getLogger("BinanceBot")
    if not logger.handlers:
        logger.setLevel(logging.INFO)
        handler = logging.FileHandler(logfile)
        formatter = logging.Formatter("[%(asctime)s] [%(levelname)s] %(message)s")
        handler.setFormatter(formatter)
        logger.addHandler(handler)
    return logger
