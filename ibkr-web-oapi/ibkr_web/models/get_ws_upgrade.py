from enum import Enum


class GetWsUpgrade(str, Enum):
    WEBSOCKET = "websocket"

    def __str__(self) -> str:
        return str(self.value)
