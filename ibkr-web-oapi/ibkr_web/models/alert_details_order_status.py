from enum import Enum


class AlertDetailsOrderStatus(str, Enum):
    PRESUBMITTED = "Presubmitted"
    SUBMITTED = "Submitted"

    def __str__(self) -> str:
        return str(self.value)
