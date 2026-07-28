from dependency_injector import containers, providers
from Services import FinanceService, FilterService
from Services.dialog_service import DialogService
from Services.repository import SqliteFinanceRepository
from ViewModels.main_viewmodel import MainViewModel
from Services.tray_service import TrayService

class AppContainer(containers.DeclarativeContainer):
    config = providers.Configuration()
    dialog_service  = providers.Singleton(DialogService)
    tray_service = providers.Singleton(TrayService)
    filter_service = providers.Singleton(FilterService)
    repository = providers.Singleton(SqliteFinanceRepository, db_path = config.db.path)
    service = providers.Factory(FinanceService, repository=repository)
    viewModel = providers.Factory(MainViewModel, service=service, tray_service=tray_service, dialog_service=dialog_service, filter_service=filter_service)