from enum import Enum


class PostGwApiV1FeeTemplatesQueryBodyInstructionType(str, Enum):
    QUERY_FEE_TEMPLATE = "QUERY_FEE_TEMPLATE"

    def __str__(self) -> str:
        return str(self.value)
