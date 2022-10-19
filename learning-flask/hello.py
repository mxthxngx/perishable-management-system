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
@app.route('/')
def index():
    conn = get_db_connection()
    orderdeets = conn.execute('SELECT * FROM orderDetails').fetchall()
    conn.close()
    return render_template('index2.html', orderdeets= orderdeets)


@app.route('/create', methods=('GET', 'POST'))
def create():
    if request.method == 'POST':
        customer_name = request.form['customer_name']
        sales_channel = request.form['sales_channel']
        destination = request.form['destination']
        items = request.form['items']
        item_status = request.form['item_status']

        if not customer_name:
            flash('name is required!')
        else:
            conn = get_db_connection()
            conn.execute('INSERT INTO orderDetails (customer_name, sales_channel,destination,items,item_status) VALUES (?, ?,?,?,?)',
                         (customer_name, sales_channel,destination,items,item_status))
            conn.commit()
            conn.close()
            return redirect(url_for('index'))

    return render_template('create.html')

if __name__ == "__main__":
    app.run()