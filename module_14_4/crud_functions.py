import sqlite3

# Создание файл crud_functions.py с функциями:
# initiate_db: создаёт таблицу Products: id, title(название продукта), description(описание), price(цена) - целое число
def initiate_db():
    conn = sqlite3.connect('products.db')
    cursor = conn.cursor()
    cursor.execute('''CREATE TABLE IF NOT EXISTS Products (
                      id INTEGER PRIMARY KEY AUTOINCREMENT,
                      title TEXT NOT NULL,
                      description TEXT,
                      price INTEGER NOT NULL)''')
    conn.commit()
    conn.close()

# функция get_all_products: возвращает  записи из таблицы Products, полученные при помощи SQL запроса.
def get_all_products():
    conn = sqlite3.connect('products.db')
    cursor = conn.cursor()
    cursor.execute("SELECT * FROM Products")
    products = cursor.fetchall()
    conn.close()
    return products

# Заполнить таблицу продуктами
def add_products():
    conn = sqlite3.connect('products.db')
    cursor = conn.cursor()

    for i in range(1, 5):
        cursor.execute("SELECT * FROM Products WHERE title = ?", (f'Продукт {i}',))
        product = cursor.fetchone()

        if product is None:
            cursor.execute("INSERT INTO Products (title, description, price) VALUES (?, ?, ?)",
                           (f'Продукт {i}', f'Описание {i}', i * 100))
    conn.commit()
    cursor.execute(
        '''UPDATE Products SET title = 'Дыбоволосное зелье', description = 'заставляет волосы выпившего встать дыбом' 
        WHERE id = 1''')
    cursor.execute(
        '''UPDATE Products SET title = 'Зелье сна без сновидений', description = 'лечебное зелье, чтобы вызвать 
        сонливость' WHERE id = 2''')
    cursor.execute('''UPDATE Products SET title = 'Рябиновый отвар', description = 'зелье из рябины' WHERE id = 3''')
    cursor.execute(
        '''UPDATE Products SET title = 'Умиротворяющий бальзам', description = 'Позволяет успокоить нервы и умерить все 
        тревоги' WHERE id = 4''')
    conn.commit()
    conn.close()
