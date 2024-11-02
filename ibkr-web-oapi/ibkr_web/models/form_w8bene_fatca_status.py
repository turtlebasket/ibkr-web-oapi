from enum import Enum


class FormW8BENEFatcaStatus(str, Enum):
    ACTIVE_NFFE = "ACTIVE_NFFE"
    AN_501_C_ORGANIZATION = "AN_501_C_ORGANIZATION"
    CERTIFIED_DEEMED_COMPLIANT_FFI = "CERTIFIED_DEEMED_COMPLIANT_FFI"
    CERTIFIED_DEEMED_COMPLIANT_INVESTMENT_ADVISORS = "CERTIFIED_DEEMED_COMPLIANT_INVESTMENT_ADVISORS"
    CERTIFIED_DEEMED_COMPLIANT_LIMITED_LIFE_DEBT = "CERTIFIED_DEEMED_COMPLIANT_LIMITED_LIFE_DEBT"
    CERTIFIED_DEEMED_COMPLIANT_NONREGISTERING_LOCAL_BANK = "CERTIFIED_DEEMED_COMPLIANT_NONREGISTERING_LOCAL_BANK"
    CERTIFIED_DEEMED_COMPLIANT_SPONSORED_VEHICLE = "CERTIFIED_DEEMED_COMPLIANT_SPONSORED_VEHICLE"
    DIRECT_REPORTING_NFFE = "DIRECT_REPORTING_NFFE"
    ENTITY_OWNED_BY_EXEMPT_BENEFICIAL_OWNERS = "ENTITY_OWNED_BY_EXEMPT_BENEFICIAL_OWNERS"
    EXCEPTED_INTER_AFFILIATE_FFI = "EXCEPTED_INTER_AFFILIATE_FFI"
    EXCEPTED_NONFINANCIAL_ENTITY = "EXCEPTED_NONFINANCIAL_ENTITY"
    EXCEPTED_NONFINANCIAL_STARTUP = "EXCEPTED_NONFINANCIAL_STARTUP"
    EXCEPTED_TERRITORY_NFFE = "EXCEPTED_TERRITORY_NFFE"
    EXEMPT_RETIREMENT_PLANS = "EXEMPT_RETIREMENT_PLANS"
    FOREIGN_GOVERNMENT = "FOREIGN_GOVERNMENT"
    INTERNATIONAL_ORGANIZATION = "INTERNATIONAL_ORGANIZATION"
    NONFINANCIAL_GROUP = "NONFINANCIAL_GROUP"
    NONPARTICIPATING_FFI = "NONPARTICIPATING_FFI"
    NONPROFIT_ORGANIZATION = "NONPROFIT_ORGANIZATION"
    NONREPORTING_IGA_FFI = "NONREPORTING_IGA_FFI"
    OWNER_DOCUMENTED_FFI = "OWNER_DOCUMENTED_FFI"
    PARICIPATING_FFI = "PARICIPATING_FFI"
    PASSIVE_NFFE = "PASSIVE_NFFE"
    PUBLICLY_TRADED_NFFE = "PUBLICLY_TRADED_NFFE"
    REGISTERED_DEEMED_COMPLIANT_FFI = "REGISTERED_DEEMED_COMPLIANT_FFI"
    REPORTING_MODEL_1_FFI = "REPORTING_MODEL_1_FFI"
    REPORTING_MODEL_2_FFI = "REPORTING_MODEL_2_FFI"
    RESTRICTED_DISTRIBUTOR = "RESTRICTED_DISTRIBUTOR"
    SPONSORED_DIRECT_REPORTING_NFFE = "SPONSORED_DIRECT_REPORTING_NFFE"
    SPONSORED_FFI = "SPONSORED_FFI"
    TERRITORY_FINANCIAL_INSTITUTION = "TERRITORY_FINANCIAL_INSTITUTION"

    def __str__(self) -> str:
        return str(self.value)