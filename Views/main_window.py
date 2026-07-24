# Views/main_window.py
from PySide6.QtWidgets import QMainWindow
from ViewModels.main_viewmodel import MainViewModel
from .ui_main_window import Ui_MainWindow

class MainWindow(QMainWindow):
    def __init__(self, viewModel: MainViewModel):
        super().__init__()
        self._viewModel = viewModel
        self.ui = Ui_MainWindow()
        self.ui.setupUi(self)
        self._viewModel.set_ui(self.ui)
        self._viewModel.set_window(self)

    def closeEvent(self, event):
        self._viewModel.handle_close_event(event)