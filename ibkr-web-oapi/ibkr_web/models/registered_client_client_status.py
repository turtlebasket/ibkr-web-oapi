from enum import Enum


class RegisteredClientClientStatus(str, Enum):
    ACTIVE = "ACTIVE"
    REQUESTED = "REQUESTED"
    REVOKED = "REVOKED"
    UNKNOWN = "UNKNOWN"

    def __str__(self) -> str:
        return str(self.value)
