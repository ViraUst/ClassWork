#Author: Vira Ustymenko
#Date: 23rd November, 2026
#Description: Database

import sqlite3

db_connection = sqlite3.connect("Databas.db")
#cursor object
cursor = db_connection.cursor()

createTable = '''create table if not exists weigo(
Name TEXT,
Sex TEXT,
Country TEXT,
Message TEXT,
Subscribe TEXT
)STRICT
'''

cursor.execute(createTable) #run the SQL command
db_connection.commit() #save the change to the database

cursor.close()
db_connection.close()