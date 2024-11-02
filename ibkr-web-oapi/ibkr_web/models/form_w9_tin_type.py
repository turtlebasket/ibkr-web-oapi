from enum import Enum


class FormW9TinType(str, Enum):
    EIN = "EIN"
    NONUS_NATIONALID = "NonUS_NationalId"
    SSN = "SSN"

    def __str__(self) -> str:
        return str(self.value)
