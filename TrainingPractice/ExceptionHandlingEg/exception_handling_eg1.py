from Loggings.logging_utls import create_logger

log = create_logger('exception_handling.log')


def example():

    values = [10,1,2,3,8,5,0,9, "hello"]

    for value in values:
        try:
            log.info(10/int(value))
        except ZeroDivisionError as ze:
            log.error(ze)
        except ValueError as ve:
            log.error(ve)
        except Exception as e:         #always have a habit of logging broader exceptions
            log.exception(e)

    #Multiple exception handling 
    for value in values:
        try:
            log.info(10/int(value))
        except (ZeroDivisionError, ValueError) as e:
            log.error("Invalid")
        except AttributeError as e:
            pass
        except Exception as e:         
            log.exception(e)