from enum import Enum


class AchInstructionBankInstructionCode(str, Enum):
    CAACH = "CAACH"
    USACH = "USACH"

    def __str__(self) -> str:
        return str(self.value)
