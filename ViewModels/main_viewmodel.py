# ViewModels/main_viewmodel.py
import os
from datetime import datetime
from typing import List, Callable, Any
from PySide6.QtCore import QObject, Signal, Qt
from PySide6.QtGui import QIcon, QAction, QPixmap, QColor
from PySide6.QtWidgets import QSystemTrayIcon, QMenu, QApplication, QTableWidgetItem
from Models import Expense, Income, Obligation
from Models.enums import ExpenseType, IncomeType, ObligationType
from Services.finance_service import FinanceService

# Доделать Obligation

class MainViewModel(QObject):
    error_occurred = Signal(str)
    def __init__(self, service: FinanceService):
        super().__init__()
        self._service = service
        self._ui = None
        self._window = None
        self._tray_icon = None
        self._tray_initialized = False

        self._current_income_month = datetime.now().month
        self._current_income_year = datetime.now().year
        self._current_expense_month = datetime.now().month
        self._current_expense_year = datetime.now().year

        self._expenses: List[Expense] = []
        self._incomes: List[Income] = []
        self._obligations: List[Obligation] = []
        self._balance: float = 0.0

# Окно
    def set_ui(self, ui) -> None:
        self._ui = ui
        self._setup_ui()

    def set_window(self, window) -> None:
        self._window = window
        if not self._tray_initialized:
            self._setup_tray()

    def _setup_ui(self) -> None:
        if not self._ui:
            return
        self._fill_comboboxes()
        self._connect_buttons()
        self._connect_navigation_buttons()
        self.get_all()

# Заполнение комбобоксов

    def _fill_comboboxes(self) -> None:
        self._fill_combobox(self._ui.comboBoxExpenseType, ExpenseType)
        self._fill_combobox(self._ui.comboBoxIncomeType, IncomeType)
        self._fill_combobox(self._ui.comboBoxObligationType, ObligationType)

# Свойства

    @staticmethod
    def _fill_combobox(combo, enum_class) -> None:
        for item in enum_class:
            combo.addItem(item.display_name, item.value)

    @property
    def expenses(self) -> List[Expense]:
        return self._expenses

    @property
    def incomes(self) -> List[Income]:
        return self._incomes

    @property
    def obligations(self) -> List[Obligation]:
        return self._obligations

    @property
    def balance(self) -> float:
        return self._balance

# Подключение всех баттонов
    def _connect_buttons(self) -> None:
        self._ui.btnAddIncome.clicked.connect(self.add_income)
        self._ui.btnAddExpense.clicked.connect(self.add_expense)
        self._ui.btnAddObligation.clicked.connect(self.add_obligation)
        self._ui.btnDeleteExpense.clicked.connect(self.delete_expense)
        self._ui.btnDeleteIncome.clicked.connect(self.delete_income)
        self._ui.btnDeleteObligation.clicked.connect(self.delete_obligation)

    def get_all(self) -> None:
        self._expenses = self._service.get_expense()
        self._incomes = self._service.get_income()
        self._obligations = self._service.get_obligation()
        self._balance = self._service.calculate_balance()
        self._update_all_ui()

    def _update_all_ui(self) -> None:
        self._update_tables()
        self._update_filtered_tables()
        self._update_balance_label()
        self.update_tableMonthStatistic()


    def _update_tables(self) -> None:
        self._update_table(self._ui.tableExpenses, self._expenses, self._expense_to_row)
        self._update_table(self._ui.tableIncomes, self._incomes, self._income_to_row)
        self._update_table(self._ui.tableObligations, self._obligations, self._obligation_to_row)

    def _update_table(self, table, data, row_mapper) -> None:
        table.setRowCount(len(data))
        for row, item in enumerate(data):
            for col, value in enumerate(row_mapper(item)):
                table.setItem(row, col, value)

