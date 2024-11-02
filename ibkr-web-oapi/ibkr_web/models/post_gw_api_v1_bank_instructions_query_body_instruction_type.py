from enum import Enum


class PostGwApiV1BankInstructionsQueryBodyInstructionType(str, Enum):
    QUERY_BANK_INSTRUCTION = "QUERY_BANK_INSTRUCTION"
    QUERY_RECENT_RECURRING_EVENTS = "QUERY_RECENT_RECURRING_EVENTS"
    QUERY_RECURRING_INSTRUCTIONS = "QUERY_RECURRING_INSTRUCTIONS"

    def __str__(self) -> str:
        return str(self.value)
