from enum import Enum


class WithholdingStatementTypeFatcaCompliantType(str, Enum):
    FATCA_COMPLIANT = "FATCA_COMPLIANT"
    NON_CONSENTING_US_ACCOUNT = "NON_CONSENTING_US_ACCOUNT"
    NON_COOPERATIVE_ACCOUNT = "NON_COOPERATIVE_ACCOUNT"

    def __str__(self) -> str:
        return str(self.value)
