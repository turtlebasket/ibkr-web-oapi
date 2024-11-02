from enum import Enum


class PostGwApiV1AccountsCloseBodyInstructionType(str, Enum):
    ACCOUNT_CLOSE = "ACCOUNT_CLOSE"

    def __str__(self) -> str:
        return str(self.value)
