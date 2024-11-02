from enum import Enum


class GetHmdsHistoryBarType(str, Enum):
    ASK = "Ask"
    BID = "Bid"
    FEERATE = "FeeRate"
    INVENTORY = "Inventory"
    LAST = "Last"
    MIDPOINT = "Midpoint"

    def __str__(self) -> str:
        return str(self.value)
