from enum import Enum


class GetIserverSecdefSearchSecType(str, Enum):
    BOND = "BOND"
    IND = "IND"
    STK = "STK"

    def __str__(self) -> str:
        return str(self.value)
