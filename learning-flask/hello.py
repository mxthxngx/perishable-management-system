from flask import Flask
from flask import Flask, render_template, request, url_for, flash, redirect
import sqlite3

app = Flask(__name__)
app.config['SECRET_KEY'] = 'your secret key'

def get_db_connection():
    conn = sqlite3.connect('database.db')
    conn.row_factory = sqlite3.Row
    return conn

app = Flask(__name__)

@app.route('/', methods=('GET', 'POST'))
def home():
    if request.method == 'POST':
        username = request.form['username']
        password = request.form['password']

        if(username=="admin" and password=="admin"):
            return redirect(url_for('index'))

    return render_template('index.html')


@app.route('/ordered')
def index():
    conn = get_db_connection()
    orderdeets = conn.execute('SELECT * FROM orderDetails').fetchall()
    conn.close()
    return render_template('index2.html', orderdeets= orderdeets)


@app.route('/stock')
def stock():
    conn = get_db_connection()
    stockdeets = conn.execute('SELECT * FROM stockDetails').fetchall()
    conn.close()
    return render_template('stock.html', stockdeets= stockdeets)


@app.route('/create', methods=('GET', 'POST'))
def create():
    if request.method == 'POST':
        partner_name = request.form['partner_name']
        item_name = request.form['item_name']
        destination = request.form['destination']
        items = request.form['items']
        item_status = request.form['item_status']

        if not partner_name:
            flash('name is required!')
        else:
            conn = get_db_connection()
            conn.execute('INSERT INTO orderDetails (partner_name, destination,item_name,items,item_status) VALUES (?, ?,?,?,?)',
                         (partner_name,destination, item_name,items,item_status))
            conn.execute("INSERT INTO stockDetails (item_name,items_available,items_total, action_needed) VALUES (?,?,?,?)",
            (item_name,items,items,'full'))
            conn.commit()
            conn.close()
            return redirect(url_for('index'))

    return render_template('create.html')

if __name__ == "__main__":
    app.run()