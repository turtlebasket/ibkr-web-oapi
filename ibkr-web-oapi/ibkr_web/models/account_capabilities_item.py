from enum import Enum


class AccountCapabilitiesItem(str, Enum):
    BOND = "BOND"
    CFD = "CFD"
    CLP = "CLP"
    CMDTY = "CMDTY"
    FOP = "FOP"
    FUND = "FUND"
    FUT = "FUT"
    LEVFX = "LEVFX"
    MRGN = "MRGN"
    MULT = "MULT"
    OPT = "OPT"
    SSF = "SSF"
    STK = "STK"

    def __str__(self) -> str:
        return str(self.value)
