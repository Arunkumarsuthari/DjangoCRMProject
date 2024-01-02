import mysql.connector



dataBase=mysql.connector.connect(
    host='localhost',
    user='root',
    password='Arun@2003'
)

cursorObject=dataBase.cursor()

cursorObject.execute("CREATE DATABASE crmdatabase")

print("adding database is done!!")