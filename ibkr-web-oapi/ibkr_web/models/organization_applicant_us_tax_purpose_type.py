from enum import Enum


class OrganizationApplicantUsTaxPurposeType(str, Enum):
    C = "C"
    E = "E"
    P = "P"

    def __str__(self) -> str:
        return str(self.value)
