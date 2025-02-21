from models.expense import Expense

def add_expense(description, amount, date):
    expense = Expense(description, amount, date)
    expense.save()

def view_expenses():
    return Expense.get_all()

def delete_expense(expense_id):
    Expense.delete(expense_id)

def update_expense(expense_id, description, amount, date):
    Expense.update(expense_id, description, amount, date)