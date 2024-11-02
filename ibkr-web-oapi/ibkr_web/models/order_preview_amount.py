from typing import Any, Dict, List, Type, TypeVar, Union

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

T = TypeVar("T", bound="OrderPreviewAmount")


@_attrs_define
class OrderPreviewAmount:
    """Describes the projected costs associated with the order ticket.

    Attributes:
        amount (Union[Unset, str]): Projected cost of the order, current reference price times total quantity.
        commission (Union[Unset, str]): Projected commissions and fees associated with the order.
        total (Union[Unset, str]): Sum of projected cost and commission values for the order.
    """

    amount: Union[Unset, str] = UNSET
    commission: Union[Unset, str] = UNSET
    total: Union[Unset, str] = UNSET
    additional_properties: Dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> Dict[str, Any]:
        amount = self.amount

        commission = self.commission

        total = self.total

        field_dict: Dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if amount is not UNSET:
            field_dict["amount"] = amount
        if commission is not UNSET:
            field_dict["commission"] = commission
        if total is not UNSET:
            field_dict["total"] = total

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        d = src_dict.copy()
        amount = d.pop("amount", UNSET)

        commission = d.pop("commission", UNSET)

        total = d.pop("total", UNSET)

        order_preview_amount = cls(
            amount=amount,
            commission=commission,
            total=total,
        )

        order_preview_amount.additional_properties = d
        return order_preview_amount

    @property
    def additional_keys(self) -> List[str]:
        return list(self.additional_properties.keys())

    def __getitem__(self, key: str) -> Any:
        return self.additional_properties[key]

    def __setitem__(self, key: str, value: Any) -> None:
        self.additional_properties[key] = value

    def __delitem__(self, key: str) -> None:
        del self.additional_properties[key]

    def __contains__(self, key: str) -> bool:
        return key in self.additional_properties
