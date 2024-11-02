from enum import Enum


class TradingPermissionProduct(str, Enum):
    BONDS = "BONDS"
    FOREX = "FOREX"
    FUTURES = "FUTURES"
    FUTURES_OPTIONS = "FUTURES OPTIONS"
    MUTUAL_FUNDS = "MUTUAL FUNDS"
    OPTIONS = "OPTIONS"
    SINGLE_STOCK_FUTURES = "SINGLE STOCK FUTURES"
    STOCKS = "STOCKS"
    STOCK_OPTIONS = "STOCK OPTIONS"
    WARRANTS = "WARRANTS"

    def __str__(self) -> str:
        return str(self.value)
