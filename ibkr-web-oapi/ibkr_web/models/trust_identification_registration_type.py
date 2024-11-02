from enum import Enum


class TrustIdentificationRegistrationType(str, Enum):
    EIN = "EIN"
    NONUS_NATIONALID = "NonUS_NationalId"
    SSN = "SSN"

    def __str__(self) -> str:
        return str(self.value)
