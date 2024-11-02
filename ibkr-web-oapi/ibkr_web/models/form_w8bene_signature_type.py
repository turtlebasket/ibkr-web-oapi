from enum import Enum


class FormW8BENESignatureType(str, Enum):
    ELECTRONIC = "Electronic"
    PHYSICAL = "Physical"

    def __str__(self) -> str:
        return str(self.value)
