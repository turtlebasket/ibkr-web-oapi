from enum import Enum


class GetIserverAccountOrdersFilters(str, Enum):
    CANCELLED = "Cancelled"
    FILLED = "Filled"
    INACTIVE = "Inactive"
    PENDINGCANCEL = "PendingCancel"
    PENDINGSUBMIT = "PendingSubmit"
    PRESUBMITTED = "PreSubmitted"
    SORTBYTIME = "SortByTime"
    SUBMITTED = "Submitted"
    WARNSTATE = "WarnState"

    def __str__(self) -> str:
        return str(self.value)
