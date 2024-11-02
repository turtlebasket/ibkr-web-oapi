from enum import Enum


class IRADecedentRelationship(str, Enum):
    INDIVIDUAL = "Individual"
    OTHER = "Other"
    SPOUSE = "Spouse"
    TRUST = "Trust"

    def __str__(self) -> str:
        return str(self.value)
