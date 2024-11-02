from enum import Enum


class PostGwApiV1InstructionsQueryBodyInstructionType(str, Enum):
    QUERY_RECENT_INSTRUCTIONS = "QUERY_RECENT_INSTRUCTIONS"

    def __str__(self) -> str:
        return str(self.value)
