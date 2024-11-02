from enum import Enum


class ACHInstructionType(str, Enum):
    CREDIT = "CREDIT"
    DEBIT = "DEBIT"
    DEBIT_CREDIT = "DEBIT_CREDIT"

    def __str__(self) -> str:
        return str(self.value)
