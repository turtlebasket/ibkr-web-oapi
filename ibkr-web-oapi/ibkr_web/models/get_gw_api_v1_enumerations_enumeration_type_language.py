from enum import Enum


class GetGwApiV1EnumerationsEnumerationTypeLanguage(str, Enum):
    AR = "ar"
    DE = "de"
    EN = "en"
    ES = "es"
    FR = "fr"
    HE = "he"
    HU = "hu"
    IT = "it"
    JA = "ja"
    NL = "nl"
    PT = "pt"
    RU = "ru"
    ZH_CN = "zh_CN"
    ZH_TW = "zh_TW"

    def __str__(self) -> str:
        return str(self.value)