# фильтрация по месяцу и году Expense Income

    def _connect_navigation_buttons(self) -> None:
        self._ui.btnIncomePrevMonth.clicked.connect(lambda: self._change_month("income", -1))
        self._ui.btnIncomeNextMonth.clicked.connect(lambda: self._change_month("income", 1))
        self._ui.btnExpensePrevMonth.clicked.connect(lambda: self._change_month("expense", -1))
        self._ui.btnExpenseNextMonth.clicked.connect(lambda: self._change_month("expense", 1))

    def _change_month(self, type: str, delta: int) -> None:
        if type == "income":
            new_month = self._current_income_month + delta
            new_year = self._current_income_year
            if new_month > 12:
                new_month = 1
                new_year += 1
            elif new_month < 1:
                new_month = 12
                new_year -= 1
            self._current_income_month = new_month
            self._current_income_year = new_year
            self._update_month_label("income")
            self._update_filtered_tables()

        elif type == "expense":
            new_month = self._current_expense_month + delta
            new_year = self._current_expense_year
            if new_month > 12:
                new_month = 1
                new_year += 1
            elif new_month < 1:
                new_month = 12
                new_year -= 1
            self._current_expense_month = new_month
            self._current_expense_year = new_year
            self._update_month_label("expense")
            self._update_filtered_tables()

    def _update_month_label(self, type: str) -> None:
        if type == "income":
            date_obj = datetime(self._current_income_year, self._current_income_month, 1)
            self._ui.labelIncomeCurrentMonth.setText(date_obj.strftime("%B %Y"))
        elif type == "expense":
            date_obj = datetime(self._current_expense_year, self._current_expense_month, 1)
            self._ui.labelExpenseCurrentMonth.setText(date_obj.strftime("%B %Y"))

    def _update_filtered_tables(self) -> None:
        self._update_table_with_filter(
            self._ui.tableIncomes,
            self._incomes,
            self._income_to_row,
            self._current_income_month,
            self._current_income_year
        )
        self._update_table_with_filter(
            self._ui.tableExpenses,
            self._expenses,
            self._expense_to_row,
            self._current_expense_month,
            self._current_expense_year
        )
        self._update_table(
            self._ui.tableObligations,
            self._obligations,
            self._obligation_to_row
        )

    def _update_table_with_filter(self, table, data, row_mapper, month, year) -> None:

        filtered_data = [
            item for item in data
            if item.date.month == month and item.date.year == year
        ]
        self._update_table(table, filtered_data, row_mapper)

    @staticmethod
    def _expense_to_row(expense: Expense) -> List[QTableWidgetItem]:
        return [
            QTableWidgetItem(expense.date.strftime("%d.%m.%Y")),
            QTableWidgetItem(expense.type.display_name),
            MainViewModel._create_amount_item(expense.amount),
            QTableWidgetItem(expense.description),
        ]

    @staticmethod
    def _income_to_row(income: Income) -> List[QTableWidgetItem]:
        return [
            QTableWidgetItem(income.date.strftime("%d.%m.%Y")),
            QTableWidgetItem(income.type.display_name),
            MainViewModel._create_amount_item(income.amount),
            QTableWidgetItem(income.description),
        ]

    @staticmethod
    def _obligation_to_row(obligation: Obligation) -> List[QTableWidgetItem]:
        remaining = obligation.amount - obligation.paid_amount
        return [
            QTableWidgetItem(obligation.name),
            QTableWidgetItem(obligation.type.display_name),
            MainViewModel._create_amount_item(obligation.amount),
            MainViewModel._create_amount_item(remaining),
            QTableWidgetItem(obligation.due_date.strftime("%d.%m.%Y")),
        ]

    @staticmethod
    def _create_amount_item(amount: float) -> QTableWidgetItem:
        item = QTableWidgetItem(f"{amount:,.2f}")
        item.setTextAlignment(Qt.AlignRight | Qt.AlignVCenter)
        return item

    def _update_balance_label(self) -> None:
        self._ui.label_balance_value.setText(f"{self._balance:,.2f} ₽")
        total_expenses = sum(e.amount for e in self._expenses)
        total_incomes = sum(i.amount for i in self._incomes)
        total_obligations = sum(o.amount - o.paid_amount for o in self._obligations)

        self._ui.label_expenses_value.setText(f"{total_expenses:,.2f} ₽")
        self._ui.label_incomes_value.setText(f"{total_incomes:,.2f} ₽")
        self._ui.label_obligations_value.setText(f"{total_obligations:,.2f} ₽")

# Таблица в разделе Финансы
    def update_tableMonthStatistic(self) -> None:
        month_data = {}
        for income in self._incomes:
            key = income.date.strftime("%Y-%m")
            if key not in month_data:
                month_data[key] = {
                    "income": 0.0,
                    "expense": 0.0,
                    "month_data": income.date.strftime("%B %Y")
                }
            month_data[key]["income"] += income.amount

        for expense in self._expenses:
            key = expense.date.strftime("%Y-%m")
            if key not in month_data:
                month_data[key]={
                    "income": 0.0,
                    "expense": 0.0,
                    "month_data": expense.date.strftime("%B %Y")
                }
            month_data[key]["expense"] += expense.amount

        sort_dict = sorted(month_data.keys())
        self._ui.tableMonthStatistics.setRowCount(len(sort_dict))

        for row, month_key in enumerate(sort_dict):
            data = month_data[month_key]
            self._ui.tableMonthStatistics.setItem(row, 0, QTableWidgetItem(data["month_data"]))
            self._ui.tableMonthStatistics.setItem(row, 1, self._create_amount_item(data["income"]))
            self._ui.tableMonthStatistics.setItem(row, 2, self._create_amount_item(data["expense"]))
            count = data["income"] - data["expense"]
            self._ui.tableMonthStatistics.setItem(row, 3, self._create_amount_item(count))

    def _clear_and_reload(self, *fields) -> None:
        for field in fields:
            field.clear()
        self.get_all()

