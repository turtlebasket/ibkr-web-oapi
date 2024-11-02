from enum import Enum


class AlgoParamValueClassName(str, Enum):
    BOOLEAN = "Boolean"
    DOUBLE = "Double"
    INTEGER = "Integer"
    STRING = "String"
    TIME = "Time"

    def __str__(self) -> str:
        return str(self.value)
