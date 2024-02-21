from logging_utls import create_logger

log = create_logger('logger_eg_logs.logs')

def dict_example():
    my_dict = {"a": 1, "b": 2, "c": 3}
 
    try:
        # Attempt to access a key that may not exist in the dictionary
        value = my_dict["d"]
    except KeyError:
        log.exception("Key not found in the dictionary.")
    except Exception as e:
        log.exception(f"Error ocurred: {e}")
    else:
        log.info("Value corresponding to key 'd':", value)
        
if __name__ == '__main__':
    dict_example()
