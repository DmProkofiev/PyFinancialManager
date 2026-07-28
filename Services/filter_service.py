from datetime import datetime
from typing import List, Tuple
from Models import Income, Expense
from Services.Interfaces.IFilterService import IFilterService

class FilterService(IFilterService):
    def __init__(self):
        self._income_month = datetime.now().month
        self._income_year = datetime.now().year
        self._expense_month = datetime.now().month
        self._expense_year = datetime.now().year

    @property
    def income_month(self) -> int:
        return self._income_month

    @property
    def income_year(self) -> int:
        return self._income_year

    @property
    def expense_month(self) -> int:
        return self._expense_month

    @property
    def expense_year(self) -> int:
        return self._expense_year

    def change_income_month(self, delta: int) -> Tuple[int, int]:
        new_month = self._income_month + delta
        new_year = self._income_year
        if new_month > 12:
            new_month = 1
            new_year += 1
        elif new_month < 1:
            new_month = 12
            new_year -= 1
        self._income_month = new_month
        self._income_year = new_year
        return new_month, new_year

    def change_expense_month(self, delta: int) -> Tuple[int, int]:
        new_month = self._expense_month + delta
        new_year = self._expense_year
        if new_month > 12:
            new_month = 1
            new_year += 1
        elif new_month < 1:
            new_month = 12
            new_year -= 1
        self._expense_month = new_month
        self._expense_year = new_year
        return new_month, new_year

    def filter_incomes(self, incomes: List[Income]) -> List[Income]:
        return [inc for inc in incomes if inc.date.month == self._income_month and inc.date.year == self._income_year]

    def filter_expenses(self, expenses: List[Expense]) -> List[Expense]:
        return [exp for exp in expenses if exp.date.month == self._expense_month and exp.date.year == self._expense_year]

    def get_income_month_label(self) -> str:
        return datetime(self._income_year, self._income_month, 1).strftime("%B %Y")

    def get_expense_month_label(self) -> str:
        return datetime(self._expense_year, self._expense_month, 1).strftime("%B %Y")