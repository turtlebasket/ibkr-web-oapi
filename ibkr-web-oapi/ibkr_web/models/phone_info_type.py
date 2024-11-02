from enum import Enum


class PhoneInfoType(str, Enum):
    BUSINESS = "Business"
    FAX = "Fax"
    HOME = "Home"
    MOBILE = "Mobile"
    MOBILE_OTHER = "Mobile (other)"
    MOBILE_WORK = "Mobile (work)"
    OTHER_VOICE = "Other (voice)"
    WORK = "Work"

    def __str__(self) -> str:
        return str(self.value)
