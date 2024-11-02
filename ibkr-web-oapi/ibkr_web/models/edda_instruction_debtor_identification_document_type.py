from enum import Enum


class EddaInstructionDebtorIdentificationDocumentType(str, Enum):
    CHINAID = "chinaId"
    HKID = "hkId"
    PASSPORT = "passport"

    def __str__(self) -> str:
        return str(self.value)
