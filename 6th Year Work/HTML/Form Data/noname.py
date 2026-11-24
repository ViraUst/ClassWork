#Author: Vira Ustymenko
#Date: 23rd November, 2026
#Description: Database

import sqlite3

db_connection = sqlite3.connect("Databas.db")
#cursor object
cursor = db_connection.cursor()

grabs_things = '''
select * from weigo
'''

cursor.execute(grabs_things)
data = cursor.fetchall()

print(data)

cursor.close()
db_connection.close()