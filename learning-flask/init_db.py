import sqlite3
connection = sqlite3.connect('database.db')


with open('schema.sql') as f:
    connection.executescript(f.read())

cur = connection.cursor()

cur.execute("INSERT INTO orderDetails (partner_name,destination,item_name,items, item_status) VALUES (?,?,?,?,?)",
            ('Mathangi','blore','soap',6,'Delivered')
            )

cur.execute("INSERT INTO stockDetails (item_name,items_available,items_total, action_needed) VALUES (?,?,?,?)",
            ('soap',6,6,'full'))



connection.commit()
connection.close()