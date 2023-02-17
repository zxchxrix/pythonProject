import sqlite3

db = 'products.sqlite'

with sqlite3.connect(db) as conn:
    conn.execute('CREATE TABLE IF NOT EXISTS products (product_id INTEGER PRIMARY KEY, name TEXT UNIQUE, quantity INT)')
conn.close()

name = 'shoes'
quantity = 7

try:
    with sqlite3.connect(db) as conn:
        conn.execute('INSERT INTO products VALUES (?, ?)', (name, quantity))
    conn.close()
except Exception as e:
    print('Error inserting: ', e)

conn = sqlite3.connect(db)
results = conn.execute('SELECT * FROM products')
for row in results:
    print(row)