from enum import Enum


class QualifiedPurchaserDetailsCode(str, Enum):
    DISCRETIONARYBASIS = "DiscretionaryBasis"
    INVESTMENTCOMPANYACT = "InvestmentCompanyAct"

    def __str__(self) -> str:
        return str(self.value)
