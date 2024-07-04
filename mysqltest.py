#!pip install mysql-connector

import mysql.connector
mydb = mysql.connector.connect(
     host="localhost",
     user="jwang1568",
     passwd="Root1568",
     auth_plugin='mysql_native_password',
     database="sql_store"
)

def mysqltest(db):
    mycursor = db.cursor()
    mycursor.execute("show databases;")
    print("=== show databases ===")    
    for x in mycursor:
        print(x)

    mycursor.execute("use sql_store")
    for x in mycursor:
        print(x)
    mycursor.execute("show tables")
    print("=== show sql_store tables ===")
    for x in mycursor:
        print(x)
    
if __name__ == "__main__":
    mysqltest(mydb)
