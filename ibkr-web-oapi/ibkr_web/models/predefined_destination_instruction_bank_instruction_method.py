from enum import Enum


class PredefinedDestinationInstructionBankInstructionMethod(str, Enum):
    ACH = "ACH"
    CPA = "CPA"
    LVP = "LVP"
    SEPA = "SEPA"
    WIRE = "WIRE"

    def __str__(self) -> str:
        return str(self.value)
