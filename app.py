from cloudipsp import Api, Checkout
from flask import Flask, redirect, render_template, request, url_for
import sqlite3
import random
import socket

app=Flask(__name__, static_folder='static')

def condb():
    conn=sqlite3.connect('datas.db')
    conn.row_factory=sqlite3.Row
    return conn

def delete_non_paid_order():
    # conn=condb()
    # m=len(conn.execute("SELECT * FROM Comp").fetchall())
    # if m:
    #     conn.execute('DELETE FROM Orders WHERE paid=0',)
    # conn.commit()
    # conn.close
    pass

def iniDB():
    conn=condb()
    conn.execute("""CREATE TABLE IF NOT EXISTS Comp(id INTEGER PRIMARY KEY,
                  name VARCHAR(50), 
                  price INTEGER, 
                  type VARCHAR(20),
                  videocard VARCHAR(70), 
                  processor VARCHAR(70),
                  mother_curcuit VARCHAR(70),
                  RAM VARCHAR(70),
                  SSD VARCHAR(70),
                  ads VARCHAR(100),
                  img VARCHAR(30))""")
    conn.commit()
    conn.execute("""CREATE TABLE IF NOT EXISTS User(id INTEGER, ip VARCHAR(20), game INTEGER(1),
                 pro INTEGER(1), office  INTEGER(1), budjet  INTEGER(1) )""")
    conn.commit()
    conn.execute("""CREATE TABLE IF NOT EXISTS Orders(id INTEGER , ads VARCHAR(200) , name VARCHAR(40) , img VARCHAR(200),  num INTEGER, ip VARCHAR(20), paid INTEGER(1) )""")
    conn.commit()
    conn.close()


def ipp():
    h=socket.gethostname()
    h=socket.gethostbyname(h)
    return str(h)

@app.route('/')
def main():
    delete_non_paid_order()
    conn=condb()
    us=conn.execute('SELECT * from User where ip=?', (ipp(),)).fetchall()
    print(ipp(), us[0]['ip'])

    if us ==[]:
        conn.execute('INSERT INTO User VALUES(?, ?, 0, 0, 0, 0)', (len(us)+1, ipp(),))
        conn.commit()
    return render_template('home.html')

@app.route('/', methods=['POST'])
def promocode():
    conn=condb()
    code=request.form['promocode']
    if code=='playgame':
        conn.execute('UPDATE User  SET game = 1 where ip=?', (ipp(),))
        conn.commit()
    return render_template('home.html')

@app.route('/orders')
def order():
    conn=condb()
    delete_non_paid_order()
    e=conn.execute("SELECT * FROM Orders where ip=?", (ipp(),)).fetchall()
    return render_template('order.html', m=e)

@app.route('/orders/away/<int:i>')
def away(i):
    delete_non_paid_order()
    conn=condb()
    conn.execute('DELETE FROM Orders where id=?', (i,))
    conn.commit()
    return render_template('order.html')

@app.route('/office')
def office():
    conn=condb()
    delete_non_paid_order()
    u=conn.execute("SELECT * FROM User where ip=?", (ipp(),)).fetchall()[0]
    m=conn.execute("SELECT * FROM Comp where type='office'").fetchall()
    return render_template('goods.html', m=m, u=u)

@app.route('/game')
def game():
    conn=condb()
    delete_non_paid_order()
    m=conn.execute("SELECT * FROM Comp where type='game'").fetchall()
    u=conn.execute("SELECT * FROM User where ip=?", (ipp(),)).fetchall()[0]
    print(u)
    return render_template('goods.html', m=m, u=u)

@app.route('/budjet')
def budjet():
    conn=condb()
    delete_non_paid_order()
    u=conn.execute("SELECT * FROM User where ip=?", (ipp(),)).fetchall()[0]
    m=conn.execute("SELECT * FROM Comp where type='budjet'").fetchall()
    return render_template('goods.html', m=m, u=u)

@app.route('/pro')
def pro():
    conn=condb()
    delete_non_paid_order()
    u=conn.execute("SELECT * FROM User where ip=?", (ipp(),)).fetchall()[0]
    m=conn.execute("SELECT * FROM Comp where type='pro'").fetchall()
    return render_template('goods.html', m=m, u=u)

@app.route('/good/<int:g>')
def good(g):
    conn=condb()
    delete_non_paid_order()
    u=conn.execute("SELECT * FROM User where ip=?", (ipp(),)).fetchall()[0]
    m=conn.execute("SELECT * FROM Comp WHERE id=?", (g,)).fetchall()[0]
    return render_template('good.html', i=m, u=u)


@app.route('/pay/<int:i>')
def pay(i):
    conn=condb()
    delete_non_paid_order()
    p=conn.execute('SELECT * FROM Comp where id=?', (i,)).fetchall()[0]
    disc=conn.execute(f"SELECT * FROM User where ip=?", (ipp(),))
    num=0 
    ords=conn.execute('SELECT * FROM Orders where ip=?', (ipp(),)).fetchall()
    serch=True
    for i in ords:
        num=round(random.randrange(0, 999))
        if num == i['num']:
            break
    conn.execute('INSERT INTO Orders VALUES( ?, ?, ?, ?, ?, ?, ?)', (len(ords)+1, p['ads'], p['name'], p['img'], num , ipp(), 0,))
    conn.commit()
    api = Api(merchant_id= 1396424,
              secret_key='test')
    checkout = Checkout(api=api)
    data = {
        "currency": "USD",
        "amount": 0#(float(p['price'])-float(p['price']*float(disc)*0.2))*100
    }#https://pay.fondy.eu/merchants/5ad6b888f4becb0c33d543d54e57d86c/default/index.html?token=d65ab72ca732187d33c369cc913b33578c68285c
    #https://pay.fondy.eu/merchants/5ad6b888f4becb0c33d543d54e57d86c/default/index.html?token=d65ab72ca732187d33c369cc913b33578c68285c
    url = checkout.url(data).get('checkout_url')
    return redirect(url)


if __name__=='__main__':
    iniDB()
    app.run()
