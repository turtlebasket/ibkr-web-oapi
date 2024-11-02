from enum import Enum


class AccountStatusRequestStatus(str, Enum):
    A = "A"
    C = "C"
    E = "E"
    F = "F"
    I = "I"
    J = "J"
    L = "L"
    M = "M"
    N = "N"
    O = "O"
    P = "P"
    Q = "Q"
    R = "R"
    W = "W"

    def __str__(self) -> str:
        return str(self.value)
