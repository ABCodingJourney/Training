from sqlalchemy import create_engine
import pandas as pd 

from .params import *


def create_connection():
        #provide database urlin specific format - eg: mysql://user:password@host:port/database
        cnx = create_engine('mysql+pymysql://'+ username+':'+password+'@'+hostname+':'+str(port)+'/'+database)

        #connect to database 
        connection = cnx.connect()
        sql_query = pd.read_sql_query('SELECT * FROM db1.customer', connection)
        df = pd.DataFrame(sql_query)

        connection.close
        return df
