from enum import Enum


class EligibleContractParticipantDetailsCode(str, Enum):
    DISCRETIONARYBASIS = "DiscretionaryBasis"
    HIGHRISK = "HighRisk"

    def __str__(self) -> str:
        return str(self.value)
