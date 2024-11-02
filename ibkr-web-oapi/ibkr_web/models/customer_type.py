from enum import Enum


class CustomerType(str, Enum):
    INDIVIDUAL = "INDIVIDUAL"
    IRA = "IRA"
    JOINT = "JOINT"
    ORG = "ORG"
    TRUST = "TRUST"
    UGMA = "UGMA"
    UTMA = "UTMA"

    def __str__(self) -> str:
        return str(self.value)
