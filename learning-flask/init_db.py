import sqlite3
connection = sqlite3.connect('database.db')


with open('schema.sql') as f:
    connection.executescript(f.read())

cur = connection.cursor()

cur.execute("INSERT INTO orderDetails (customer_name, sales_channel,destination,items, item_status) VALUES (?,?,?,?,?)",
            ('Mathangi', 'raj shop','blore',6,'Delivered')
            )

cur.execute("INSERT INTO orderDetails (customer_name, sales_channel,destination,items, item_status) VALUES (?,?,?,?,?)",
            ('Anu', 'Krish shop','blore',5,'Pending')
            )


connection.commit()
connection.close()