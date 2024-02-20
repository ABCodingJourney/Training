import mysql.connector
from tenacity import retry, stop_after_attempt, wait_fixed

from .params import *


@retry(wait=wait_fixed(2), stop=stop_after_attempt(3))
def connect_to_database():
    connection = mysql.connector.connect(host=hostname, user=username, password=password, database=database)

    cursor = connection.cursor()

    cursor.close
    connection.close



