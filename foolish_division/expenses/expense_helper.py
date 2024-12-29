from foolish_division.expenses.models import Expense, ExpenseGroup


class ExpenseHelper:
    def __init__(self, expense: Expense):
        self.expense = expense


class ExpenseGroupHelper:
    def __init__(self, category: ExpenseGroup):
        self.category = category
