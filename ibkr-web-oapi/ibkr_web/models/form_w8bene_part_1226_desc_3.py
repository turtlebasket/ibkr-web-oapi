from enum import Enum


class FormW8BENEPart1226Desc3(str, Enum):
    COLLECTIVEINVESTMENTVEHICLE = "CollectiveInvestmentVehicle"
    EXEMPTBENEFICIALOWNER_RETIREMENTPLAN = "ExemptBeneficialOwner-RetirementPlan"
    FINANCIALINSTITUTIONWITHLOCALCLIENTBASE = "FinancialInstitutionwithlocalClientBase"
    INVESTMENTADVISORSANDMANAGERS = "InvestmentAdvisorsandManagers"
    LOCALBANK = "LocalBank"
    SPONSOREDCLOSELYHELDINVESTMENTVEHICLE = "SponsoredCloselyHeldInvestmentVehicle"
    SPONSOREDINVESTMENTENTITY = "SponsoredInvestmentEntity"
    TRUSTEEDOCUMENTEDTRUST = "TrusteeDocumentedTrust"

    def __str__(self) -> str:
        return str(self.value)
