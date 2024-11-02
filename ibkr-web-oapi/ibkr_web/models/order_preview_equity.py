from typing import Any, Dict, List, Type, TypeVar, Union

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

T = TypeVar("T", bound="OrderPreviewEquity")


@_attrs_define
class OrderPreviewEquity:
    """Describes the projected change to the account's equity.

    Attributes:
        current (Union[Unset, str]): Current equity.
        change (Union[Unset, str]): Difference between current and projected equity values.
        after (Union[Unset, str]): Projected equity after execution of the order.
    """

    current: Union[Unset, str] = UNSET
    change: Union[Unset, str] = UNSET
    after: Union[Unset, str] = UNSET
    additional_properties: Dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> Dict[str, Any]:
        current = self.current

        change = self.change

        after = self.after

        field_dict: Dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if current is not UNSET:
            field_dict["current"] = current
        if change is not UNSET:
            field_dict["change"] = change
        if after is not UNSET:
            field_dict["after"] = after

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        d = src_dict.copy()
        current = d.pop("current", UNSET)

        change = d.pop("change", UNSET)

        after = d.pop("after", UNSET)

        order_preview_equity = cls(
            current=current,
            change=change,
            after=after,
        )

        order_preview_equity.additional_properties = d
        return order_preview_equity

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
