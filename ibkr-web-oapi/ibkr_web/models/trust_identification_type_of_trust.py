from enum import Enum


class TrustIdentificationTypeOfTrust(str, Enum):
    ERISA = "ERISA"
    IRREVOC = "IRREVOC"
    OTHER = "OTHER"
    RETIREMENT = "RETIREMENT"
    REVOCABLE = "REVOCABLE"
    SMSF = "SMSF"
    TESTAMENTARY = "TESTAMENTARY"

    def __str__(self) -> str:
        return str(self.value)
