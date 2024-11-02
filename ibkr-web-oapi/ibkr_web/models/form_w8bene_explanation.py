from enum import Enum


class FormW8BENEExplanation(str, Enum):
    TIN_NOT_DISCLOSED = "TIN_NOT_DISCLOSED"
    TIN_NOT_ISSUED = "TIN_NOT_ISSUED"
    TIN_NOT_REQUIRED = "TIN_NOT_REQUIRED"
    US_TIN = "US_TIN"

    def __str__(self) -> str:
        return str(self.value)
