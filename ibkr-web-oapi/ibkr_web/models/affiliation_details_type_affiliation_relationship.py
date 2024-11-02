from enum import Enum


class AffiliationDetailsTypeAffiliationRelationship(str, Enum):
    CHILD = "Child"
    OTHER = "Other"
    PARENT = "Parent"
    SELF = "Self"
    SPOUSE = "Spouse"

    def __str__(self) -> str:
        return str(self.value)
