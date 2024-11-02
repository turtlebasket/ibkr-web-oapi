from enum import Enum


class PostGwApiV1ExternalAssetTransfersBodyInstructionType(str, Enum):
    COMPLEX_ASSET_TRANSFER = "COMPLEX_ASSET_TRANSFER"
    DWAC = "DWAC"
    EXTERNAL_POSITION_TRANSFER = "EXTERNAL_POSITION_TRANSFER"
    FOP = "FOP"

    def __str__(self) -> str:
        return str(self.value)
