from enum import Enum


class IndividualGender(str, Enum):
    F = "F"
    FEMALE = "Female"
    M = "M"
    MALE = "Male"

    def __str__(self) -> str:
        return str(self.value)
