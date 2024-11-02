from enum import Enum


class IdentificationCardColor(str, Enum):
    BLUE = "BLUE"
    GREEN = "GREEN"
    YELLOW = "YELLOW"

    def __str__(self) -> str:
        return str(self.value)
