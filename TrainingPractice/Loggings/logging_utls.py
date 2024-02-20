import logging

def create_logger(log_file_name):
    log = logging.getLogger(log_file_name)
    log.setLevel(logging.INFO)
    file_handler = logging.FileHandler('logs/'+log_file_name)
    stream_handler = logging.StreamHandler()

    formatter = logging.Formatter('%(asctime)s:%(funcName)s:%(message)s')
    file_handler.setFormatter(formatter)

    log.addHandler(file_handler)
    log.addHandler(stream_handler)

    return log