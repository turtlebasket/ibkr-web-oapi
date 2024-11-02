from enum import Enum


class SingleWatchlistEntryAssetClass(str, Enum):
    BOND = "BOND"
    CASH = "CASH"
    CRYPTO = "CRYPTO"
    FUND = "FUND"
    FUT = "FUT"
    OPT = "OPT"
    STK = "STK"
    WAR = "WAR"

    def __str__(self) -> str:
        return str(self.value)
