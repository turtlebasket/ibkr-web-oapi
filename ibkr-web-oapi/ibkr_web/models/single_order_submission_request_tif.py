from enum import Enum


class SingleOrderSubmissionRequestTif(str, Enum):
    DAY = "DAY"
    GTC = "GTC"
    IOC = "IOC"
    OPG = "OPG"
    PAX = "PAX"

    def __str__(self) -> str:
        return str(self.value)
