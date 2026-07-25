# Services/IDialogService.py
from typing import Protocol
from typing import Optional
from PySide6.QtWidgets import QWidget
from Models import Expense, Income, Obligation


class IDialogService:
    def show_error(self, parent: Optional[QWidget], message: str, title: str = "Ошибка") -> None:
        raise NotImplementedError

    def show_info(self, parent: Optional[QWidget], message: str, title: str = "Информация") -> None:
        raise NotImplementedError

    def show_warning(self, parent: Optional[QWidget], message: str, title: str = "Предупреждение") -> None:
        raise NotImplementedError

    def show_question(self, parent: Optional[QWidget], message: str, title: str = "Подтверждение") -> bool:
        raise NotImplementedError

    # редактирование
    def edit_expense(self, expense: Expense, parent: Optional[QWidget]) -> Optional[Expense]:
        raise NotImplementedError

    def edit_income(self, income: Income, parent: Optional[QWidget]) -> Optional[Income]:
        raise NotImplementedError

    def edit_obligation(self, obligation: Obligation, parent: Optional[QWidget]) -> Optional[Obligation]:
        raise NotImplementedError