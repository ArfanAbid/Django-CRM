import mysql.connector

database=mysql.connector.connect(
    host = 'localhost',
    user ='root',
    passwd= '1122'
    
    
    )

#prepare a cursor object

cursorObject=database.cursor()

#Create a data base

cursorObject.execute("CREATE DATABASE my_database")

print("All Done!")


