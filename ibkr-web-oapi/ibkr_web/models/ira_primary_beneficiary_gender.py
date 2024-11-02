from enum import Enum


class IRAPrimaryBeneficiaryGender(str, Enum):
    F = "F"
    FEMALE = "Female"
    M = "M"
    MALE = "Male"

    def __str__(self) -> str:
        return str(self.value)
