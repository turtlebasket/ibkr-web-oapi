from enum import Enum


class AllocationMethod(str, Enum):
    A = "A"
    C = "C"
    E = "E"
    N = "N"
    P = "P"
    R = "R"
    S = "S"

    def __str__(self) -> str:
        return str(self.value)
