from enum import Enum


class TaskRequestType(str, Enum):
    PENDING = "pending"
    REGISTRATION = "registration"

    def __str__(self) -> str:
        return str(self.value)
