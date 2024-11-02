from enum import Enum


class IRAPrimaryBeneficiaryEntityEntityType(str, Enum):
    CHARITY = "Charity"
    ESTATE = "Estate"
    TRUST = "Trust"

    def __str__(self) -> str:
        return str(self.value)
