from PySide6.QtWidgets import (
    QDialog, QVBoxLayout, QHBoxLayout, QLabel,
    QLineEdit, QComboBox, QPushButton, QDateEdit
)
from PySide6.QtCore import QDate
from Models import Expense, ExpenseType
from datetime import datetime

class ExpenseDialog(QDialog):
    def __init__(self, expense: Expense, parent=None):
        super().__init__(parent)
        self._original = expense
        self._updated = None

        self.setWindowTitle("Редактирование расхода")
        self.setModal(True)
        self.setMinimumWidth(400)

        layout = QVBoxLayout(self)

        # Сумма
        layout.addWidget(QLabel("Сумма:"))
        self.amount_edit = QLineEdit()
        self.amount_edit.setText(str(expense.amount))
        layout.addWidget(self.amount_edit)

        # Тип
        layout.addWidget(QLabel("Тип:"))
        self.type_combo = QComboBox()
        for t in ExpenseType:
            self.type_combo.addItem(t.display_name, t.value)
        index = self.type_combo.findData(expense.type.value)
        if index >= 0:
            self.type_combo.setCurrentIndex(index)
        layout.addWidget(self.type_combo)

        # Описание
        layout.addWidget(QLabel("Описание:"))
        self.desc_edit = QLineEdit()
        self.desc_edit.setText(expense.description)
        layout.addWidget(self.desc_edit)

        # Дата
        layout.addWidget(QLabel("Дата:"))
        self.date_edit = QDateEdit()
        self.date_edit.setDisplayFormat("dd.MM.yyyy")
        self.date_edit.setDate(QDate(expense.date.year, expense.date.month, expense.date.day))
        layout.addWidget(self.date_edit)

        # Кнопки
        btn_layout = QHBoxLayout()
        ok_btn = QPushButton("OK")
        ok_btn.clicked.connect(self.accept)
        cancel_btn = QPushButton("Отмена")
        cancel_btn.clicked.connect(self.reject)
        btn_layout.addWidget(ok_btn)
        btn_layout.addWidget(cancel_btn)
        layout.addLayout(btn_layout)

    def get_updated_record(self) -> Expense:
        if self._updated is None:
            amount = float(self.amount_edit.text())
            type_str = self.type_combo.currentData()
            expense_type = ExpenseType(type_str)
            description = self.desc_edit.text()
            date = self.date_edit.date().toPython()
            self._updated = Expense(
                id=self._original.id,
                amount=amount,
                type=expense_type,
                description=description,
                date=date,
                created_at=self._original.created_at,
                updated_at=datetime.now()
            )
        return self._updated