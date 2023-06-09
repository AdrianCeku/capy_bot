import mysql.connector
from config import db_host, db_username, db_password, db_name

user_login = mysql.connector.connect(
    host= db_host,
    user= db_username,
    password= db_password,
)

cursor = user_login.cursor()
cursor.execute(f"CREATE DATABASE IF NOT EXISTS {db_name}")
cursor.close()
user_login.close

db = mysql.connector.connect(
    host= db_host,
    user= db_username,
    password= db_password,
    database= db_name
)

cursor = db.cursor()
cursor.execute("CREATE TABLE IF NOT EXISTS logs (id INT AUTO_INCREMENT PRIMARY KEY, username VARCHAR(255), discord_id VARCHAR(255), command VARCHAR(255), prompt VARCHAR(4095), response VARCHAR(32767), date DATE, time TIME )")
cursor.close()
db.close()

def insert(username, discord_id, command, prompt, response):

    connection = mysql.connector.connect(
    host= db_host,
    user= db_username,
    password= db_password,
    database= db_name
    )

    c = connection.cursor()
    query = "INSERT INTO logs (username, discord_id, command, prompt, response, date, time) VALUES (%s, %s, %s, %s, %s, CURDATE(), CURTIME() )"
    values = (username, discord_id, command, prompt, response)
    c.execute(query, values)
    connection.commit()
    c.close()
    connection.close()
