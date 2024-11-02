from enum import Enum


class DwacInstructionDirection(str, Enum):
    IN = "IN"
    OUT = "OUT"

    def __str__(self) -> str:
        return str(self.value)
