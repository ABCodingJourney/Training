from Loggings.logging_utls import create_logger

log = create_logger('exception_handling_file.log')


def openFile(fileName):
    try:
        if fileName == 'corrupt_file.txt':
            raise Exception
        f = open(fileName)
    except FileNotFoundError:
        log.error("This file does not exist")
    except Exception as e:
        log.exception("Corrupt file")
    else:
        log.info(f.read())
        f.close()
    finally:
        log.info("Finally block")
