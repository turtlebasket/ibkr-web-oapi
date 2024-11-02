from enum import Enum


class AdministratorTypeSuffix(str, Enum):
    I = "I"
    II = "II"
    III = "III"
    IV = "IV"
    JR = "Jr."
    SR = "Sr."
    V = "V"

    def __str__(self) -> str:
        return str(self.value)
