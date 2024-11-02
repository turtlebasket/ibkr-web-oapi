from enum import Enum


class WatchlistDeleteSuccessAction(str, Enum):
    CONTEXT = "context"

    def __str__(self) -> str:
        return str(self.value)
