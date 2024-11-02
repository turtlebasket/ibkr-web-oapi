from enum import Enum


class DVPInstructionTxGroupCode(str, Enum):
    G = "G"
    N = "N"
    R = "R"
    Z = "Z"

    def __str__(self) -> str:
        return str(self.value)
