import mysql.connector
import pandas as pd

#Database Information
dbhost = str(input("Type your Database Host: "))
dbuser = str(input("Type your Database User: "))
dbpassword = str(input("Type your Database Password: "))
dbname = str(input("Type your Database Name: "))

# Connecting to the Database
connection = mysql.connector.connect(
    host= dbhost,
    user= dbuser,
    password= dbpassword,
    database= dbname
)

# Creating a cursor to execute commands
cursor = connection.cursor()

# Making a Query
query = str(input("Type your Query command: "))
cursor.execute(query)

#Obtaining Results
results = cursor.fetchall()

df = pd.DataFrame(results)

#Converting results to excel file
df.to_excel("Results.xlsx")

# Closing database connection
connection.close()
