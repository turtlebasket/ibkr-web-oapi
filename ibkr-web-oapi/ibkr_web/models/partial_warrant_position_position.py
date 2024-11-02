from enum import Enum


class PartialWarrantPositionPosition(str, Enum):
    LONG = "LONG"
    SHORT = "SHORT"

    def __str__(self) -> str:
        return str(self.value)
