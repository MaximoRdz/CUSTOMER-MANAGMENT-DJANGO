import mysql.connector

# create a db connection
database = mysql.connector.connect(
    host="localhost", 
    user="root", 
    passwd="SQL_Maxi"
)

# create a cursor
cursor = database.cursor()

# create a database
cursor.execute("CREATE DATABASE crm_database")

print("Database created successfully")