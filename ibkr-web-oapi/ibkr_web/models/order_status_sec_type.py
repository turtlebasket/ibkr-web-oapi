from enum import Enum


class OrderStatusSecType(str, Enum):
    BOND = "BOND"
    CASH = "CASH"
    CRYPTO = "CRYPTO"
    FOP = "FOP"
    FUND = "FUND"
    FUT = "FUT"
    OPT = "OPT"
    STK = "STK"
    WAR = "WAR"

    def __str__(self) -> str:
        return str(self.value)