# Бизнес Логика Expense Income CRUD
    def add_income(self) -> None:
        try:
            amount = float(self._ui.lineEditIncomeAmount.text())
            date = self._ui.lineEditIncomeDate.text()
            if date:
                date = datetime.strptime(date, "%d.%m.%Y")
            else:
                date = datetime.now()
            income_type = IncomeType(self._ui.comboBoxIncomeType.currentData())
            description = self._ui.lineEditIncomeDesc.text()
            self._service.add_income(amount, income_type, description, date)
            self._clear_and_reload(self._ui.lineEditIncomeAmount, self._ui.lineEditIncomeDesc)
        except ValueError as e:
            self.error_occurred.emit(str(e))

    def add_expense(self) -> None:
        try:
            amount = float(self._ui.lineEditExpenseAmount.text())
            date = self._ui.lineEditExpenseDate.text()
            if date:
                date = datetime.strptime(date, "%d.%m.%Y")
            else:
                date = datetime.now()
            expense_type = ExpenseType(self._ui.comboBoxExpenseType.currentData())
            description = self._ui.lineEditExpenseDesc.text()
            self._service.add_expense(amount, expense_type, description, date)
            self._clear_and_reload(self._ui.lineEditExpenseAmount, self._ui.lineEditExpenseDesc)
        except ValueError as e:
            self.error_occurred.emit(str(e))

# доделать
    def add_obligation(self) -> None:
        try:
            name = self._ui.lineEditObligationName.text()
            amount = float(self._ui.lineEditObligationAmount.text())
            obligation_type = ObligationType(self._ui.comboBoxObligationType.currentData())
            due_date_str = self._ui.lineEditObligationDueDate.text()
            start_date_str = self._ui.lineEditObligationStartDate.text()

            if due_date_str:
                due_date = datetime.strptime(due_date_str, "%d.%m.%Y")
            else:
                due_date = datetime.now()
            if start_date_str:
                start_date = datetime.strptime(start_date_str, "%d.%m.%Y")
            else:
                start_date = datetime.now()

            monthly_payment = float(self._ui.lineEditObligationMonthlyPayment.text())
            paid_amount = float(self._ui.lineEditObligationPaidAmount.text())
            description = self._ui.lineEditObligationDesc.text()

            self._service.add_obligation(name=name, obligation_type=obligation_type, amount=amount, due_date=due_date, start_date=start_date, monthly_payment=monthly_payment, paid_amount=paid_amount, description=description)

            self._clear_and_reload(self._ui.lineEditObligationName,self._ui.lineEditObligationAmount, self._ui.lineEditObligationDesc, self._ui.lineEditObligationDueDate, self._ui.lineEditObligationStartDate, self._ui.lineEditObligationMonthlyPayment, self._ui.lineEditObligationPaidAmount)
        except ValueError as e:
            self.error_occurred.emit(str(e))


    def delete_expense(self) -> None:
        self._delete_selected(self._ui.tableExpenses, self._expenses, self._service.delete_expense)

    def delete_income(self) -> None:
        self._delete_selected(self._ui.tableIncomes, self._incomes, self._service.delete_income)

    def delete_obligation(self) -> None:
        self._delete_selected(self._ui.tableObligations, self._obligations, self._service.delete_obligation)

# получение id при выделении строки в таблице

    def _delete_selected(self, table, data, delete_func) -> None:
        row = table.currentRow()
        if row >= 0:
            item_id = data[row].id
            delete_func(item_id)
            self.get_all()

# System Tray

    def _setup_tray(self) -> None:
        if not QSystemTrayIcon.isSystemTrayAvailable() or self._tray_initialized:
            return

        icon = self._load_tray_icon()
        self._tray_icon = QSystemTrayIcon(icon, self._window)
        self._tray_icon.setToolTip("FIBER Financial Manager")

        menu = QMenu()
        for label, handler in [
            ("Показать", self.show_window),
            ("Скрыть", self.hide_window),
            (None, None),
            ("Выход", self.quit_application),
        ]:
            if label is None:
                menu.addSeparator()
            else:
                action = QAction(label, self._window)
                action.triggered.connect(handler)
                menu.addAction(action)

        self._tray_icon.setContextMenu(menu)
        self._tray_icon.activated.connect(self._on_tray_activated)
        self._tray_icon.show()
        self._tray_initialized = True

    def _load_tray_icon(self) -> QIcon:
        base_dir = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
        icon_path = os.path.join(base_dir, "Resources", "FIBERFMico.png")
        icon = QIcon(icon_path)
        if icon.isNull():
            pixmap = QPixmap(64, 64)
            pixmap.fill(QColor(80, 80, 150))
            icon = QIcon(pixmap)
        return icon

    def show_window(self) -> None:
        if self._window:
            self._window.show()
            self._window.raise_()
            self._window.activateWindow()

    def hide_window(self) -> None:
        if self._window:
            self._window.hide()

    def _on_tray_activated(self, reason) -> None:
        if reason == QSystemTrayIcon.DoubleClick:
            if self._window.isVisible():
                self._window.hide()
            else:
                self._window.show()

    def quit_application(self) -> None:
        if self._tray_icon:
            self._tray_icon.hide()
            self._tray_icon = None
        QApplication.quit()

    def handle_close_event(self, event) -> None:
        event.ignore()
        self._window.hide()
        if self._tray_icon:
            self._tray_icon.showMessage(
                "FIBER Financial Manager",
                QSystemTrayIcon.Information,
                2000
            )