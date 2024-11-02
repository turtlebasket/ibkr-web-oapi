from enum import Enum


class IRAContingentBeneficiaryMaritalStatus(str, Enum):
    C = "C"
    D = "D"
    M = "M"
    S = "S"
    W = "W"

    def __str__(self) -> str:
        return str(self.value)
