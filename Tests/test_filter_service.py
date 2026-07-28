from datetime import datetime

from Models import Income, Expense


def test_change_income_month(filter_service):
    filter_service.change_income_month(1)
    filter_service._income_month = 12
    filter_service._income_year = 2023
    new_month, new_year = filter_service.change_income_month(1)
    assert new_month == 1
    assert new_year == 2024

def test_filter_incomes(filter_service):
    filter_service._income_month = 7
    filter_service._income_year = 2026
    incomes = [
        Income(date=datetime(2026, 7, 15), amount=100.0),
        Income(date=datetime(2026, 8, 10), amount=200.0),
    ]
    filtered = filter_service.filter_incomes(incomes)
    assert len(filtered) == 1
    assert filtered[0].amount == 100.0

def test_filter_expenses(filter_service):
    filter_service._expense_month = 7
    filter_service._expense_year = 2026
    expenses = [
        Expense(date=datetime(2026, 7, 20), amount=50.0),
        Expense(date=datetime(2026, 6, 5), amount=75.0),
    ]
    filtered = filter_service.filter_expenses(expenses)
    assert len(filtered) == 1
    assert filtered[0].amount == 50.0