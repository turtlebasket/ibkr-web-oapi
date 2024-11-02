from enum import Enum


class CommissionScheduleTypePricingStructure(str, Enum):
    FIXED = "FIXED"
    TIERED = "TIERED"

    def __str__(self) -> str:
        return str(self.value)
