from enum import Enum


class LegalEntityIdentificationFormationType(str, Enum):
    OTHER = "OTHER"
    PRIVATE = "PRIVATE"
    PUBLIC = "PUBLIC"

    def __str__(self) -> str:
        return str(self.value)
