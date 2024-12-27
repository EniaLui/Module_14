import sqlite3

# Создайние файл базы данных not_telegram.db
conn = sqlite3.connect('not_telegram.db')
# Создайние объект курсора
cursor = conn.cursor()

# Создание таблицы
cursor.execute('''CREATE TABLE IF NOT EXISTS Users (id INTEGER PRIMARY KEY,
    username TEXT NOT NULL, email TEXT NOT NULL, age INTEGER, balance INTEGER NOT NULL
)''')

# Заполнить таблицу
for i in range(1, 11):
    cursor.execute("INSERT INTO Users(username, email, age, balance) VALUES (?, ?, ?, ?)",
                   (f'User{i}', f'example{i}@gmail.com', i*10, 1000))

conn.commit()

# Обновление таблицы (Каждый 2 пункт):
cursor.execute('''UPDATE Users SET balance = 500 WHERE id % 2 != 0''')
conn.commit()

# Удаление каждой 3 записи:
cursor.execute('''DELETE FROM Users WHERE id % 3 = 1''')
conn.commit()

# Создание выборки
cursor.execute('SELECT username, email, age, balance FROM Users WHERE age != 60')
rows = cursor.fetchall()

for row in rows:
    print(f"Имя: {row[0]} | Почта: {row[1]} | Возраст: {row[2]} | Баланс: {row[3]}")

conn.close()