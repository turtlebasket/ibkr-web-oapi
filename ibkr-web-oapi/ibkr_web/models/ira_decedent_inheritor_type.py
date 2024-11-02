from enum import Enum


class IRADecedentInheritorType(str, Enum):
    I = "I"
    O = "O"
    S = "S"
    T = "T"

    def __str__(self) -> str:
        return str(self.value)
