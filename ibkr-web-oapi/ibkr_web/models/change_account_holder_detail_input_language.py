from enum import Enum


class ChangeAccountHolderDetailInputLanguage(str, Enum):
    AR_AE = "ar-AE"
    DE = "de"
    EN = "en"
    ES = "es"
    FR = "fr"
    HE_IL = "he-IL"
    HU = "hu"
    IT = "it"
    JA = "ja"
    PT = "pt"
    RU = "ru"
    ZH_HANS = "zh-Hans"

    def __str__(self) -> str:
        return str(self.value)
