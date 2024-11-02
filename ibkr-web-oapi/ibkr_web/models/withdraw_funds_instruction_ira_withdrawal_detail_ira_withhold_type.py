from enum import Enum


class WithdrawFundsInstructionIraWithdrawalDetailIraWithholdType(str, Enum):
    DEATH = "DEATH"
    DIRECT_ROLLOVER = "DIRECT_ROLLOVER"
    EARLY = "EARLY"
    EXCESS_CY = "EXCESS_CY"
    EXCESS_PY = "EXCESS_PY"
    EXCESS_SC = "EXCESS_SC"
    NORMAL = "NORMAL"
    ROTH_DISTRIBUTION = "ROTH_DISTRIBUTION"

    def __str__(self) -> str:
        return str(self.value)
