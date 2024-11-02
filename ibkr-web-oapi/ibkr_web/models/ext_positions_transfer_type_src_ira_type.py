from enum import Enum


class ExtPositionsTransferTypeSrcIRAType(str, Enum):
    ED = "ED"
    ISA = "ISA"
    RH = "RH"
    RI = "RI"
    RO = "RO"
    RRSP = "RRSP"
    RT = "RT"
    SH = "SH"
    SIMPLE = "SIMPLE"
    SP = "SP"
    SRRSP = "SRRSP"
    TFSA = "TFSA"
    TH = "TH"

    def __str__(self) -> str:
        return str(self.value)
