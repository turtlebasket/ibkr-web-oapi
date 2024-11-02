from enum import Enum


class FormW9SignatureType(str, Enum):
    ELECTRONIC = "Electronic"
    PHYSICAL = "Physical"

    def __str__(self) -> str:
        return str(self.value)
