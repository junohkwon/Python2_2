
#DBconnection.py

import MySQLdb

db_host = "localhost"
db_user = "root"
db_pw = "root"
db_name = "python_testdb"


connect_pool = []

def connectDB():
    connect = MySQLdb.connect(db_host,db_user,db_pw,db_name)
    return connect
