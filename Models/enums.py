from enum import Enum
from typing import List, Dict, Tuple

class BaseEnum(Enum):

# Читаемое наименование для UI
    @property
    def display_name(self) -> str:
        if hasattr(self, '_display_name_'):
            return self._display_name_
        return self.value.replace('_', ' ').title()

# Список кортежей для списка в UI
    @classmethod
    def choices(cls) -> List[Tuple[str, str]]:
        return [(item.value, item.display_name) for item in cls]

# список всех значений
    @classmethod
    def values_list(cls) -> List[str]:
        return [item.value for item in cls]

    @classmethod
    def display_dict(cls) -> Dict[str, str]:
        return {item.value: item.display_name for item in cls}

    def __new__(cls, value, display_name=None):
        obj = object.__new__(cls)
        obj._value_ = value
        obj._display_name_ = display_name or value
        return obj

class IncomeType(BaseEnum):
    PRIMARY_JOB = ("PrimaryJob", "Основная работа")
    TEMPRARY_WORK = ("TempraryWork", "Временная работа")
    FREELANCE = ("Freelance", "Фриланс")
    INVESTMENTS = ("Investments", "Инвестиции")
    PASSIVE_INCOME = ("PassiveIncome", "Пассивный доход")
    GIFTS = ("Gifts", "Подарки")
    TAX_REFUND = ("TaxRefund", "Возврат налогов")
    OTHER = ("Other", "Другое")

class ExpenseType(BaseEnum):
    CREDIT = ("Credit", "Кредит")
    DEBT = ("Debt", "Долг")
    MORTGAGE = ("Mortgage", "Ипотека")
    FINE = ("Fine", "Штраф")
    SERVICES = ("Services", "Услуги")
    PURCHASE = ("Purchase", "Покупка")
    FOOD = ("Food", "Еда")
    TRANSPORT = ("Transport", "Транспорт")
    ENTERTAINMENT = ("Entertainment", "Развлечения")
    HEALTH = ("Health", "Здоровье")
    EDUCATION = ("Education", "Образование")
    CLOTHING = ("Clothing", "Одежда")
    OTHER = ("Other", "Другое")

class ObligationType(BaseEnum):
    CREDIT = ("Credit", "Кредит")
    DEBT = ("Debt", "Долг")
    MORTGAGE = ("Mortgage", "Ипотека")
    LEASE = ("Lease", "Аренда")
    ALIMONY = ("Alimony", "Алименты")
    TAX = ("Tax", "Налоги")
    OTHER = ("Other", "Другое")