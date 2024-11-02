from enum import Enum


class CommissionConfigStyle(str, Enum):
    BUNDLED = "Bundled"
    UNBUNDLED = "Unbundled"

    def __str__(self) -> str:
        return str(self.value)
