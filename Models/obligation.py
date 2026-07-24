from dataclasses import dataclass, field
from datetime import date, datetime
from typing import Optional
from .enums import ObligationType

@dataclass
class Obligation():
    id: int | None = None
    name: str=""
    amount: float = 0.0
    type: Optional[ObligationType] = None
    due_date: datetime = field(default_factory=datetime.now)
    start_date: datetime = field(default_factory=datetime.now)
    monthly_payment: float = 0.0
    paid_amount: float = 0.0
    description: str = ""
    created_at: datetime = field(default_factory=datetime.now)
    updated_at: datetime = field(default_factory=datetime.now)

    def __post_init__(self):
        if not self.created_at:
            self.created_at = datetime.now()
        self.updated_at = datetime.now()
        self.validate()

    def validate(self) -> None:
        if not self.name.strip():
            raise ValueError("")