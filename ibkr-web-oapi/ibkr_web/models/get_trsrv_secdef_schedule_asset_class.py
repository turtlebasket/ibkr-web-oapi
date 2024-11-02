from enum import Enum


class GetTrsrvSecdefScheduleAssetClass(str, Enum):
    BND = "BND"
    CFD = "CFD"
    FND = "FND"
    FUT = "FUT"
    ICS = "ICS"
    OPT = "OPT"
    STK = "STK"
    SWP = "SWP"
    WAR = "WAR"

    def __str__(self) -> str:
        return str(self.value)
