import pytest
from unittest.mock import Mock, call
from PySide6.QtWidgets import QApplication
from PySide6.QtCore import Qt
from ViewModels.main_viewmodel import MainViewModel
from Models import Income, IncomeType, Expense, ExpenseType
from datetime import datetime

@pytest.fixture
def app(qtbot):
    return QApplication.instance() or QApplication([])

def test_get_all_updates_data(view_model, finance_service, mock_repo):
    mock_repo.get_all_incomes.return_value = [Income(amount=100.0)]
    mock_repo.get_all_expenses.return_value = [Expense(amount=50.0)]
    view_model.get_all()
    assert len(view_model.incomes) == 1
    assert len(view_model.expenses) == 1
    assert view_model.balance == 50.0  # 100 - 50

def test_add_income_updates_view(view_model, mock_repo):
    view_model._ui.lineEditIncomeAmount.text = Mock(return_value="200")
    view_model._ui.lineEditIncomeDate.text = Mock(return_value="01.07.2026")
    view_model._ui.lineEditIncomeDesc.text = Mock(return_value="Зарплата")
    view_model._ui.comboBoxIncomeType.currentData = Mock(return_value=IncomeType.PRIMARY_JOB.value)
    view_model.add_income()
    mock_repo.add_income.assert_called_once()
    view_model._ui.lineEditIncomeAmount.clear.assert_called_once()

def test_edit_expense(view_model):
    expense = Expense(id=1, amount=100.0, type=ExpenseType.FOOD, description="Обед")
    view_model._filtered_expenses = [expense]
    view_model._ui.tableExpenses.currentRow = Mock(return_value=0)
    view_model._dialog.edit_expense = Mock(return_value=expense)
    view_model._service.update_expense = Mock()
    view_model.edit_expense()
    view_model._service.update_expense.assert_called_once()