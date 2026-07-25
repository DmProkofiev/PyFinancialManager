from PySide6.QtWidgets import QMessageBox, QWidget, QDialog
from typing import Optional
from Models import Expense, Income, Obligation
from Views.dialog import ExpenseDialog, IncomeDialog, ObligationDialog


class DialogService:
    @staticmethod
    def show_error(parent: Optional[QWidget], message: str, title: str = "Ошибка") -> None:
        QMessageBox.critical(parent, title, message)

    @staticmethod
    def show_info(parent: Optional[QWidget], message: str, title: str = "Информация") -> None:
        QMessageBox.information(parent, title, message)

    @staticmethod
    def show_warning(parent: Optional[QWidget], message: str, title: str = "Предупреждение") -> None:
        QMessageBox.warning(parent, title, message)

    @staticmethod
    def show_question(parent: Optional[QWidget], message: str, title: str = "Подтверждение") -> bool:
        reply = QMessageBox.question(parent, title, message, QMessageBox.Yes | QMessageBox.No)
        return reply == QMessageBox.Yes

# Редактирование

    @staticmethod
    def edit_expense(expense: Expense, parent: Optional[QWidget]) -> Optional[Expense]:
        dialog = ExpenseDialog(expense, parent)
        if dialog.exec() == QDialog.Accepted:
            return dialog.get_updated_record()
        return None

    @staticmethod
    def edit_income(income: Income, parent: Optional[QWidget]) -> Optional[Income]:
        dialog = IncomeDialog(income, parent)
        if dialog.exec() == QDialog.Accepted:
            return dialog.get_updated_record()
        return None

    @staticmethod
    def edit_obligation(obligation: Obligation, parent: Optional[QWidget]) -> Optional[Obligation]:
        dialog = ObligationDialog(obligation, parent)
        if dialog.exec() == QDialog.Accepted:
            return dialog.get_updated_record()
        return None