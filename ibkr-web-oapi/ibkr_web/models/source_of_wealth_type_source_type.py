from enum import Enum


class SourceOfWealthTypeSourceType(str, Enum):
    SOW_IND_ALLOWANCE = "SOW-IND-Allowance"
    SOW_IND_DISABILITY = "SOW-IND-Disability"
    SOW_IND_INCOME = "SOW-IND-Income"
    SOW_IND_INHERITANCE = "SOW-IND-Inheritance"
    SOW_IND_INTEREST = "SOW-IND-Interest"
    SOW_IND_MARKETPROFIT = "SOW-IND-MarketProfit"
    SOW_IND_OTHER = "SOW-IND-Other"
    SOW_IND_PENSION = "SOW-IND-Pension"
    SOW_IND_PROPERTY = "SOW-IND-Property"
    SOW_ORG_BUSINESS = "SOW-ORG-Business"
    SOW_ORG_MARKETTRADINGPROFITS = "SOW-ORG-MarketTradingProfits"
    SOW_ORG_OTHER = "SOW-ORG-Other"
    SOW_ORG_OWNEREQUITY = "SOW-ORG-OwnerEquity"
    SOW_ORG_PROPERTY = "SOW-ORG-Property"
    SOW_ORG_RETAINEDEARNINGS = "SOW-ORG-RetainedEarnings"

    def __str__(self) -> str:
        return str(self.value)
