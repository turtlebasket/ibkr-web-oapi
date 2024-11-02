from enum import Enum


class PostGwApiV1ExternalCashTransfersBodyInstructionType(str, Enum):
    DEPOSIT = "DEPOSIT"
    WITHDRAWAL = "WITHDRAWAL"

    def __str__(self) -> str:
        return str(self.value)
