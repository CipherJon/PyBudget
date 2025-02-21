import unittest
import sqlite3
from models.expense import Expense
from config.config import DATABASE_PATH

class TestExpense(unittest.TestCase):
    def setUp(self):
        # Recreate the database schema before each test
        conn = sqlite3.connect(DATABASE_PATH)
        cursor = conn.cursor()
        cursor.execute('DROP TABLE IF EXISTS expenses')
        Expense.create_table()
        conn.close()

    def test_add_expense(self):
        expense = Expense('Test Expense', 100.0, '2025-02-21')
        expense.save()
        expenses = Expense.get_all()
        self.assertEqual(len(expenses), 1)
        self.assertEqual(expenses[0][1], 'Test Expense')
        self.assertEqual(expenses[0][2], 100.0)
        self.assertEqual(expenses[0][3], '2025-02-21')

    def test_delete_expense(self):
        expense = Expense('Test Expense', 100.0, '2025-02-21')
        expense.save()
        expenses = Expense.get_all()
        Expense.delete(expenses[0][0])
        expenses = Expense.get_all()
        self.assertEqual(len(expenses), 0)

    def test_update_expense(self):
        expense = Expense('Test Expense', 100.0, '2025-02-21')
        expense.save()
        expenses = Expense.get_all()
        Expense.update(expenses[0][0], 'Updated Expense', 200.0, '2025-02-22')
        expenses = Expense.get_all()
        self.assertEqual(len(expenses), 1)
        self.assertEqual(expenses[0][1], 'Updated Expense')
        self.assertEqual(expenses[0][2], 200.0)
        self.assertEqual(expenses[0][3], '2025-02-22')

if __name__ == '__main__':
    unittest.main()