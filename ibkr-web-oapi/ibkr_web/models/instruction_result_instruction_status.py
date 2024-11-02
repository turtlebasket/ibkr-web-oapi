from enum import Enum


class InstructionResultInstructionStatus(str, Enum):
    PENDING = "PENDING"
    PROCESSED = "PROCESSED"

    def __str__(self) -> str:
        return str(self.value)
