import datetime

from Models import Income, Expense, Obligation, ExpenseType


def test_calculate_balance(finance_service, mock_repo):
    mock_repo.get_all_incomes.return_value = [
        Income(amount=5000),
        Income(amount=10000)
    ]
    mock_repo.get_all_expenses.return_value = [
        Expense(amount = 6000),
        Expense(amount = 11000)
    ]
    balance = finance_service.calculate_balance()
    assert balance == 7000

def test_add_expense(finance_service, mock_repo):
    finance_service.add_expense(150.0, ExpenseType.FOOD, "Обед", datetime.now())
    mock_repo.add_expense.assert_called_once()
    expense_arg = mock_repo.add_expense.call_args[0][0]
    assert expense_arg.amount == 150.0
    assert expense_arg.type == ExpenseType.FOOD
    assert expense_arg.description == "Обед"

def test_get_expenses(finance_service, mock_repo):
    mock_repo.get_all_expenses.return_value = [Expense(amount=100.0)]
    expenses = finance_service.get_expense()
    assert len(expenses) == 1
    assert expenses[0].amount == 100.0

def test_add_income(finance_service, mock_repo):
    pass

def test_get_incomes(finance_service, mock_repo):
    pass
