# Services/finance_service.py
from datetime import datetime
from typing import List, Optional
from Services.repository import SqliteFinanceRepository
from Models.expense import Expense
from Models.income import Income
from Models.obligation import Obligation
from Models.enums import ExpenseType, IncomeType, ObligationType
from Services.Interfaces.IFinanceService import IFinanceService

class FinanceService(IFinanceService):
    def __init__(self, repository: SqliteFinanceRepository):
        self._repo = repository

    # READ
    def get_expense(self) -> List[Expense]:
        return self._repo.get_all_expenses()

    def get_income(self) -> List[Income]:
        return self._repo.get_all_incomes()

    def get_obligation(self) -> List[Obligation]:
        return self._repo.get_all_obligations()

    def get_expense_by_id(self, expense_id: int) -> Optional[Expense]:
        return self._repo.get_expense_by_id(expense_id)

    def get_income_by_id(self, income_id: int) -> Optional[Income]:
        return self._repo.get_income_by_id(income_id)

    def get_obligation_by_id(self, obligation_id: int) -> Optional[Obligation]:
        return self._repo.get_obligation_by_id(obligation_id)

    def get_expenses_by_period(self, start: datetime, end: datetime) -> List[Expense]:
        return self._repo.get_expenses_by_period(start, end)

    def get_incomes_by_period(self, start: datetime, end: datetime) -> List[Income]:
        return self._repo.get_incomes_by_period(start, end)

    # РАСЧЁТ
    def calculate_balance(self) -> float:
        total_income = sum(i.amount for i in self.get_income())
        total_expense = sum(e.amount for e in self.get_expense())
        return total_income - total_expense

    # CREATE
    def add_expense(self, amount: float, expense_type: ExpenseType, description: str, date: Optional[datetime]) -> None:
        item = Expense(amount=amount, type=expense_type, description=description, date=date)
        self._repo.add_expense(item)

    def add_income(self, amount: float, income_type: IncomeType, description: str, date: Optional[datetime]) -> None:
        item = Income(amount=amount, type=income_type, description=description, date=date)
        self._repo.add_income(item)

    def add_obligation(self, name: str, obligation_type: ObligationType, amount: float,
                       due_date: Optional[datetime] = None, start_date: Optional[datetime] = None,
                       monthly_payment: float = 0.0, paid_amount: float = 0.0,
                       description: str = "") -> None:
        if due_date is None:
            due_date = datetime.now()
        if start_date is None:
            start_date = datetime.now()
        item = Obligation(name=name, type=obligation_type, amount=amount,
                          due_date=due_date, start_date=start_date,
                          monthly_payment=monthly_payment, paid_amount=paid_amount,
                          description=description)
        self._repo.add_obligation(item)

    # UPDATE
    def update_expense(self, expense: Expense) -> None:
        expense.updated_at = datetime.now()
        self._repo.update_expense(expense)

    def update_income(self, income: Income) -> None:
        income.updated_at = datetime.now()
        self._repo.update_income(income)

    def update_obligation(self, obligation: Obligation) -> None:
        obligation.updated_at = datetime.now()
        self._repo.update_obligation(obligation)

    # DELETE
    def delete_expense(self, expense_id: int) -> None:
        self._repo.delete_expense(expense_id)

    def delete_income(self, income_id: int) -> None:
        self._repo.delete_income(income_id)

    def delete_obligation(self, obligation_id: int) -> None:
        self._repo.delete_obligation(obligation_id)