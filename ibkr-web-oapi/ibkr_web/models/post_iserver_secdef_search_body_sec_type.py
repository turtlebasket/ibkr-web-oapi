from enum import Enum


class PostIserverSecdefSearchBodySecType(str, Enum):
    BOND = "BOND"
    IND = "IND"
    STK = "STK"

    def __str__(self) -> str:
        return str(self.value)
