from enum import Enum


class IRAPrimaryBeneficiaryEntityRelationship(str, Enum):
    BROTHER = "Brother"
    CHARITY = "Charity"
    CHILD = "Child"
    COMMON_LAW_PARTNER = "Common Law Partner"
    DAUGHTER = "Daughter"
    ESTATE = "Estate"
    FATHER = "Father"
    GRANDCHILD = "Grandchild"
    HUSBAND = "Husband"
    MOTHER = "Mother"
    OTHER = "Other"
    PARENT = "Parent"
    SIBLING = "Sibling"
    SISTER = "Sister"
    SON = "Son"
    SPOUSE = "Spouse"
    TRUST = "Trust"
    WIFE = "Wife"

    def __str__(self) -> str:
        return str(self.value)
