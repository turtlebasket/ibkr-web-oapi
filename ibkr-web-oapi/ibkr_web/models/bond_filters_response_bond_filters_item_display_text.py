from enum import Enum


class BondFiltersResponseBondFiltersItemDisplayText(str, Enum):
    COUPON = "Coupon"
    CURRENCY = "Currency"
    ISSUE_DATE = "Issue Date"
    MATURITY_DATE = "Maturity Date"

    def __str__(self) -> str:
        return str(self.value)
