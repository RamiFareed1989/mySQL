import os
import pymysql

# Get username from gitpod workspace
# (Modify this variable if runnin on another environment)

username = os.getenv('user')

# Connect to the database

connection = pymysql.connect(host='localhost', user=username, 
password='', db='Chinook')

try: 
    # Run a query
    with connection.cursor() as cursor:
        sql = "Select * from Artist;"
        cursor.execute(sql)
        result = cursor.fetchall()
        print(result)
finally:
    # Close the connection, regardless of whether the above was successful
    connection.close()