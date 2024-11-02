from enum import Enum


class ProhibitedQuestionnaireDetailCode(str, Enum):
    BIRTH = "BIRTH"
    BUSINESSDEALINGS = "BUSINESSDEALINGS"
    CITIZENSHIP = "CITIZENSHIP"
    FINANCIALACCOUNTS = "FINANCIALACCOUNTS"
    MULTI = "MULTI"
    PASSPORT = "PASSPORT"
    RESIDENT = "RESIDENT"

    def __str__(self) -> str:
        return str(self.value)
