from enum import Enum


class FormW9CustomerType(str, Enum):
    CORPORATION = "Corporation"
    INDIVIDUAL = "Individual"
    LLC = "LLC"
    OTHER = "Other"
    PARTNERSHIP = "Partnership"

    def __str__(self) -> str:
        return str(self.value)
