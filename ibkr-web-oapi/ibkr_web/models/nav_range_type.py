from typing import Any, Dict, List, Type, TypeVar, Union

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

T = TypeVar("T", bound="NAVRangeType")


@_attrs_define
class NAVRangeType:
    """
    Attributes:
        min_ (Union[Unset, float]):
        max_ (Union[Unset, float]):
        max_fee (Union[Unset, float]):
    """

    min_: Union[Unset, float] = UNSET
    max_: Union[Unset, float] = UNSET
    max_fee: Union[Unset, float] = UNSET
    additional_properties: Dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> Dict[str, Any]:
        min_ = self.min_

        max_ = self.max_

        max_fee = self.max_fee

        field_dict: Dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if min_ is not UNSET:
            field_dict["min"] = min_
        if max_ is not UNSET:
            field_dict["max"] = max_
        if max_fee is not UNSET:
            field_dict["maxFee"] = max_fee

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        d = src_dict.copy()
        min_ = d.pop("min", UNSET)

        max_ = d.pop("max", UNSET)

        max_fee = d.pop("maxFee", UNSET)

        nav_range_type = cls(
            min_=min_,
            max_=max_,
            max_fee=max_fee,
        )

        nav_range_type.additional_properties = d
        return nav_range_type

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
