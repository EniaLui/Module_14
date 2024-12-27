import sqlite3

# Код из предыдущего задания
#from module_14_1 import * #(нет необходимости при доступе к not_telegram.db)
connection = sqlite3.connect('not_telegram.db')
cursor = connection.cursor()

#  Удаление пользователя с id=6
cursor.execute("DELETE FROM Users WHERE id = 6")
connection.commit()

#  Подсчёт кол-ва всех пользователей
cursor.execute("SELECT COUNT(*) FROM Users")
total_users = cursor.fetchone()[0]

# Подсчет суммы балансов.
cursor.execute("SELECT SUM(balance) FROM Users")
all_balances = cursor.fetchone()[0]

# Подсчёт суммы всех балансов
cursor.execute("SELECT AVG(balance) FROM Users")
average_balance = cursor.fetchone()[0]
print(average_balance)

connection.close()