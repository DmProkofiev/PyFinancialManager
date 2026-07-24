import sqlite3
from datetime import datetime
from typing import List, Optional
from Models import expense, income
from Models.expense import Expense
from Models.income import Income
from Models.obligation import Obligation
from Models.enums import ExpenseType, IncomeType, ObligationType
from datetime import date, timedelta

class SqliteFinanceRepository:
    def __init__(self, db_path: str = "source.db"):
        self.db_path = db_path
        self._init_db()

# Создание\Инициализация таблицы
    def _init_db(self) -> None:
        with sqlite3.connect(self.db_path) as conn:
            conn.execute("""
                CREATE TABLE IF NOT EXISTS expense(
                     id INTEGER PRIMARY KEY,
                     amount REAL NOT NULL,
                     type TEXT NOT NULL,
                     description TEXT,
                     date TEXT NOT NULL,
                     created_at TEXT NOT NULL,
                     updated_at TEXT NOT NULL
                )
                 """)
            conn.execute("""
                CREATE TABLE IF NOT EXISTS income(
                    id INTEGER PRIMARY KEY,
                    amount REAL NOT NULL,
                    type TEXT NOT NULL,
                    description TEXT,
                    date TEXT NOT NULL,
                    created_at TEXT NOT NULL,
                    updated_at TEXT NOT NULL
                )
                 """)
            conn.execute("""
                CREATE TABLE IF NOT EXISTS obligation(
                    id INTEGER PRIMARY KEY,
                    name TEXT NOT NULL,
                    type TEXT NOT NULL,
                    amount REAL NOT NULL,
                    due_date TEXT NOT NULL,
                    start_date TEXT NOT NULL,
                    monthly_payment REAL NOT NULL,
                    paid_amount REAL NOT NULL,
                    description TEXT,
                    created_at TEXT NOT NULL,
                    updated_at TEXT NOT NULL 
                )
            """)

# Преобразование строки в Обект
    # Expense
    def _row_to_expense(self, row) -> Expense:
        return Expense(
            id=row[0],
            amount=row[1],
            type=ExpenseType(row[2]),
            description=row[3] or "",
            date=datetime.fromisoformat(row[4]),
            created_at=datetime.fromisoformat(row[5]),
            updated_at=datetime.fromisoformat(row[6])

        )

    # Income
    def _row_to_income(self, row) -> Income:
        return Income(
            id=row[0],
            amount=row[1],
            type=IncomeType(row[2]),
            description=row[3] or "",
            date=datetime.fromisoformat(row[4]),
            created_at=datetime.fromisoformat(row[5]),
            updated_at=datetime.fromisoformat(row[6])
        )

    # Obligation
    def _row_to_obligation(self, row) -> Obligation:
        return Obligation(
            id=row[0],
            name=row[1],
            type=ObligationType(row[2]),
            amount=row[3],
            due_date=datetime.fromisoformat(row[4]),
            start_date=datetime.fromisoformat(row[5]),
            monthly_payment=row[6],
            paid_amount=row[7],
            description=row[8] or "",
            created_at=datetime.fromisoformat(row[9]),
            updated_at=datetime.fromisoformat(row[10])
        )

# Явное Преобразование обьекта в кортеж:для операций INSERT UPDATE

    def _expense_to_tuple(self, expense: Expense) -> tuple:
        return(
            expense.amount,
            expense.type.value,
            expense.description,
            expense.date.isoformat(),
            expense.created_at.isoformat(),
            expense.updated_at.isoformat()
        )

    def _income_to_tuple(self, income: Income) -> tuple:
        return(
            income.amount,
            income.type.value,
            income.description,
            income.date.isoformat(),
            income.created_at.isoformat(),
            income.updated_at.isoformat()
        )

    def _obligation_to_tuple(self, obligation: Obligation):
        return(
            obligation.name,
            obligation.type.value,
            obligation.amount,
            obligation.due_date.isoformat(),
            obligation.start_date.isoformat(),
            obligation.monthly_payment,
            obligation.paid_amount,
            obligation.description,
            obligation.created_at.isoformat(),
            obligation.updated_at.isoformat()
        )

#   Методы CRUD

# Обьект INCOME
# CREATE

    def add_income(self, income: Income) -> None:
        with sqlite3.connect(self.db_path) as conn:
            cursor = conn.execute(
                "INSERT INTO income (amount, type, description, date, created_at, updated_at) VALUES (?, ?, ?, ?, ?, ?)",
                self._income_to_tuple(income)[:6]
            )
            income.id = cursor.lastrowid

# READ

    def get_all_incomes(self) -> List[Income]:
        with sqlite3.connect(self.db_path) as conn:
            cursor = conn.execute(
                "SELECT id, amount, type, description, date, created_at, updated_at FROM income ORDER BY date DESC"
            )
            rows = cursor.fetchall()
        return [self._row_to_income(row) for row in rows]

    def get_income_by_id(self, income_id: int ) -> Optional[Income]:
        with sqlite3.connect(self.db_path) as conn:
            cursor = conn.execute(
                "SELECT id, amount, type, description, date, created_at, updated_at FROM income WHERE id = ?",
                (income_id,)
            )
            row = cursor.fetchone()
        return self._row_to_income(row) if row else None

    def get_incomes_by_period(self, start: datetime, end: datetime) -> List[Income]:
        with sqlite3.connect(self.db_path) as conn:
            cursor = conn.execute(
                "SELECT id, amount, type, description, date, created_at, updated_at "
                "FROM income WHERE date BETWEEN ? AND ? ORDER BY date DESC",
                (start.isoformat(), end.isoformat())
            )
            rows = cursor.fetchall()
        return [self._row_to_income(row) for row in rows]

