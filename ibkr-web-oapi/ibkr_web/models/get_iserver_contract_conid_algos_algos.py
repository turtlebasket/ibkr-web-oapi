from enum import Enum


class GetIserverContractConidAlgosAlgos(str, Enum):
    ADAPTIVE = "Adaptive"
    VWAP = "Vwap"

    def __str__(self) -> str:
        return str(self.value)
