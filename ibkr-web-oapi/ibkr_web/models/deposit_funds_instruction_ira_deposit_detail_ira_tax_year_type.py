from enum import Enum


class DepositFundsInstructionIraDepositDetailIraTaxYearType(str, Enum):
    CURRENT = "CURRENT"
    PRIOR = "PRIOR"

    def __str__(self) -> str:
        return str(self.value)
