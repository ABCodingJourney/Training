import pkg.mysqlConnect as mysqlnonorm
import pkg.mysqlConnectAlchemy as sqlalchemy
import pkg.retryUsingTenacity as rt
from pkg.loggingConfigs import create_logger

log = create_logger('connection_logs.log')


def execute():
    
    #MySQL Connection without using ORM package
    try:

        log.info("Create MYSQL connection")
        records = mysqlnonorm.create_connection()

    except Exception as e:
        log.exception(f"Error Occurred: {e}")

    else:
        log.info("Connection Successful")
        log.info(records)

    #Mysql Connection with ORM package - SQLAlchemy Engine
    try:
        log.info("Creating MYSQL connection with SQL Alchemy")
        data = sqlalchemy.create_connection()

    except Exception as e:
        log.exception(f"Error Occurred: {e}")

    else:
        log.info("Connection Successful")
        log.info(data)


    #Retry connection with tenacity
    try:
        log.info("Retrying Connection using tenacity")
        rt.connect_to_database()
    
    except Exception as e:
        log.exception('Failed to connect to database ', e)

    else:
        log.info("Connection Successful")

    finally:
        log.info(rt.connect_to_database.retry.statistics)
    