
from pkg.main import execute
from pkg.loggingConfigs import create_logger

log = create_logger('main_logs.log')

try:
    log.info("Creating Connections")
    execute()

except Exception as e:
    log.exception(f"Error occurred {e}")

else:
    log.info("Functions Successful")



