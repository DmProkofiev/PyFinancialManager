from unittest.mock import Mock
import pytest
from Services import SqliteFinanceRepository, FinanceService, FilterService, TrayService
from Services.Interfaces.IDialogService import IDialogService
from ViewModels import MainViewModel

@pytest.fixture
def mock_repo():
    repo = Mock(spec = SqliteFinanceRepository)
    repo.get_all_expenses.return_value = []
    repo.get_all_incomes.return_value = []
    repo.get_all_obligations.return_value = []
    return repo

@pytest.fixture
def finance_service(mock_repo):
    return FinanceService(mock_repo)

@pytest.fixture
def filter_service():
    return FilterService()

@pytest.fixture
def mock_dialog():
    return Mock(spec=IDialogService)

@pytest.fixture
def mock_tray():
    return Mock(spec=TrayService)

@pytest.fixture
def view_model(finance_service, filter_service, mock_dialog, mock_tray):
    vm = MainViewModel(finance_service, mock_tray, mock_dialog, filter_service)
    vm._ui = Mock()
    vm._ui.tableIncomes = Mock()
    vm._ui.tableExpenses = Mock()
    vm._ui.tableObligations = Mock()
    vm._ui.labelIncomeCurrentMonth = Mock()
    vm._ui.labelExpenseCurrentMonth = Mock()
    vm._ui.label_balance_value = Mock()
    vm._ui.label_expenses_value = Mock()
    vm._ui.label_incomes_value = Mock()
    vm._ui.label_obligations_value = Mock()
    vm._ui.tableMonthStatistics = Mock()
    vm._ui.lineEditIncomeAmount = Mock()
    vm._ui.lineEditIncomeDate = Mock()
    vm._ui.lineEditIncomeDesc = Mock()
    vm._ui.comboBoxIncomeType = Mock()
    vm._ui.lineEditExpenseAmount = Mock()
    vm._ui.lineEditExpenseDate = Mock()
    vm._ui.lineEditExpenseDesc = Mock()
    vm._ui.comboBoxExpenseType = Mock()
    vm._ui.lineEditObligationName = Mock()
    vm._ui.lineEditObligationAmount = Mock()
    vm._ui.lineEditObligationDesc = Mock()
    vm._ui.lineEditObligationDueDate = Mock()
    vm._ui.lineEditObligationStartDate = Mock()
    vm._ui.lineEditObligationMonthlyPayment = Mock()
    vm._ui.lineEditObligationPaidAmount = Mock()
    vm._ui.comboBoxObligationType = Mock()
    vm._ui.btnAddIncome = Mock()
    vm._ui.btnAddExpense = Mock()
    vm._ui.btnAddObligation = Mock()
    vm._ui.btnUpdateExpense = Mock()
    vm._ui.btnUpdateIncome = Mock()
    vm._ui.btnUpdateObligation = Mock()
    vm._ui.btnDeleteExpense = Mock()
    vm._ui.btnDeleteIncome = Mock()
    vm._ui.btnDeleteObligation = Mock()
    vm._ui.btnIncomePrevMonth = Mock()
    vm._ui.btnIncomeNextMonth = Mock()
    vm._ui.btnExpensePrevMonth = Mock()
    vm._ui.btnExpenseNextMonth = Mock()
    return vm