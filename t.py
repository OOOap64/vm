from flask import Flask, render_template, request, redirect, url_for
import sqlite3

app = Flask(__name__)

# Функция для подключения к базе данных
def get_db_connection():
    conn = sqlite3.connect('database.db')
    conn.row_factory = sqlite3.Row
    return conn


conn=get_db_connection()
conn.execute('''DELETE FROM user''')
#conn.commit()
#conn.execute('''CREATE S cart(
#             id INTEGER PRIMARY KEY AUTOINCREMENT,
#             name VARCHAR(25),
#             time INTEGER(2),
#             price BIGINT)''')
#conn.commit()
#conn.execute('''CREATE TABLE IF NOT EXISTS user(
#             id BIGINT PRIMARY KEY AUTOINCREMENT,
#             name VARCHAR(12),
#             password VARCHAR(12),
#             budjet DOUBLE DEFAULT 1000)
#             ''')   
#conn.commit()
#conn.execute("DROP TABLE goods")
conn.execute("INSERT INTO goods values(1, 'Pizza', 25, 15 )")
conn.commit()
conn.execute("INSERT INTO goods values(2, 'Water', 1, 2 )")
conn.commit()
conn.execute("INSERT INTO goods values(3, 'Soup', 25, 14 )")
conn.commit()
conn.execute('DELETE FROM user')
conn.commit()
conn.close()