from enum import Enum


class GetIserverWatchlistsSC(str, Enum):
    USER_WATCHLIST = "USER_WATCHLIST"

    def __str__(self) -> str:
        return str(self.value)
