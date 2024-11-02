from enum import Enum


class OrganizationApplicantTypeOfTrading(str, Enum):
    CUSTOMER = "CUSTOMER"
    FIRM = "FIRM"

    def __str__(self) -> str:
        return str(self.value)
