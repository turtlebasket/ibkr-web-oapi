from enum import Enum


class PostGwApiV1InternalAssetTransfersBodyInstructionType(str, Enum):
    INTERNAL_POSITION_TRANSFER = "INTERNAL_POSITION_TRANSFER"

    def __str__(self) -> str:
        return str(self.value)
