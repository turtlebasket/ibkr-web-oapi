from enum import Enum


class CommissionConfigType(str, Enum):
    COMMODITIES = "Commodities"
    SECURITIES = "Securities"

    def __str__(self) -> str:
        return str(self.value)
