# Services/TrayService.py
import os
from PySide6.QtGui import QIcon, QAction, QPixmap, QColor
from PySide6.QtWidgets import QSystemTrayIcon, QMenu, QApplication

class TrayService:
    _instance = None
    _tray_icon = None

    def __new__(cls):
        if cls._instance is None:
            cls._instance = super().__new__(cls)
        return cls._instance

    def setup_tray(self, window, view_model, icon_path: str) -> None:
        if TrayService._tray_icon is not None:
            return

        if not QSystemTrayIcon.isSystemTrayAvailable():
            return

        icon = QIcon(icon_path)
        if icon.isNull():
            pixmap = QPixmap(64, 64)
            pixmap.fill(QColor(80, 80, 150))
            icon = QIcon(pixmap)

        self._tray_icon = QSystemTrayIcon(icon, window)
        self._tray_icon.setToolTip("FIBER Financial Manager")

        menu = QMenu()
        for label, handler in [
            ("Показать", window.show_window),
            ("Скрыть", window.hide_window),
            (None, None),
            ("Выход", window.quit_application),
        ]:
            if label is None:
                menu.addSeparator()
            else:
                action = QAction(label, window)
                action.triggered.connect(handler)
                menu.addAction(action)

        self._tray_icon.setContextMenu(menu)
        self._tray_icon.activated.connect(window._on_tray_activated)
        self._tray_icon.show()

    def hide_tray(self) -> None:
        if self._tray_icon:
            self._tray_icon.hide()
            self._tray_icon = None
