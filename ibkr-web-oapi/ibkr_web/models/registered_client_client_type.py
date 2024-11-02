from enum import Enum


class RegisteredClientClientType(str, Enum):
    CONFIDENTIAL = "CONFIDENTIAL"
    PUBLIC = "PUBLIC"
    TEST = "TEST"

    def __str__(self) -> str:
        return str(self.value)
