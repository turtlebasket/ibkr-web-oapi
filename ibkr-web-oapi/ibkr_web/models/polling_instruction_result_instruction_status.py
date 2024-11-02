from enum import Enum


class PollingInstructionResultInstructionStatus(str, Enum):
    PENDING = "PENDING"
    PROCESSED = "PROCESSED"
    REJECTED = "REJECTED"

    def __str__(self) -> str:
        return str(self.value)
