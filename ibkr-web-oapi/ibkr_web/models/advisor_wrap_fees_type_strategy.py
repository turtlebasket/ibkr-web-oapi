from enum import Enum


class AdvisorWrapFeesTypeStrategy(str, Enum):
    AUTOMATED = "AUTOMATED"
    DIRECTBILLING = "DIRECTBILLING"
    NO_FEE = "NO_FEE"

    def __str__(self) -> str:
        return str(self.value)