# UPDATE

    def update_income(self, income: Income) -> None:
        with sqlite3.connect(self.db_path) as conn:
            conn.execute(
                "UPDATE income SET amount=?, type=?, description=?, date=?, created_at=?, updated_at=? WHERE id=?",
                self._income_to_tuple(income)
            )

# DELETE

    def delete_income(self, income_id: int) -> None:
        with sqlite3.connect(self.db_path) as conn:
            conn.execute(
                "DELETE FROM income WHERE id=?",
                (income_id,))

# Обьект EXPENSE
# CREATE

    def add_expense(self, expense: Expense) -> None:
        with sqlite3.connect(self.db_path) as conn:
            cursor = conn.execute(
                "INSERT INTO expense (amount, type, description, date, created_at, updated_at) VALUES (?, ?, ?, ?, ?, ?)",
                self._expense_to_tuple(expense)[:6]
            )
            expense.id = cursor.lastrowid

# READ

    def get_all_expenses(self) -> List[Expense]:
        with sqlite3.connect(self.db_path) as conn:
            cursor = conn.execute(
                 "SELECT id, amount, type, description, date, created_at, updated_at "
                "FROM expense ORDER BY date DESC"
            )
            rows = cursor.fetchall()
        return [self._row_to_expense(row) for row in rows]

    def get_expense_by_id(self, expense_id: int) -> Optional[Expense]:
        with sqlite3.connect(self.db_path) as conn:
            cursor = conn.execute(
                "SELECT id, amount, type, description, date, created_at, updated_at FROM expense WHERE id = ?",
                (expense_id,)
            )
            row = cursor.fetchone()
        return self._row_to_expense(row) if row else None

    def get_expenses_by_period(self, start: datetime, end: datetime) -> List[Expense]:
        with sqlite3.connect(self.db_path) as conn:
            cursor = conn.execute(
                "SELECT id, amount, type, description, date, created_at, updated_at "
                "FROM expense WHERE date BETWEEN ? AND ? ORDER BY date DESC",
                (start.isoformat(), end.isoformat())
            )
            rows = cursor.fetchall()
        return [self._row_to_expense(row) for row in rows]

# UPDATE

    def update_expense(self, expense: Expense) -> None:
        with sqlite3.connect(self.db_path) as conn:
            conn.execute(
                "UPDATE expense SET amount=?, type=?, description=?, date=?, updated_at=? WHERE id=?",
                self._expense_to_tuple(expense)
            )


# DELETE

    def delete_expense(self, expense_id: int) -> None:
        with sqlite3.connect(self.db_path) as conn:
            conn.execute("DELETE FROM expense WHERE id = ?", (expense_id,))

# Обьект Obligation
# CREATE

    def add_obligation(self, obligation: Obligation) -> None:
        with sqlite3.connect(self.db_path) as conn:
            cursor = conn.execute(
                "INSERT INTO obligation (name, type, amount, due_date, start_date, monthly_payment, paid_amount, description, created_at, updated_at) VALUES (? ,? ,? ,?, ? ,? ,? ,? ,?, ?)",
                self._obligation_to_tuple(obligation)[:10]
            )
            obligation.id=cursor.lastrowid
# READ

    def get_all_obligations(self) -> List[Obligation]:
        with sqlite3.connect(self.db_path) as conn:
            cursor = conn.execute(
                "SELECT id, name, type, amount, due_date, start_date, monthly_payment, paid_amount, description, created_at, updated_at FROM obligation ORDER BY due_date ASC",
            )
            rows = cursor.fetchall()
        return [self._row_to_obligation(row) for row in rows]

    def get_obligation_by_id(self, obligation_id: int) -> Optional[Obligation]:
        with sqlite3.connect(self.db_path) as conn:
            cursor = conn.execute(
                "SELECT id, name, type, amount, due_date, start_date, monthly_payment, paid_amount, description, created_at, updated_at FROM obligation WHERE id = ?",
                (obligation_id, )
            )
            row = cursor.fetchone()
            return self._row_to_obligation(row) if row else None

# UPDATE

    def update_obligation(self, obligation: Obligation) -> None:
        with sqlite3.connect(self.db_path) as conn:
            cursor = conn.execute(
                "UPDATE obligation SET name=?, type=?, amount=?, due_date=?, start_date=?, monthly_payment=?, paid_amount=?, description=?, created_at=?, updated_at=? WHERE id = ?",
                self._obligation_to_tuple(obligation)
            )

# DELETE

    def delete_obligation(self, obligation_id: int) -> None:
        with sqlite3.connect(self.db_path) as conn:
            conn.execute(
                "DELETE FROM obligation WHERE id=?",
                (obligation_id, )
            )




