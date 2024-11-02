from enum import Enum


class OrderStatusChildOrderType(str, Enum):
    A = "A"
    B = "B"
    VALUE_0 = "0"

    def __str__(self) -> str:
        return str(self.value)
