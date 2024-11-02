from enum import Enum


class AccountInvestmentObjectivesItem(str, Enum):
    GROWTH = "Growth"
    HEDGING = "Hedging"
    INCOME = "Income"
    PRESERVATION = "Preservation"
    SPECULATION = "Speculation"
    TRADING = "Trading"

    def __str__(self) -> str:
        return str(self.value)
