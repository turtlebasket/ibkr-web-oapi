from enum import Enum


class PredefinedDestinationInstructionFinancialInstitutionBranchCodeType(str, Enum):
    BANK_CODE_CAD = "BANK_CODE_CAD"
    BSB_AUD = "BSB_AUD"
    NONE = "NONE"

    def __str__(self) -> str:
        return str(self.value)
