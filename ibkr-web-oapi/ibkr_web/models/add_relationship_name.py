from enum import Enum


class AddRelationshipName(str, Enum):
    ACCOUNTANT = "Accountant"
    ACCOUNT_ADMIN = "Account_Admin"
    ACCOUNT_BILLING = "Account_Billing"
    ACCOUNT_CLEARING = "Account_Clearing"
    ACCOUNT_HOLDER = "Account_Holder"
    ACCOUNT_SALES = "Account_Sales"
    ACCOUNT_TRADING = "Account_Trading"
    ADMINISTRATOR = "Administrator"
    ADVISORY_PRINCIPAL = "Advisory_Principal"
    ADVISORY_SIGNATORY = "Advisory_Signatory"
    APPLY_USER = "Apply_User"
    ASSOCIATED_FUND = "Associated_Fund"
    AS_INTEREST_MAY_APPEAR = "As_Interest_May_Appear"
    AUTHORIZED_PERSON = "Authorized_Person"
    BENEFICIALOWNER = "Beneficialowner"
    BENEFICIARY = "Beneficiary"
    CEO = "Ceo"
    CFTC_APPLICANT_OCR_CONTACT = "Cftc_Applicant_Ocr_Contact"
    CFTC_NON_APPLICANT_OCR_CONTACT = "Cftc_Non_Applicant_Ocr_Contact"
    CHARITY = "Charity"
    CHIEF_COMPLIANCE_OFFICER = "Chief_Compliance_Officer"
    CHIEF_FINANCIAL_OFFICER = "Chief_Financial_Officer"
    CHILD = "Child"
    COMMON_LAW_PARTNER = "Common_Law_Partner"
    COMPLIANCE_CONTACT = "Compliance_Contact"
    COMPLIANCE_OFFICER = "Compliance_Officer"
    COMP_OFFICER = "Comp_Officer"
    CONTACT = "Contact"
    CONTINGENT = "Contingent"
    CONTROLLING_OFFICER = "Controlling_Officer"
    CUSTODIAN = "Custodian"
    CUSTODIAN_EMPLOYEE = "Custodian_Employee"
    DIRECTOR = "Director"
    EMPLOYEE = "Employee"
    ESTATE = "Estate"
    FINANCIAL_USER = "Financial_User"
    FIRM_ADMIN = "Firm_Admin"
    FIRM_BILLING = "Firm_Billing"
    FIRM_CLEARING = "Firm_Clearing"
    FIRM_SALES = "Firm_Sales"
    FIRM_TRADING = "Firm_Trading"
    FIRM_USER = "Firm_User"
    FIRSTHOLDER = "Firstholder"
    FUND_ADMIN = "Fund_Admin"
    FUND_CONTACT = "Fund_Contact"
    FUND_MANAGER = "Fund_Manager"
    GRANDCHILD = "Grandchild"
    GRANTOR = "Grantor"
    HEAD_OF_DESK = "Head_Of_Desk"
    INVESTMENT_ADVISOR = "Investment_Advisor"
    IRA_BENEFICIARY = "Ira_Beneficiary"
    IRA_DECEDENT = "Ira_Decedent"
    IRA_PRESENT_TRUST = "Ira_Present_Trust"
    JOINT_APPLICANT = "Joint_Applicant"
    LEAD_COMPLIANCE_OFFICER = "Lead_Compliance_Officer"
    LIFE_PARTNER = "Life_Partner"
    MM_CONTACT = "Mm_Contact"
    NOMINEE = "Nominee"
    NOMINEE_GUARDIAN = "Nominee_Guardian"
    NOMINEE_OWNER = "Nominee_Owner"
    NON_EMPLOYEE = "Non_Employee"
    OCR_ACCOUNT_CONTROLLER = "Ocr_Account_Controller"
    ORGANIZATION_APPLICANT = "Organization_Applicant"
    OTHER = "Other"
    OTHER_OFFICER = "Other_Officer"
    OWNER = "Owner"
    PARENT = "Parent"
    PARTNER = "Partner"
    PENSION_ADMIN = "Pension_Admin"
    PENSION_ADMIN_CONTACT = "Pension_Admin_Contact"
    PLAN_SPONSOR = "Plan_Sponsor"
    PLAN_SPONSOR_OFFICER = "Plan_Sponsor_Officer"
    POOLED_USER = "Pooled_User"
    PRIMARY_CONTRIBUTOR = "Primary_Contributor"
    PRINCIPAL = "Principal"
    PROMOTER = "Promoter"
    REG_REP = "Reg_Rep"
    SECONDHOLDER = "Secondholder"
    SECRETARY = "Secretary"
    SHAREHOLDER = "Shareholder"
    SHF_INVESTMANAGER = "Shf_Investmanager"
    SIBLING = "Sibling"
    SIGNATORY = "Signatory"
    SPOUSE = "Spouse"
    SUCCESSOR_CUSTODIAN = "Successor_Custodian"
    SUCCESSOR_CUSTODIAN_EMPLOYEE = "Successor_Custodian_Employee"
    SUCCESSOR_HOLDER = "Successor_Holder"
    SUPERV_BROKER = "Superv_Broker"
    THIRD_PARTY_ADMIN = "Third_Party_Admin"
    TOD_CONTINGENT_BENEFICIARY = "Tod_Contingent_Beneficiary"
    TOD_PRIMARY_BENEFICIARY = "Tod_Primary_Beneficiary"
    TRADER = "Trader"
    TRADING_OFFICER = "Trading_Officer"
    TRANSFER_ON_DEATH_LEGATOR = "Transfer_On_Death_Legator"
    TREASURER = "Treasurer"
    TRUSTEE = "Trustee"
    TRUST_APPLICANT = "Trust_Applicant"
    TRUST_CONTROLLER = "Trust_Controller"
    TRUST_IRA = "Trust_Ira"
    USER_INDIVIDUAL = "User_Individual"
    WHOLETIME_DIRECTOR = "Wholetime_Director"

    def __str__(self) -> str:
        return str(self.value)
