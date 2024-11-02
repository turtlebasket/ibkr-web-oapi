from enum import Enum


class WatchlistsResponseDataUserListsItemType(str, Enum):
    WATCHLIST = "watchlist"

    def __str__(self) -> str:
        return str(self.value)
