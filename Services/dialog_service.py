from PySide6.QtWidgets import QMessageBox, QWidget
from typing import Optional

class DialogService:
    @staticmethod
    def show_error(parent: Optional[QWidget], message: str, title: str = "Ошибка") -> None:
        QMessageBox.critical(parent, title, message)

    @staticmethod
    def show_info(parent: Optional[QWidget], message: str, title: str = "Информация") -> None:
        QMessageBox.critical(parent, title, message)
