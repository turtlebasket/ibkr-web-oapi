from enum import Enum


class PartialOptionPositionOptionType(str, Enum):
    CALL = "CALL"
    PUT = "PUT"

    def __str__(self) -> str:
        return str(self.value)
