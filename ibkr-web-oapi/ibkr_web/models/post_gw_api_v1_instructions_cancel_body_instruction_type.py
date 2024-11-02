from enum import Enum


class PostGwApiV1InstructionsCancelBodyInstructionType(str, Enum):
    CANCEL_INSTRUCTION = "CANCEL_INSTRUCTION"

    def __str__(self) -> str:
        return str(self.value)
