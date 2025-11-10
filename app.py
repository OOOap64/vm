from cloudipsp import Api, Checkout
from flask import Flask, render_template, redirect
import sqlite3


# def ipp():
#     host=socket.gethostname()
#     ip=socket.gethostbyname(host)
#     return str(ip)

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
                 price BIGINT,
                 pathimg VARCHAR(100))''')
    conn.commit()
    conn.close()
    # conn.execute('''CREATE TABLE IF NOT EXISTS user(
    #              id INTEGER PRIMARY KEY,
    #              name VARCHAR(12),
    #              password VARCHAR(12),
    #              email VARCHAR(30),
    #              budjet INTEGER,
    #              ip VARCHAR(20),
    #              ''')   
    # conn.commit()
    
# def s():
#     us=auth()
#     conn=get_db_connection()
#     m=conn.execute("SELECT * FROM cart").fetchall()
#     s=0
#     for i in range(m):
#         s+=float(i['price'])

#     return us, s, m, conn

# def auth():
#     conn=get_db_connection()
#     ip=ipp()
#     users=conn.execute('SELECT * FROM user').fetchall()
#     for i in users:
#         if ip==i['ip']:
#             return i

@app.route('/')
def home():
    conn=get_db_connection()
    goods=conn.execute('SELECT * FROM goods').fetchall()
    conn.close()
    return render_template('home.html', m=goods)

@app.route('/about')
def about():
    return render_template('about.html')

# @app.route("/put_away/<int:g_id>")
# def put_away(g_id):
#     conn=get_db_connection()
#     us=auth()
#     cg=[str(us['count']).split(' ')]
#     cg[g_id-1]=str(int(cg[g_id-1])-1)
#     st=''
#     for i in cg:
#         st+=i
#     conn.execute('''UPDATE TABLE user SET good_id=?
#                  WHERE ip=?;''', (st, ipp(),))
#     conn.commit()
#     conn.close()
#     return redirect(url_for('cart'))

@app.route('/buy/<int:b_id>')
def buy(b_id):
    conn=get_db_connection()
    a=conn.execute('SELECT * from goods').fetchall()
    a=int(a[b_id-1]['price'])
    api = Api(merchant_id= 1396424,
              secret_key='test')
    checkout = Checkout(api=api)
    data = {
        "currency": "USD",
        "amount": a*100
    }
    url = checkout.url(data).get('checkout_url')
    return redirect(url)
    # us=auth()
    # count=[str(us['count']).split(',')]
    # if us['id']==True:
    #     conn=get_db_connection()
    #     count[b_id-1]=str(int(count[b_id-1])+1)
    #     c=''
    #     for cc in count:
    #         c+=cc
    #     conn.execute('''UPDATE user SET count=?  WHERE ip=?;''', (c, ipp()))#, c, ipp()))
    #     conn.commit()
    #     conn.close()


# @app.route("/sign_in")#, methods=['POST'])
# def r():
#     return render_template("sign_in.html")

# # def ordd():
# #     conn=get_db_connection()
# #     mg=conn.execute("SELECT id FROM goods").fetchall()
# #     ord=''
# #     for i in mg:
# #         ord+='0 '
# #     return ord

# @app.route("/sign_in", methods=['POST'])
# def sign_in():
#     if request.method=='POST':
#         nm=request.form['name']
#         ps=request.form['password']
#         em=request.form['email']
#         conn=get_db_connection()
#         m=conn.execute('SELECT * FROM user').fetchall()
#         for i in m:
#             if nm==i[1] and ps==i[2] and em==i[3] and ipp()==i[-1] :
#                return redirect(url_for('home'))
#         # ord=ordd()
#         conn.execute('INSERT INTO user VALUES(?, ?, ?, ?, 50, ?, ?)', (int(len(m)+1), nm, ps, em, ipp()))
#         conn.commit()
#         conn.close()
        
#         return redirect(url_for('home'))
    #return render_template(url_for('sign_in.html'))

# @app.route("/cart")
# def cart():
#     us=auth()
#     count=[str(us['count']).split(',')]
#     conn=get_db_connection()
#     s=0
#     lo=[str(us['order_list']).split(' ')]
#     ms=[]
#     goods=conn.execute('SELECT * FROM goods').fetchall()
#     if len(count)!=0:
#         for i in range(len(goods)):
#             if count[i]>0:
#                 ms.append({'name':goods[i]['name'], 'sum':(goods[i]['price']*int(count[i])), 'time':goods[i]['time']})
#     return render_template('cart.html', m=ms, us=us, sum=s, lo=lo)

# @app.route("/cart", methods=['POST'])
# def pay():
#     us=auth()
#     count=[str(us['count']).split(',')]
#     conn=get_db_connection()
#     s=0
#     goods=conn.execute('SELECT * FROM goods').fetchall()   
#     for d in range(len(count)):
#         s+=int(count[d])*int(goods[d]['price'])
#     if us["budjet"]>=s:
#         conn.execute("UPDATE user SET  budjet=? WHERE  ip=?", (int(us['budjet'])-s, ipp()))
#         conn.commit()
#         conn.execute("UPDATE user SET order_list=? WHERE ip=?", (round(random.random()*10000), ipp()))
#         conn.commit()
#         conn.execute("UPDATE user SET count='' WHERE ip=?", (ordd(), ipp()))
#         conn.commit()
#         conn.close()
#         return redirect(url_for('home'))
#     else:
#         return redirect(url_for('cart'))
    
if __name__=='__main__':
    init_db()
    app.run(debug=True)