from enum import Enum


class AccountBrokerageServiceCodesItem(str, Enum):
    IBCLEARING = "IBClearing"
    IBEXECUTION = "IBExecution"
    IBPRIME = "IBPrime"

    def __str__(self) -> str:
        return str(self.value)
