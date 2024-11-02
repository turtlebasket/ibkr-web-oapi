from enum import Enum


class OrderCancelSuccessMsg(str, Enum):
    REQUEST_WAS_SUBMITTED = "Request was submitted"

    def __str__(self) -> str:
        return str(self.value)
