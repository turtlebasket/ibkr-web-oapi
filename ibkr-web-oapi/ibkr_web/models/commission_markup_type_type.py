from enum import Enum


class CommissionMarkupTypeType(str, Enum):
    FA = "FA"
    FM = "FM"
    PM = "PM"

    def __str__(self) -> str:
        return str(self.value)
