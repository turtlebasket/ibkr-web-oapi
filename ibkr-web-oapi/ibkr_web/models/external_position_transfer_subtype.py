from enum import Enum


class ExternalPositionTransferSubtype(str, Enum):
    ACATS = "ACATS"
    ATON = "ATON"

    def __str__(self) -> str:
        return str(self.value)
