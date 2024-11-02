from enum import Enum


class DepositFundsInstructionIraDepositDetailIraContributionType(str, Enum):
    CONTRIBUTION = "CONTRIBUTION"
    DIRECT_ROLLOVER = "DIRECT_ROLLOVER"
    EMPLOYER_SEP_CONTRIBUTION = "EMPLOYER_SEP_CONTRIBUTION"
    LATE_ROLLOVER = "LATE_ROLLOVER"
    ROLLOVER = "ROLLOVER"
    SPOUSAL_CONTRIBUTION = "SPOUSAL_CONTRIBUTION"

    def __str__(self) -> str:
        return str(self.value)
