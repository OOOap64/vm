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
    conn=condb()
    m=len(conn.execute("SELECT * FROM Comp").fetchall())
    if m:
        conn.execute('DELETE FROM Orders WHERE paid=Flase',)
    conn.commit()
    conn.close

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
    conn.execute("""CREATE TABLE IF NOT EXISTS User(id INTEGER, ip VARCHAR(20), game BOOLEAN,
                 pro BOOLEAN, office BOOLEAN, budjet BOOLEAN )""")
    conn.commit()
    conn.execute("""CREATE TABLE IF NOT EXISTS Orders(id INTEGER , ads VARCHAR(200) , name VARCHAR(40) , img VARCHAR(200),  num INTEGER, ip VARCHAR(20), paid BOOLEAN )""")
    conn.commit()
    conn.close()


def ipp():
    h=socket.gethostname()
    h=socket.gethostbyname(h)
    return h

@app.route('/')
def main():
    delete_non_paid_order()
    return render_template('home.html')

@app.route('/', methods=['POST'])
def promocode():
    conn=condb()
    code=request.form['code']
    us=conn.execute('SELECT * from User where id=?', (ipp())) 
    if us is None:
        conn.execute('INSERT INTO User VALUES(?, False, False, False, False)', (ipp()))
        conn.commit()
    if code=='playgame':
        conn.execute('UPDATE User  SET game=True, where ip=?', (ipp()))
        conn.commit()
    return render_template('home.html')

@app.route('/orders')
def order():
    conn=condb()
    delete_non_paid_order()
    m=conn.execute('SELECT * FROM Order where ip=?', (ipp()))
    return render_template('order.html', m=m)

@app.route('/orders/away/<int:i>')
def away(i):
    delete_non_paid_order()
    conn=condb()
    conn.execute('DELETE FROM Order where id=?', (i))
    conn.commit()
    return render_template('order.html')

@app.route('/office')
def office():
    conn=condb()
    delete_non_paid_order()
    m=conn.execute("SELECT * FROM Comp where type=office").fetchall()
    return render_template('good.hmtl', m=m)

@app.route('/game')
def game():
    conn=condb()
    delete_non_paid_order()
    m=conn.execute("SELECT * FROM Comp where type=game").fetchall()
    return render_template('good.hmtl', m=m)

@app.route('/budjet')
def budjet():
    conn=condb()
    delete_non_paid_order()
    m=conn.execute("SELECT * FROM Comp where type=budjet").fetchall()
    return render_template('good.hmtl', m=m)

@app.route('/pro')
def pro():
    conn=condb()
    delete_non_paid_order()
    m=conn.execute("SELECT * FROM Comp where type=pro").fetchall()
    return render_template('goods.hmtl', m=m)

@app.route('/good/<int:g>')
def good(g):
    conn=condb()
    delete_non_paid_order()
    m=conn.execute("SELECT * FROM Comp WHERE id=?", (g)).fetchall()[0]
    return render_template('good.html', i=m)


@app.route('/pay/<int:i>')
def pay(i):
    conn=condb()
    delete_non_paid_order()
    p=conn.execute('SELECT * FROM Comp where id=?', (i)).fetchall()[0]
    disc=conn.execute(f"SELECT {p['type']} FROM User where ip=?", (ipp()))
    url = checkout.url(data).get('checkout_url')
    num=0 
    ords=conn.execute('SELECT * FROM Orders, where ip=?', (ipp())).fetchall()
    num=None
    serch=True
    for i in ords:
        num=round(random.randrange(0, 999))
        if num not in i['num']:
            break
    conn.execute('INSERT INTO Orderss(?, ?, ?, ?, ?, ?, ?)', (len(ords), p['ads'], p['name'], p['img'], num , ipp()))
    api = Api(merchant_id= 1396424,
              secret_key='test')
    checkout = Checkout(api=api)
    data = {
        "currency": "RUS",
        "amount": 0#(float(p['price'])-float(p['price']*float(disc)*0.2))*100
    }
    redirect(url)


if __name__=='__main__':
    iniDB()
    app.run()
