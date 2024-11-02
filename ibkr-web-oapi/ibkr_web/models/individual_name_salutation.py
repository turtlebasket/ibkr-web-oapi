from enum import Enum


class IndividualNameSalutation(str, Enum):
    DR = "Dr."
    IND = "Ind."
    MR = "Mr."
    MRS = "Mrs."
    MS = "Ms."
    MX = "Mx."

    def __str__(self) -> str:
        return str(self.value)
