from enum import Enum


class TraditionalBankInstructionVerificationBankInstructionCode(str, Enum):
    ACHUS = "ACHUS"
    CAACH = "CAACH"
    USACH = "USACH"
    WIRE = "WIRE"

    def __str__(self) -> str:
        return str(self.value)
