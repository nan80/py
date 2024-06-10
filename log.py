
from logging import getLogger, StreamHandler, Formatter, FileHandler, DEBUG, INFO

def setup_logger(name, logfile='LOGFILENAME.txt'):
    logger = getLogger(name)
    logger.setLevel(DEBUG)

    # create file handler which logs even DEBUG messages
    fh = FileHandler(logfile)
    fh.setLevel(DEBUG)
    fh_formatter = Formatter('%(asctime)s - %(levelname)s - %(filename)s - %(name)s - %(funcName)s - %(message)s')
    fh.setFormatter(fh_formatter)

    # create console handler with a INFO log level
    ch = StreamHandler()
    ch.setLevel(INFO)
    ch_formatter = Formatter('%(asctime)s - %(levelname)s - %(message)s', '%Y-%m-%d %H:%M:%S')
    ch.setFormatter(ch_formatter)

    # add the handlers to the logger
    logger.addHandler(fh)
    logger.addHandler(ch)
    return logger
