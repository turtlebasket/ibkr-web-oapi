from enum import Enum


class FormW8IMYUsTinType(str, Enum):
    EIN = "EIN"
    ITIN = "ITIN"
    QI_EIN = "QI-EIN"
    SSN = "SSN"
    WP_EIN = "WP-EIN"
    WT_EIN = "WT-EIN"

    def __str__(self) -> str:
        return str(self.value)
