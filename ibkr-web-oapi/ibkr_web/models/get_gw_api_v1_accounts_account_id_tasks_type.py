from enum import Enum


class GetGwApiV1AccountsAccountIdTasksType(str, Enum):
    PENDING = "pending"
    REGISTRATION = "registration"

    def __str__(self) -> str:
        return str(self.value)
