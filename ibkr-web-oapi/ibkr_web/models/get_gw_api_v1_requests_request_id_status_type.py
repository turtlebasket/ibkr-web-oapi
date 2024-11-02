from enum import Enum


class GetGwApiV1RequestsRequestIdStatusType(str, Enum):
    RESPONSE = "response"
    UPDATE = "update"

    def __str__(self) -> str:
        return str(self.value)
