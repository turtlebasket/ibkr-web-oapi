from enum import Enum


class DayQuantityLimitAsset(str, Enum):
    BILL = "BILL"
    BOND = "BOND"
    CASH = "CASH"
    CFD = "CFD"
    COMB = "COMB"
    FOP = "FOP"
    FUND = "FUND"
    FUT = "FUT"
    MRGN = "MRGN"
    OPT = "OPT"
    SSF = "SSF"
    STK = "STK"
    WAR = "WAR"

    def __str__(self) -> str:
        return str(self.value)
