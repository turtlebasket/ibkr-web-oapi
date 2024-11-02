from enum import Enum


class IRADecedentGender(str, Enum):
    F = "F"
    FEMALE = "Female"
    M = "M"
    MALE = "Male"

    def __str__(self) -> str:
        return str(self.value)
