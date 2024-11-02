from enum import Enum


class DVPInstructionRole(str, Enum):
    B = "B"
    C = "C"
    E = "E"

    def __str__(self) -> str:
        return str(self.value)
