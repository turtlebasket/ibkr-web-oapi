from enum import Enum


class DepositNotificationCurrency(str, Enum):
    AED = "AED"
    AUD = "AUD"
    CAD = "CAD"
    CHF = "CHF"
    CNH = "CNH"
    CZK = "CZK"
    DKK = "DKK"
    EUR = "EUR"
    GBP = "GBP"
    HKD = "HKD"
    HUF = "HUF"
    ILS = "ILS"
    JPY = "JPY"
    KRW = "KRW"
    MXN = "MXN"
    NOK = "NOK"
    NZD = "NZD"
    PLN = "PLN"
    RUB = "RUB"
    SAR = "SAR"
    SEK = "SEK"
    SGD = "SGD"
    TRY = "TRY"
    USD = "USD"
    ZAR = "ZAR"

    def __str__(self) -> str:
        return str(self.value)
