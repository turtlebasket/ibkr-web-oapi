from enum import Enum


class SingleOrderSubmissionRequestTrailingType(str, Enum):
    AMT = "amt"
    VALUE_1 = "%"

    def __str__(self) -> str:
        return str(self.value)
