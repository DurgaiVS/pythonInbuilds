import mysql.connector

mydb = mysql.connector.connect(
    host='localhost',
    user='root',
    password='dvs003NAMMApaya@&',
    database='collegedatabase'
)

mycursor = mydb.cursor()

mycursor.execute('SELECT *')

for x in mycursor:
    print(x)