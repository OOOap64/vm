import sqlite3

# Функция для подключения к базе данных
def get_db_connection():
    conn = sqlite3.connect('database.db')
    conn.row_factory = sqlite3.Row
    return conn


conn=get_db_connection()
m=conn.execute("SELECT * ")
conn.execute("DROP TABLE goods")
conn.execute('''
        CREATE TABLE goods(
                 id INTEGER PRIMARY KEY,
                 name VARCHAR(25),
                 time INTEGER(2),
                 price BIGINT,
                 pathimg VARCHAR(500))''')
conn.commit()
conn.execute("INSERT INTO goods values(1, 'Pizza', 25, 15, 'https://avatars.mds.yandex.net/i?id=6494f73f563ebae8e2fd426f042b2d45432518f6-5088700-images-thumbs&n=13' )")
conn.commit()
conn.execute("INSERT INTO goods values(2, 'Water', 1, 2, 'https://avatars.mds.yandex.net/i?id=a585b2d3398bccd569e3bfbb35e4a70601b5f7b3457b5acd-12384509-images-thumbs&n=13' )")
conn.commit()
conn.execute("INSERT INTO goods values(3, 'Soup', 25, 14, 'https://avatars.mds.yandex.net/i?id=8306188cc03bfa3a8380d13f10f29ef1ccc9c39c-4219883-images-thumbs&n=13' )")
conn.commit()
conn.close()

