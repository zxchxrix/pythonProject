import sqlite3

db = 'first_db.sqlite'
def create_table():
    with sqlite3.connect(db) as conn:
        conn.execute('CREATE TABLE IF NOT EXISTS products (id int, name text)')
    conn.close()

def insert_example_data():
    with sqlite3.connect(db) as conn:
        conn.execute('INSERT INTO products VALUES (1000, "hat")')
        conn.execute('INSERT INTO products VALUES (1001, "jacket")')
    conn.close()

def display_all_data():
    conn = sqlite3.connect(db)
    results = conn.execute('SELECT * FROM products')

    print(f'Here\'s whats in the db so far:')
    for row in results:
        print(row)

    conn.close()

def display_one_product(product_name):
    conn = sqlite3.connect(db)
    result = conn.execute('SELECT * FROM products WHERE name like ?', (product_name, ))
    first_row = result.fetchone()
    if first_row:
        print('Here\'s the first item in the database for \'jacket\'')
        print(first_row)
    else:
        print('\nNot found\n')

    conn.close()

def create_new_product():
    print('\t\n-- Adding new product --')
    new_id = int(input('Enter new id: '))
    new_name = input('enter new product: ')

    with sqlite3.connect(db) as conn:
        conn.execute(f'INSERT INTO products VALUES (?, ?)', (new_id, new_name))
        print(f'\t-- Product: {new_id} - {new_name} added --\n')
    conn.close()

def update_product():
    update_product = 'wool hat'
    update_id = 1000

    with sqlite3.connect(db) as conn:
        conn.execute(f'UPDATE products SET name = ? WHERE id = ?', (update_product, update_id))
        print('Updated \'wool hat\' to where product id was 1000\n')
    conn.close()

def delete_product():
    print('\t-- Deleting product --')
    delete_this = input('Enter name of product you want to delete: ')

    with sqlite3.connect(db) as conn:
        conn.execute(f'DELETE FROM products WHERE name = ?', (delete_this, ))
        print(f'\t-- Deleted {delete_this} from table')
    conn.close()

create_table()
insert_example_data()
display_all_data()
display_one_product('jacket')
create_new_product()
update_product()
delete_product()