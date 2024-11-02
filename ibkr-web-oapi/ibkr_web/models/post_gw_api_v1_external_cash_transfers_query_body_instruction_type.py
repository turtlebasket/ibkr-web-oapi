from enum import Enum


class PostGwApiV1ExternalCashTransfersQueryBodyInstructionType(str, Enum):
    QUERY_IRA_CONTRIBUTIONS = "QUERY_IRA_CONTRIBUTIONS"
    QUERY_WITHDAWABLE_FUNDS = "QUERY_WITHDAWABLE_FUNDS"

    def __str__(self) -> str:
        return str(self.value)
