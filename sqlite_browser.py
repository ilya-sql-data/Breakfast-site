import sqlite3

con = sqlite3.connect("orders.db")
cur = con.cursor()

# Показать все таблицы
cur.execute("SELECT name FROM sqlite_master WHERE type='table';")
print("Таблицы:", cur.fetchall())

# Посмотреть структуру таблицы
cur.execute("PRAGMA table_info(orders);")
print("Структура таблицы orders:")
for column in cur.fetchall():
    print(column)

# Посмотреть первые 5 заказов
cur.execute("SELECT * FROM orders LIMIT 5;")
print("Примеры заказов:")
for row in cur.fetchall():
    print(row)

con.close()
