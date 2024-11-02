from enum import Enum


class DocumentProofOfAddressType(str, Enum):
    BANK_STATEMENT = "Bank Statement"
    BROKERAGE_STATEMENT = "Brokerage Statement"
    CURRENT_LEASE = "Current Lease"
    DRIVER_LICENSE = "Driver License"
    EVIDENCE_OF_OWNERSHIP_OF_PROPERTY = "Evidence of Ownership of Property"
    GOVERNMENT_ISSUED_LETTERS = "Government Issued Letters"
    HOMEOWNER_INSURANCE_POLICY_BILL = "Homeowner Insurance Policy Bill"
    HOMEOWNER_INSURANCE_POLICY_DOCUMENT = "Homeowner Insurance Policy Document"
    OTHER_DOCUMENT = "Other Document"
    RENTER_INSURANCE_POLICY_BILL = "Renter Insurance Policy bill"
    RENTER_INSURANCE_POLICY_DOCUMENT = "Renter Insurance Policy Document"
    SECURITY_SYSTEM_BILL = "Security System Bill"
    UTILITY_BILL = "Utility Bill"

    def __str__(self) -> str:
        return str(self.value)
