from enum import Enum


class PresetsDefaultMethodForAll(str, Enum):
    AVAILABLEEQUITY = "AvailableEquity"
    C = "C"
    E = "E"
    N = "N"
    P = "P"
    R = "R"
    S = "S"

    def __str__(self) -> str:
        return str(self.value)
