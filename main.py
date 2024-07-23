import sqlite3

conn = sqlite3.connect('hw.db')
cursor = conn.cursor()

cursor.execute('''
    CREATE TABLE IF NOT EXISTS products (
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        product_title TEXT NOT NULL,
        price REAL NOT NULL DEFAULT 0.0,
        quantity INTEGER NOT NULL DEFAULT 0
    )
''')
conn.commit()


def add_products():
    products = [
        ('Bread', 1.5, 100),
        ('Milk', 0.99, 200),
        ('Eggs', 2.5, 150),
        ('Butter', 3.75, 80),
        ('Cheese', 4.5, 50),
        ('Apples', 1.2, 120),
        ('Bananas', 0.89, 110),
        ('Chicken', 5.0, 60),
        ('Beef', 7.0, 40),
        ('Fish', 6.5, 70),
        ('Rice', 2.0, 90),
        ('Pasta', 1.1, 130),
        ('Tomatoes', 1.8, 140),
        ('Potatoes', 0.75, 200),
        ('Carrots', 0.65, 180)
    ]
    cursor.executemany('INSERT INTO products (product_title, price, quantity) VALUES (?, ?, ?)', products)
    conn.commit()


add_products()


def update_quantity(id, new_quantity):
    cursor.execute('UPDATE products SET quantity = ? WHERE id = ?', (new_quantity, id))
    conn.commit()


def update_price(id, new_price):
    cursor.execute('UPDATE products SET price = ? WHERE id = ?', (new_price, id))
    conn.commit()


def delete_product(id):
    cursor.execute('DELETE FROM products WHERE id = ?', (id,))
    conn.commit()


def select_all_products():
    cursor.execute('SELECT * FROM products')
    rows = cursor.fetchall()
    for row in rows:
        print(row)


def select_products_by_price_and_quantity(price_limit, quantity_limit):
    cursor.execute('SELECT * FROM products WHERE price < ? AND quantity > ?', (price_limit, quantity_limit))
    rows = cursor.fetchall()
    for row in rows:
        print(row)


def search_products_by_title(keyword):
    cursor.execute("SELECT * FROM products WHERE product_title LIKE ?", ('%' + keyword + '%',))
    rows = cursor.fetchall()
    for row in rows:
        print(row)


def menu():
    while True:
        print("\nМеню:")
        print("1. Изменить количество товара по id")
        print("2. Изменить цену товара по id")
        print("3. Удалить товар по id")
        print("4. Показать все товары")
        print("5. Показать товары дешевле лимита по цене и с количеством больше лимита")
        print("6. Искать товары по названию")
        print("7. Выйти")

        choice = input("Выберите действие (1-7): ")

        if choice == '1':
            id = int(input("Введите id товара: "))
            new_quantity = int(input("Введите новое количество: "))
            update_quantity(id, new_quantity)
            print("Количество обновлено.")
        elif choice == '2':
            id = int(input("Введите id товара: "))
            new_price = float(input("Введите новую цену: "))
            update_price(id, new_price)
            print("Цена обновлена.")
        elif choice == '3':
            id = int(input("Введите id товара: "))
            delete_product(id)
            print("Товар удалён.")
        elif choice == '4':
            select_all_products()
        elif choice == '5':
            price_limit = float(input("Введите лимит по цене: "))
            quantity_limit = int(input("Введите лимит по количеству: "))
            select_products_by_price_and_quantity(price_limit, quantity_limit)
        elif choice == '6':
            keyword = input("Введите слово для поиска: ")
            search_products_by_title(keyword)
        elif choice == '7':
            break
        else:
            print("Неверный выбор, попробуйте снова.")



menu()

conn.close()
