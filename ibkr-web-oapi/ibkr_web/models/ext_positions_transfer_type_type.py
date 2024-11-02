from enum import Enum


class ExtPositionsTransferTypeType(str, Enum):
    FULL = "FULL"
    PARTIAL = "PARTIAL"

    def __str__(self) -> str:
        return str(self.value)
