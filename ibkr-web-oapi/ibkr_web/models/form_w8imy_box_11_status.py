from enum import Enum


class FormW8IMYBox11Status(str, Enum):
    LIMITED_BRANCH = "LIMITED_BRANCH"
    PARTICIPATING_FFI = "PARTICIPATING_FFI"
    REPORTING_MODEL_1_FFI = "REPORTING_MODEL_1_FFI"
    REPORTING_MODEL_2_FFI = "REPORTING_MODEL_2_FFI"
    US_BRANCH = "US_BRANCH"

    def __str__(self) -> str:
        return str(self.value)
