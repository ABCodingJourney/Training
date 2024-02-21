import mysql.connector

from .params import *

def create_connection():
        connection = mysql.connector.connect(host=hostname, user=username, password=password, database="db1")

        # cursor object to hold connection
        cursor = connection.cursor()
        cursor.execute("SELECT * FROM db1.customer limit 1")

        #object to hold the records fetched
        records = cursor.fetchall()   

        cursor.close
        connection.close

        
        return records
