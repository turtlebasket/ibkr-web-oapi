from enum import Enum


class FormCRSOecdStatus(str, Enum):
    CUSTODIAL_INSTITUTION = "CUSTODIAL_INSTITUTION"
    DEPOSITORY_INSTITUTION = "DEPOSITORY_INSTITUTION"
    EXEMPT_RETIREMENT_PLAN = "EXEMPT_RETIREMENT_PLAN"
    FINANCIAL_INSTITUTION = "FINANCIAL_INSTITUTION"
    INVESTMENT_ENTITY_IN_NONPARTICIPATING_JURISDICTION = "INVESTMENT_ENTITY_IN_NONPARTICIPATING_JURISDICTION"
    INVESTMENT_ENTITY_NOT_LISTED = "INVESTMENT_ENTITY_NOT_LISTED"
    NON_REPORTING_FI = "NON_REPORTING_FI"
    NON_REPORTING_FINANCIAL_INSTITUTION = "NON_REPORTING_FINANCIAL_INSTITUTION"
    OTHER_ACTIVE_NON_FINANCIAL_ENTITY = "OTHER_ACTIVE_NON_FINANCIAL_ENTITY"
    OTHER_INVESTMENT_ENTITY = "OTHER_INVESTMENT_ENTITY"
    PASSIVE_NON_FINANCIAL_ENTITY = "PASSIVE_NON_FINANCIAL_ENTITY"
    PUBLICLY_TRADED_CORPORATION_OR_AFFILIATE = "PUBLICLY_TRADED_CORPORATION_OR_AFFILIATE"
    SPECIFIED_INSURANCE_COMPANY = "SPECIFIED_INSURANCE_COMPANY"

    def __str__(self) -> str:
        return str(self.value)
