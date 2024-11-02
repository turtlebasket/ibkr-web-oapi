from enum import Enum


class GetIserverAccountAlertAlertIdType(str, Enum):
    Q = "Q"

    def __str__(self) -> str:
        return str(self.value)
