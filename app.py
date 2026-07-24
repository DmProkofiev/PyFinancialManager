import sys
from PySide6.QtWidgets import QApplication
from dependency_injector.wiring import Provide, inject
from Views.main_window import MainWindow
from ViewModels import MainViewModel
from container import AppContainer

@inject
def main(viewModel: MainViewModel = Provide[AppContainer.viewModel]) -> None:
    app = QApplication(sys.argv)
    window = MainWindow(viewModel)
    window.show()

    with open("Resources/style.qss", "r", encoding = "utf8") as f:
        app.setStyleSheet(f.read())
    sys.exit(app.exec())

if __name__ == "__main__":
    container = AppContainer()
    container.config.db.path.from_env("DB_PATH", default="source.db")
    container.wire(modules=[__name__])
    main()