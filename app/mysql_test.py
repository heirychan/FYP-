import mysql.connector
 
mydb = mysql.connector.connect(
  host="localhost",
  user="root",
  passwd="123"
)
 
mycursor = mydb.cursor()
 
mycursor.execute("CREATE DATABASE runoob_db")