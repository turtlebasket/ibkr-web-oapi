from enum import Enum


class TradingInstrumentDescriptionSecurityIdType(str, Enum):
    CASH = "CASH"
    CUSIP = "CUSIP"
    ISIN = "ISIN"

    def __str__(self) -> str:
        return str(self.value)
