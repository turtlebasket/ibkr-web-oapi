from enum import Enum


class WithdrawFundsInstructionBankInstructionMethod(str, Enum):
    ACH = "ACH"
    CHECK = "CHECK"
    WIRE = "WIRE"

    def __str__(self) -> str:
        return str(self.value)
