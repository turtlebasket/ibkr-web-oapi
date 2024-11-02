from enum import Enum


class IRAContingentBeneficiaryGender(str, Enum):
    F = "F"
    FEMALE = "Female"
    M = "M"
    MALE = "Male"

    def __str__(self) -> str:
        return str(self.value)
