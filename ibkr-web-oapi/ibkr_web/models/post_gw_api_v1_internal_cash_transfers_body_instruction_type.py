from enum import Enum


class PostGwApiV1InternalCashTransfersBodyInstructionType(str, Enum):
    INTERNAL_CASH_TRANSFER = "INTERNAL_CASH_TRANSFER"

    def __str__(self) -> str:
        return str(self.value)
