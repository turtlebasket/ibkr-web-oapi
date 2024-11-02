from enum import Enum


class TradingPermissionCountry(str, Enum):
    ALL = "ALL"
    AUSTRALIA = "AUSTRALIA"
    AUSTRIA = "AUSTRIA"
    BELGIUM = "BELGIUM"
    CANADA = "CANADA"
    FRANCE = "FRANCE"
    GERMANY = "GERMANY"
    HK_CHINA = "HK-CHINA"
    HONG_KONG = "HONG KONG"
    ITALY = "ITALY"
    JAPAN = "JAPAN"
    KOREA = "KOREA"
    MEXICO = "MEXICO"
    NORWAY = "NORWAY"
    SINGAPORE = "SINGAPORE"
    SPAIN = "SPAIN"
    SWEDEN = "SWEDEN"
    SWITZERLAND = "SWITZERLAND"
    THE_NETHERLANDS = "THE NETHERLANDS"
    UNITED_KINGDOM = "UNITED KINGDOM"
    UNITED_STATES = "UNITED STATES"

    def __str__(self) -> str:
        return str(self.value)
