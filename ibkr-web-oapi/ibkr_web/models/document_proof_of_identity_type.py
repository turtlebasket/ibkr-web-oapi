from enum import Enum


class DocumentProofOfIdentityType(str, Enum):
    ALIEN_ID_CARD = "Alien ID Card"
    BANK_STATEMENT = "Bank Statement"
    BROKERAGE_STATEMENT = "Brokerage Statement"
    CRA_ASSESSMENT = "CRA Assessment"
    CREDIT_CARD_STATEMENT = "Credit Card Statement"
    DRIVER_LICENSE = "Driver License"
    EVIDENCE_OF_OWNERSHIP_OF_PROPERTY = "Evidence of Ownership of Property"
    NATIONAL_ID_CARD = "National ID Card"
    PASSPORT = "Passport"
    T4_STATEMENT = "T4 Statement"
    UTILITY_BILL = "Utility Bill"

    def __str__(self) -> str:
        return str(self.value)
