from enum import Enum


class ExtPositionsTransferTypeSubType(str, Enum):
    ACATS = "ACATS"
    ATON = "ATON"

    def __str__(self) -> str:
        return str(self.value)
