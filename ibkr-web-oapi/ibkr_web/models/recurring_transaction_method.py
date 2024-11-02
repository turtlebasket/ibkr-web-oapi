from enum import Enum


class RecurringTransactionMethod(str, Enum):
    ACH = "ACH"
    CHECK = "CHECK"
    SKIP_DEPOSIT = "SKIP_DEPOSIT"
    WIRE = "WIRE"

    def __str__(self) -> str:
        return str(self.value)
