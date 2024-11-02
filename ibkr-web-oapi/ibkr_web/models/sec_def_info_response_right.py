from enum import Enum


class SecDefInfoResponseRight(str, Enum):
    C = "C"
    P = "P"

    def __str__(self) -> str:
        return str(self.value)
