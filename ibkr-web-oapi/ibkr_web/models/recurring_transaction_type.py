from enum import Enum


class RecurringTransactionType(str, Enum):
    DEPOSIT = "DEPOSIT"
    WITHDRAWAL = "WITHDRAWAL"

    def __str__(self) -> str:
        return str(self.value)
