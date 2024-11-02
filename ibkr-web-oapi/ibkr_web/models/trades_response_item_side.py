from enum import Enum


class TradesResponseItemSide(str, Enum):
    B = "B"
    S = "S"

    def __str__(self) -> str:
        return str(self.value)
