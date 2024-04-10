import mysql.connector as mysql

def connect_db():
    return mysql.connect(
    user = "root", 
    password = "",
    host = "localhost",
    database = "agence"
)