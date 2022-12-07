import sqlite3
import os

DB_FILE_NAME = "hometelegram.db"

if os.path.exists(DB_FILE_NAME) :
    os.remove(DB_FILE_NAME)

con = sqlite3.connect(DB_FILE_NAME)
print("File db ok")
cursor = con.cursor()
cursor.execute("CREATE TABLE user (name varchar(25) PRIMARY KEY)")
cursor.execute("CREATE TABLE message (id INTEGER PRIMARY KEY AUTOINCREMENT, text varchar(1024), username varchar(25), FOREIGN KEY (username) REFERENCES user(name))")
print("Dafaults tables ok")
con.close()
print("--------------------")
print("Database creted ;)")