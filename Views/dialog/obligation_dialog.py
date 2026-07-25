from PySide6.QtWidgets import (
    QDialog, QVBoxLayout, QHBoxLayout, QLabel,
    QLineEdit, QComboBox, QPushButton, QDateEdit
)
from PySide6.QtCore import QDate
from Models import Obligation, ObligationType
from datetime import datetime

class ObligationDialog(QDialog):
    def __init__(self, obligation: Obligation, parent=None):
        super().__init__(parent)
        self._original = obligation
        self._updated = None

        self.setWindowTitle("Редактирование обязательства")
        self.setModal(True)
        self.setMinimumWidth(450)

        layout = QVBoxLayout(self)

        # Название
        layout.addWidget(QLabel("Название:"))
        self.name_edit = QLineEdit()
        self.name_edit.setText(obligation.name)
        layout.addWidget(self.name_edit)

        # Сумма
        layout.addWidget(QLabel("Сумма:"))
        self.amount_edit = QLineEdit()
        self.amount_edit.setText(str(obligation.amount))
        layout.addWidget(self.amount_edit)

        # Тип
        layout.addWidget(QLabel("Тип:"))
        self.type_combo = QComboBox()
        for t in ObligationType:
            self.type_combo.addItem(t.display_name, t.value)
        index = self.type_combo.findData(obligation.type.value)
        if index >= 0:
            self.type_combo.setCurrentIndex(index)
        layout.addWidget(self.type_combo)

        # Дата начала
        layout.addWidget(QLabel("Дата начала:"))
        self.start_date_edit = QDateEdit()
        self.start_date_edit.setDisplayFormat("dd.MM.yyyy")
        self.start_date_edit.setDate(QDate(
            obligation.start_date.year,
            obligation.start_date.month,
            obligation.start_date.day
        ))
        layout.addWidget(self.start_date_edit)

        # Дата окончания
        layout.addWidget(QLabel("Дата окончания:"))
        self.due_date_edit = QDateEdit()
        self.due_date_edit.setDisplayFormat("dd.MM.yyyy")
        self.due_date_edit.setDate(QDate(
            obligation.due_date.year,
            obligation.due_date.month,
            obligation.due_date.day
        ))
        layout.addWidget(self.due_date_edit)

        # Ежемесячный платёж
        layout.addWidget(QLabel("Ежемесячный платёж:"))
        self.monthly_payment_edit = QLineEdit()
        self.monthly_payment_edit.setText(str(obligation.monthly_payment))
        layout.addWidget(self.monthly_payment_edit)

        # Оплачено
        layout.addWidget(QLabel("Оплачено:"))
        self.paid_amount_edit = QLineEdit()
        self.paid_amount_edit.setText(str(obligation.paid_amount))
        layout.addWidget(self.paid_amount_edit)

        # Описание
        layout.addWidget(QLabel("Описание:"))
        self.desc_edit = QLineEdit()
        self.desc_edit.setText(obligation.description)
        layout.addWidget(self.desc_edit)

        # Кнопки
        btn_layout = QHBoxLayout()
        ok_btn = QPushButton("OK")
        ok_btn.clicked.connect(self.accept)
        cancel_btn = QPushButton("Отмена")
        cancel_btn.clicked.connect(self.reject)
        btn_layout.addWidget(ok_btn)
        btn_layout.addWidget(cancel_btn)
        layout.addLayout(btn_layout)

    def get_updated_record(self) -> Obligation:
        if self._updated is None:
            name = self.name_edit.text()
            amount = float(self.amount_edit.text())
            type_str = self.type_combo.currentData()
            obligation_type = ObligationType(type_str)
            start_date = self.start_date_edit.date().toPython()
            due_date = self.due_date_edit.date().toPython()
            monthly_payment = float(self.monthly_payment_edit.text()) if self.monthly_payment_edit.text() else 0.0
            paid_amount = float(self.paid_amount_edit.text()) if self.paid_amount_edit.text() else 0.0
            description = self.desc_edit.text()

            self._updated = Obligation(
                id=self._original.id,
                name=name,
                amount=amount,
                type=obligation_type,
                due_date=due_date,
                start_date=start_date,
                monthly_payment=monthly_payment,
                paid_amount=paid_amount,
                description=description,
                created_at=self._original.created_at,
                updated_at=datetime.now()
            )
        return self._updated