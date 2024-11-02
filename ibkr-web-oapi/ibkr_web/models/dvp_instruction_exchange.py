from enum import Enum


class DVPInstructionExchange(str, Enum):
    AMEX = "AMEX"
    BOX = "BOX"
    CBOE = "CBOE"
    ISE = "ISE"
    NASDAQ = "NASDAQ"
    NYSE = "NYSE"
    PHLX = "PHLX"
    PSE = "PSE"

    def __str__(self) -> str:
        return str(self.value)
