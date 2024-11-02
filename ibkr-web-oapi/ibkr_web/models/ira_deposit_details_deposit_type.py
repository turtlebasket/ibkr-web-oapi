from enum import Enum


class IRADepositDetailsDepositType(str, Enum):
    CONTRIBUTION = "contribution"
    ROLLOVER = "rollover"

    def __str__(self) -> str:
        return str(self.value)
