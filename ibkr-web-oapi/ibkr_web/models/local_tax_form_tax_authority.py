from enum import Enum


class LocalTaxFormTaxAuthority(str, Enum):
    AUSTRALIA_TA = "AUSTRALIA_TA"
    CANADA_TA = "CANADA_TA"
    ISRAEL_TA = "ISRAEL_TA"
    RUSSIA_TA = "RUSSIA_TA"
    SWEDEN_TA = "SWEDEN_TA"

    def __str__(self) -> str:
        return str(self.value)
