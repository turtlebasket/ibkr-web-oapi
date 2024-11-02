from enum import Enum


class PollingInstructionResultInstructionType(str, Enum):
    ACCOUNT_CLOSE = "ACCOUNT_CLOSE"
    ACH_INSTRUCTION = "ACH_INSTRUCTION"
    APPLY_FEE_TEMPLATE = "APPLY_FEE_TEMPLATE"
    CANCEL_INSTRUCTION = "CANCEL_INSTRUCTION"
    COMPLEX_ASSET_TRANSFER = "COMPLEX_ASSET_TRANSFER"
    DELETE_BANK_INSTRUCTION = "DELETE_BANK_INSTRUCTION"
    DEPOSIT = "DEPOSIT"
    DWAC = "DWAC"
    EXTERNAL_POSITION_TRANSFER = "EXTERNAL_POSITION_TRANSFER"
    FOP = "FOP"
    INTERNAL_CASH_TRANSFER = "INTERNAL_CASH_TRANSFER"
    MICRO_AMOUNT = "MICRO_AMOUNT"
    PREDEFINED_DESTINATION_INSTRUCTION_TRADITIONAL_BANK_INSTRUCTION_VERIFICATION = (
        "PREDEFINED_DESTINATION_INSTRUCTION TRADITIONAL_BANK_INSTRUCTION_VERIFICATION"
    )
    QUERY_RECENT_INSTRUCTIONS = "QUERY_RECENT_INSTRUCTIONS"
    QUERY_WITHDAWABLE_FUNDS_INTERNAL_POSITION_TRANSFER = "QUERY_WITHDAWABLE_FUNDS INTERNAL_POSITION_TRANSFER"
    WITHDRAWAL = "WITHDRAWAL"

    def __str__(self) -> str:
        return str(self.value)
