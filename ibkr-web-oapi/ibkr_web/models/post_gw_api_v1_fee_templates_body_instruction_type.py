from enum import Enum


class PostGwApiV1FeeTemplatesBodyInstructionType(str, Enum):
    APPLY_FEE_TEMPLATE = "APPLY_FEE_TEMPLATE"

    def __str__(self) -> str:
        return str(self.value)
