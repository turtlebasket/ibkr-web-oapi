from enum import Enum


class RecurringTransactionFrequency(str, Enum):
    MONTHLY = "MONTHLY"
    QUARTERLY = "QUARTERLY"
    YEARLY = "YEARLY"

    def __str__(self) -> str:
        return str(self.value)
