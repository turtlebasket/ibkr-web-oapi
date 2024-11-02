from enum import Enum


class TrustApplicantTrustType(str, Enum):
    COMPLEX_TRUST = "COMPLEX_TRUST"
    GRANTOR_TRUST = "GRANTOR_TRUST"
    SINGLE_TRUST = "SINGLE_TRUST"
    US_TAXABLE_TRUST = "US_TAXABLE_TRUST"

    def __str__(self) -> str:
        return str(self.value)
