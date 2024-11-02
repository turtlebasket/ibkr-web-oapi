from enum import Enum


class Typecodes(str, Enum):
    BA = "BA"
    CA = "CA"
    CB = "CB"
    CT = "CT"
    DA = "DA"
    DL = "DL"
    EA = "EA"
    M8 = "M8"
    MF = "MF"
    MS = "MS"
    OE = "OE"
    PR = "PR"
    PS = "PS"
    PT = "PT"
    SE = "SE"
    SG = "SG"
    SM = "SM"
    ST = "ST"
    T2 = "T2"
    TD = "TD"
    TI = "TI"
    TO = "TO"
    UA = "UA"

    def __str__(self) -> str:
        return str(self.value)
