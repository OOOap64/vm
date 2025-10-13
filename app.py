from flask import Flask, render_template, request, redirect, url_for
import sqlite3

app = Flask(__name__, static_folder="static")

# Функция для подключения к базе данных
def get_db_connection():
    conn = sqlite3.connect('database.db')
    conn.row_factory = sqlite3.Row
    return conn

def init_db():
    conn=get_db_connection()
    conn.execute('''
        CREATE TABLE IF NOT EXISTS goods(
                 id INTEGER PRIMARY KEY,
                 name VARCHAR(25),
                 time INTEGER(2),
                 price BIGINT)''')
    conn.commit()
    conn.execute('''CREATE TABLE IF NOT EXISTS cart(
                 id INTEGER PRIMARY KEY AUTOINCREMENT,
                 name VARCHAR(25),
                 time INTEGER(2),
                 price BIGINT)''')
    conn.commit()
    conn.execute('''CREATE TABLE IF NOT EXISTS user(
                 id INTEGER PRIMARY KEY AUTOINCREMENT,
                 name VARCHAR(12),
                 password VARCHAR(12),
                 budjet DOUBLE DEFAULT 1000)
                 ''')   
    conn.commit()
    conn.close()
    
    #№\  #if f is None:
    #№\  #    conn.execute("INSERT INTO goods values(1, 'Pizza', 25, 15 )")
    #№\  #    conn.commit()
    #№\  #    conn.execute("INSERT INTO goods values(2, 'Water', 1, 2 )")
    #№\  #    conn.commit()
    #№\  #    conn.execute("INSERT INTO goods values(3, 'Soup', 25, 14 )")
    #№\  #    conn.commit()
    #№\  #if conn.execute('SELECT * FROM user').fetchall():
    #№\  #    conn.execute('DELETE FROM user')
    #№\  #    conn.commit()
        


def s():
    us=auth()
    conn=get_db_connection()
    m=conn.execute("SELECT * FROM cart").fetchall()
    s=0
    for i in range(len(m)):
        s+=float(m[i]['price'])
    return us, s, m, conn
def auth():
    conn=get_db_connection()
    user=conn.execute('SELECT * FROM user').fetchall()
    if user is not None:
        return user
    else:
        return False

@app.route('/')
def home():
    us=auth()
    conn=get_db_connection()
    goods=conn.execute('SELECT * FROM goods').fetchall()
    conn.close()
    return render_template('home.html', m=goods, us=us)

@app.route('/about')
def about():
    us=auth()
    return render_template('about.html', us=us)

@app.route("/put_away/<int:g_id>")
def put_away(g_id):
    conn=get_db_connection()
    conn.execute('DELETE FORM cart WHERE id=?', (g_id,))
    conn.commit()
    conn.close()
    return redirect(url_for('cart'))

@app.route('/buy/<int:b_id>')
def buy(b_id):
    conn=get_db_connection()
    g=conn.execute('SELECT * FROM goods').fetchall()[b_id-1]
    m=conn.execute('SELECT * FROM cart').fetchall()
    conn.execute('INSERT INTO cart VALUES(?, ?, ?, ?)', (len(m)+1, g[1], g[2], g[3] ))
    conn.commit()
    conn.close()
    return redirect(url_for('home'))


@app.route("/sign_in")#, methods=['POST'])
def r():
    return render_template("sign_in.html")

@app.route("/sign_in", methods=['POST'])
def sign_in():
    if request.method=='POST':
        nm=request.form['name']
        ps=request.form['password']
        conn=get_db_connection()
        m=conn.execute('SELECT * FROM user').fetchall()
        conn.execute('INSERT INTO user VALUES(?, ?, ?, 1000)', (int(len(m)+1),nm, ps,))
        conn.commit()
        conn.close()
        return redirect(url_for('home'))
    #return render_template(url_for('sign_in.html'))

@app.route("/cart")
def cart():
    us=auth()
    conn=get_db_connection()
    m=conn.execute("SELECT * FROM cart").fetchall()
    s=0
    for i in range(len(m)):
        s+=float(m[i]['price'])
    conn.close()
    return render_template('cart.html', m=m, us=us, s=s)

@app.route("/cart", methods=['POST'])
def pay():
    us=auth()
    conn=get_db_connection()
    m=conn.execute("SELECT * FROM cart").fetchall()
    s=0
    for i in range(len(m)):
        s+=float(m[i]['price'])
    m=conn.execute("SELECT * FROM cart").fetchall()
    if us[0]["budjet"]>=s:
        conn.execute("UPDATE user SET  budjet=? ", (int(us[0][-1]-float(s)),))
        conn.commit()
        conn.execute('DELETE FROM cart')
        conn.commit()
        conn.close()
        return redirect(url_for('home'))
    else:
        return redirect(url_for('cart'))
    
if __name__=='__main__':
    init_db()
    app.run(debug=True)