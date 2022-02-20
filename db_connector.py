import mysql.connector

#config details for connecting to the mysql databse server through localhost
db_config = {
    'user': 'root',
    'password': '1234',
    'host': 'localhost',
    'database': 'assignment_1'
}

db = mysql.connector.connect(**db_config)
cursor = db.cursor()