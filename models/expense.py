import sqlite3
from config.config import DATABASE_PATH

class Expense:
    def __init__(self, description, amount, date):
        self.description = description
        self.amount = amount
        self.date = date

    @staticmethod
    def create_table():
        conn = sqlite3.connect(DATABASE_PATH)
        cursor = conn.cursor()
        cursor.execute('''
            CREATE TABLE IF NOT EXISTS expenses (
                id INTEGER PRIMARY KEY,
                description TEXT,
                amount REAL,
                date TEXT
            )
        ''')
        conn.commit()
        conn.close()

    def save(self):
        conn = sqlite3.connect(DATABASE_PATH)
        cursor = conn.cursor()
        cursor.execute('''
            INSERT INTO expenses (description, amount, date)
            VALUES (?, ?, ?)
        ''', (self.description, self.amount, self.date))
        conn.commit()
        conn.close()

    @staticmethod
    def get_all():
        conn = sqlite3.connect(DATABASE_PATH)
        cursor = conn.cursor()
        cursor.execute('SELECT * FROM expenses')
        expenses = cursor.fetchall()
        conn.close()
        return expenses

    @staticmethod
    def delete(expense_id):
        conn = sqlite3.connect(DATABASE_PATH)
        cursor = conn.cursor()
        cursor.execute('DELETE FROM expenses WHERE id = ?', (expense_id,))
        conn.commit()
        conn.close()

    @staticmethod
    def update(expense_id, description, amount, date):
        conn = sqlite3.connect(DATABASE_PATH)
        cursor = conn.cursor()
        cursor.execute('''
            UPDATE expenses
            SET description = ?, amount = ?, date = ?
            WHERE id = ?
        ''', (description, amount, date, expense_id))
        conn.commit()
        conn.close()