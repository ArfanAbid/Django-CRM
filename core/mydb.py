import mysql.connector

database = mysql.connector.connect(host = 'localhost', user ='root', password= 'arfan123')

#prepare a cursor object

cursorObject=database.cursor()

#Create a data base

cursorObject.execute("CREATE DATABASE my_database")

print("All Done!")


