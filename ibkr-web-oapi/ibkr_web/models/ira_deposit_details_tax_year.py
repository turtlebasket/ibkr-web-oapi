from enum import Enum


class IRADepositDetailsTaxYear(str, Enum):
    CURRENT = "current"
    PRIOR = "prior"

    def __str__(self) -> str:
        return str(self.value)
