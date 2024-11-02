from enum import Enum


class FormCRSControllingPersonDesignation(str, Enum):
    BY_OTHER_MEANS = "BY_OTHER_MEANS"
    BY_OWNERSHIP = "BY_OWNERSHIP"
    SENIOR_MGMT_OFFICER = "SENIOR_MGMT_OFFICER"

    def __str__(self) -> str:
        return str(self.value)
