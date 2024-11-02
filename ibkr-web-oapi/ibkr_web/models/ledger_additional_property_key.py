from enum import Enum


class LedgerAdditionalPropertyKey(str, Enum):
    LEDGERLIST = "LedgerList"

    def __str__(self) -> str:
        return str(self.value)
