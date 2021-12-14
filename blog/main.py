import sqlite3
from models import Post

connection = sqlite3.connect("db.sqlite3")
cursor = connection.cursor()

cursor.execute('''CREATE TABLE IF NOT EXISTS Users(
                fname text
                lname text
                jtitle text
                )''')

user1 = Post("John", "Doe", "Manager")
cursor.execute("INSERT INTO users VALUES (?, ?, ?)", (user1.name, user1.lastname, user1.job_title))
connection.commit()
connection.close()