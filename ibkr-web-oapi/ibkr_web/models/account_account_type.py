from enum import Enum


class AccountAccountType(str, Enum):
    INVESTMENT = "Investment"
    SMSF = "SMSF"
    TRADING = "Trading"

    def __str__(self) -> str:
        return str(self.value)
