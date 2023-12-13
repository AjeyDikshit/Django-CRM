# Install Mysql on your computer
# https://dev.mysql.com/downloads/installer/
# pip install mysql
# pip install mysql-connector (If this doesn't work, try the one below)
# pip install mysql-connector-python 

import mysql.connector

dataBase = mysql.connector.connect(
	host = 'localhost',
	user = 'root',
	passwd = 'mysql123' 
	)

# prepare a cursor object
cursorObject = dataBase.cursor()

# Create a database
# Here the name of the Database should match with the 'NAME'
# attribute inside settings.py > DATABASE > default
cursorObject.execute("CREATE DATABASE myCompany")

print("All Done!")