import sqlite3
from datetime import datetime

class OrderHandler:
    def __init__(self, db_path):
        self.db_path = db_path
        self._create_table()

    def _create_table(self):
        "Создаем таблицу, если ее нет"
    con = sqlite3.connect("orders.db")
    cur = con.cursor()
    cur.execute(
        """CREATE TABLE IF NOT EXISTS orders
        (name TEXT,
        maindish TEXT,
        coffee TEXT,
        fruit TEXT,
        created_at TEXT)"""
    )
    con.commit()
    con.close()

    def save_order(self, order):
        created_at = datetime.now().strftime('%Y-%m-%d %H:%M:%S')
        con = sqlite3.connect(self.db_path)
        cur = con.cursor()
        cur.execute(
            "INSERT INTO orders(name, maindish, coffee, fruit, created_at) VALUES(?,?,?,?,?);",
            (order["name"], order["maindish"], order["coffee"], order["fruit"], created_at),
        )
        con.commit()
        con.close()


    def get_orders(self, sort_by="created_at_desc", date_filter=None):
        """Получаем все заказы из БД"""
        con = sqlite3.connect(self.db_path)
        con.row_factory = sqlite3.Row
        cur = con.cursor()

        query = "SELECT * FROM orders"
        params = []

        if date_filter:
            query += "WHERE DATE(created_at) = ? "
            params.append(date_filter)

        if sort_by == 'created_at_asc':
            query += " ORDER BY datatime(creared_at) ASC"
        elif sort_by == 'created_at_desc':
            query += "ORDER BY datatime(created_at) DESC"

        cur.execute ("SELECT * FROM orders ORDER BY created_at DESC;")
        rows = cur.fetchall()
        con.close()
        return rows
