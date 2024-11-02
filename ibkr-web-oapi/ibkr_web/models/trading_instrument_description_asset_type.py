from enum import Enum


class TradingInstrumentDescriptionAssetType(str, Enum):
    CASH = "CASH"
    STK = "STK"
    UNKNOWN = "UNKNOWN"

    def __str__(self) -> str:
        return str(self.value)
