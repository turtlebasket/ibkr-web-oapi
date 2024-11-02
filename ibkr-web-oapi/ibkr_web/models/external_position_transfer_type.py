from enum import Enum


class ExternalPositionTransferType(str, Enum):
    FULL = "FULL"

    def __str__(self) -> str:
        return str(self.value)
