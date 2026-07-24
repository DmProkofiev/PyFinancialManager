from dataclasses import dataclass, field
from datetime import date, datetime
from typing import Optional
from Models.enums import ExpenseType

@dataclass
class Expense():
    id: int | None = None
    amount: float = 0.0
    type: Optional[ExpenseType] = None
    description: str = ""
    date: date = date.today()
    created_at: datetime = field(default_factory=datetime.now)
    updated_at: datetime = field(default_factory=datetime.now)