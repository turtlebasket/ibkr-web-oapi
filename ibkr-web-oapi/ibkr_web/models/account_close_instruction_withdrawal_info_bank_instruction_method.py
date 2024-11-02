from enum import Enum


class AccountCloseInstructionWithdrawalInfoBankInstructionMethod(str, Enum):
    ACH = "ACH"
    CHECK = "CHECK"
    WIRE = "WIRE"

    def __str__(self) -> str:
        return str(self.value)
