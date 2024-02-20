import logging

def logConfig():
    logging.basicConfig(
        level=logging.INFO,
        filename='basic_logs.log',
        format='%(asctime)s %(levelname)s %(message)s',
        datefmt="%d-%m-%Y %H:%M:%S"
    )
