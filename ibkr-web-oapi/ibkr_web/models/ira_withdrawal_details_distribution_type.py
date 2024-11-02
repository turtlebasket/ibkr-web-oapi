from enum import Enum


class IRAWithdrawalDetailsDistributionType(str, Enum):
    DEATH = "DEATH"
    DISABILITY = "DISABILITY"
    EARLY = "EARLY"
    EARLY_EXCEPT = "EARLY_EXCEPT"
    EXCESS_CONTRIB = "EXCESS_CONTRIB"
    NORMAL = "NORMAL"

    def __str__(self) -> str:
        return str(self.value)
