from enum import Enum


class DVPInstructionType(str, Enum):
    CMTA = "CMTA"
    DTCID = "DTCID"
    GUS = "GUS"
    NSCC = "NSCC"
    OCCSSF = "OCCSSF"

    def __str__(self) -> str:
        return str(self.value)
