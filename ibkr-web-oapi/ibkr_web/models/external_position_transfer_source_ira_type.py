from enum import Enum


class ExternalPositionTransferSourceIRAType(str, Enum):
    ED = "ED"
    RH = "RH"
    RI = "RI"
    RO = "RO"
    RT = "RT"
    SH = "SH"
    SP = "SP"
    TH = "TH"

    def __str__(self) -> str:
        return str(self.value)
