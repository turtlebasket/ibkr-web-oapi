from enum import Enum


class ComplexAssetTransferInstructionDirection(str, Enum):
    IN = "IN"
    OUT = "OUT"

    def __str__(self) -> str:
        return str(self.value)
