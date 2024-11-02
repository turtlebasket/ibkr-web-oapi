from enum import Enum


class PartialWarrantPositionOptionType(str, Enum):
    CALL = "CALL"
    PUT = "PUT"

    def __str__(self) -> str:
        return str(self.value)
