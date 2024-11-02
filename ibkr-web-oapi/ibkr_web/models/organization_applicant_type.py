from enum import Enum


class OrganizationApplicantType(str, Enum):
    CORPORATION = "CORPORATION"
    LLC = "LLC"
    PARTNERSHIP = "PARTNERSHIP"
    UNINCORPORATED_BUSINESS = "UNINCORPORATED BUSINESS"

    def __str__(self) -> str:
        return str(self.value)
