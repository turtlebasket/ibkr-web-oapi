from typing import Any, Dict, List, Type, TypeVar, Union

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

T = TypeVar("T", bound="RestrictionInfo")


@_attrs_define
class RestrictionInfo:
    """
    Attributes:
        id (Union[Unset, int]):
        by_ib (Union[Unset, bool]):
        name (Union[Unset, str]):
    """

    id: Union[Unset, int] = UNSET
    by_ib: Union[Unset, bool] = UNSET
    name: Union[Unset, str] = UNSET
    additional_properties: Dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> Dict[str, Any]:
        id = self.id

        by_ib = self.by_ib

        name = self.name

        field_dict: Dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if id is not UNSET:
            field_dict["id"] = id
        if by_ib is not UNSET:
            field_dict["byIB"] = by_ib
        if name is not UNSET:
            field_dict["name"] = name

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        d = src_dict.copy()
        id = d.pop("id", UNSET)

        by_ib = d.pop("byIB", UNSET)

        name = d.pop("name", UNSET)

        restriction_info = cls(
            id=id,
            by_ib=by_ib,
            name=name,
        )

        restriction_info.additional_properties = d
        return restriction_info

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
