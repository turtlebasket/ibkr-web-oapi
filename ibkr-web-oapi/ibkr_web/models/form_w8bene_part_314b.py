from enum import Enum


class FormW8BENEPart314B(str, Enum):
    COMPANYMEETSDERIVATIVEBENEFITSTEST = "CompanyMeetsDerivativeBenefitsTest"
    COMPANYMEETSOWNERSHIPANDBASEEROSIONTEST = "CompanyMeetsOwnershipAndBaseErosionTest"
    COMPANYWITHINCOMEACTIVEBUSINESS = "CompanyWithIncomeActiveBusiness"
    FAVORABLEDISCRETIONARYDETERMINATION = "FavorableDiscretionaryDetermination"
    GOVERNMENT = "Government"
    NOLOBARTICLEINTREATY = "NoLobArticleInTreaty"
    OTHER = "Other"
    PUBLICLYTRADEDCORPORATION = "PubliclyTradedCorporation"
    SUBSIDIARYOFAPUBLICLYTRADEDCORPORATION = "SubsidiaryOfAPubliclyTradedCorporation"
    TAXEXEMPTORGANIZATION = "TaxExemptOrganization"
    TAXEXEMPTPENSIONTRUSTORPENSIONFUND = "TaxExemptPensionTrustOrPensionFund"

    def __str__(self) -> str:
        return str(self.value)
