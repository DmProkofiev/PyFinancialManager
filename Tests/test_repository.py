import pytest
import sqlite3
from datetime import date, datetime
from Models import Expense, Income, Obligation
from Models.enums import ExpenseType, IncomeType, ObligationType
from Services.repository import SqliteFinanceRepository

@pytest.fixture
def repo():
    return SqliteFinanceRepository(":memory:")

def test_init_creates_tables(repo):
    with sqlite3.connect(":memory:") as conn:
        cursor = conn.execute("SELECT name FROM sqlite_master WHERE type='table'")
        tables = [row[0] for row in cursor.fetchall()]
        assert "expense" in tables
        assert "income" in tables
        assert "obligation" in tables

def test_add_expense(repo):
    expense = Expense(
        amount=100.0,
        type=ExpenseType.FOOD,
        description="Обед",
        date=date(2025, 1, 1)
    )
    repo.add_expense(expense)
    assert expense.id is not None
    all_expenses = repo.get_all_expenses()
    assert len(all_expenses) == 1
    saved = all_expenses[0]
    assert saved.amount == 100.0
    assert saved.type == ExpenseType.FOOD
    assert saved.description == "Обед"
    assert saved.date == date(2025, 1, 1)

def test_get_expense_by_id(repo):
    expense = Expense(amount=50.0, type=ExpenseType.TRANSPORT, description="Такси", date=date(2025, 2, 1))
    repo.add_expense(expense)
    fetched = repo.get_expense_by_id(expense.id)
    assert fetched is not None
    assert fetched.amount == 50.0
    assert fetched.type == ExpenseType.TRANSPORT

def test_update_expense(repo):
    expense = Expense(amount=30.0, type=ExpenseType.ENTERTAINMENT, description="Кино", date=date(2025, 3, 1))
    repo.add_expense(expense)
    expense.amount = 40.0
    expense.description = "Кино с попкорном"
    repo.update_expense(expense)
    updated = repo.get_expense_by_id(expense.id)
    assert updated.amount == 40.0
    assert updated.description == "Кино с попкорном"

def test_delete_expense(repo):
    expense = Expense(amount=20.0, type=ExpenseType.HEALTH, description="Лекарства", date=date(2025, 4, 1))
    repo.add_expense(expense)
    repo.delete_expense(expense.id)
    assert repo.get_expense_by_id(expense.id) is None

def test_add_income(repo):
    income = Income(amount=500.0, type=IncomeType.PRIMARY_JOB, description="Зарплата", date=date(2025, 5, 1))
    repo.add_income(income)
    assert income.id is not None
    all_incomes = repo.get_all_incomes()
    assert len(all_incomes) == 1
    saved = all_incomes[0]
    assert saved.amount == 500.0
    assert saved.type == IncomeType.PRIMARY_JOB

def test_add_obligation(repo):
    obligation = Obligation(
        name="Кредит",
        type=ObligationType.CREDIT,
        amount=10000.0,
        due_date=datetime(2026, 12, 31),
        start_date=datetime(2025, 1, 1),
        monthly_payment=1000.0,
        paid_amount=2000.0,
        description="Автокредит"
    )
    repo.add_obligation(obligation)
    assert obligation.id is not None
    all_obligations = repo.get_all_obligations()
    assert len(all_obligations) == 1
    saved = all_obligations[0]
    assert saved.name == "Кредит"
    assert saved.amount == 10000.0