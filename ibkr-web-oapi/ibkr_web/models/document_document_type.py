from enum import Enum


class DocumentDocumentType(str, Enum):
    ADDITIONAL_PROOF_OF_IDENTITY_DOCUMENT = "Additional Proof of Identity Document"
    ARTICLES_OF_INCORPORATION = "Articles of Incorporation"
    AUTHORIZATION_TO_OPEN_ACCOUNT_CERTIFICATION = "Authorization to Open Account - Certification"
    AUTHORIZATION_TO_OPEN_ACCOUNT_EVIDENCE = "Authorization to Open Account - Evidence"
    BANK_PASSBOOKSTATEMENT = "Bank Passbook/Statement"
    BANK_STATEMENT = "Bank Statement"
    BROKERAGE_STATEMENT = "Brokerage Statement"
    CERTIFICATE_OF_GOOD_STANDING = "Certificate of Good Standing"
    CERTIFICATE_OF_INCORPORATIONFORMATION = "Certificate of Incorporation/Formation"
    CERTIFICATE_OF_REGISTRATIOS = "Certificate of Registratios"
    CERTIFIED_PROOF_OF_ADDRESS = "Certified Proof of Address"
    CERTIFIED_PROOF_OF_IDENTITY = "Certified Proof of Identity"
    CHECK = "Check"
    COMPANY_CHARTER = "Company Charter"
    COMPANY_OWNERSHIP = "Company Ownership"
    COPY_OF_PASSPORT_NATIONAL_ID_OR_DRIVERS_LICENSE = "Copy of Passport, National Id or Driver's License"
    CORPORATE_CHARTER = "Corporate Charter"
    COURT_OR_GOVT_ISSUED_DOCUMENT = "Court- or Govt-issued document"
    CRS_CARD_OF_LOMBARDY = "CRS card of Lombardy"
    CURRENT_LEASE = "Current Lease"
    DIVORCE_SETTLEMENT = "Divorce Settlement"
    EMPLOYER_CONFIRMATION = "Employer Confirmation"
    ENTITLEMENT_TO_PAYMENTS = "Entitlement to Payments"
    EVIDENCE_OF_OWNERSHIP_OF_PROPERTY = "Evidence of Ownership of Property"
    FINANCIAL_STATEMENT = "Financial Statement"
    GOVERNMENT_ISSUED_BUSINESS_LICENSE = "Government-issued Business License"
    INCOME_TAX_RETURN = "Income Tax Return"
    ITALIAN_ELECTRONIC_ID_CARD_CIE = "Italian Electronic ID Card - CIE"
    ITALIAN_HEALTH_CARD_TESSERA_SANITARIA = "Italian Health Card (Tessera Sanitaria)"
    LETTER = "Letter"
    NATIONAL_ID = "National ID"
    OWNERSHIP = "Ownership"
    PASSPORT = "Passport"
    PAY_SLIP = "Pay Slip"
    PROOF_OF_PRINCIPAL_PLACE_OF_BUSINESS_AND_REGISTRATION = "Proof of Principal Place of Business and Registration"
    PROOF_OF_SALE = "Proof of Sale"
    PROOF_OF_WINNINGS = "Proof of Winnings"
    SEVERANCE = "Severance"
    TAX_RETURN = "Tax Return"
    UTILITY_BILL = "Utility Bill"
    WILL = "Will"

    def __str__(self) -> str:
        return str(self.value)
