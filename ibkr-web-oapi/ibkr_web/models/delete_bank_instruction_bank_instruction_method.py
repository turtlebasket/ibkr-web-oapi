from enum import Enum


class DeleteBankInstructionBankInstructionMethod(str, Enum):
    ACH = "ACH"
    WIRE = "WIRE"

    def __str__(self) -> str:
        return str(self.value)
