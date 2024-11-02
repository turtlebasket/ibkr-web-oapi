from enum import Enum


class LiveOrdersResponseOrdersItemStatus(str, Enum):
    CANCELLED = "Cancelled"
    FILLED = "Filled"
    INACTIVE = "Inactive"
    PENDINGCANCEL = "PendingCancel"
    PENDINGSUBMIT = "PendingSubmit"
    PRESUBMITTED = "PreSubmitted"
    SUBMITTED = "Submitted"
    WARNSTATE = "WarnState"

    def __str__(self) -> str:
        return str(self.value)
