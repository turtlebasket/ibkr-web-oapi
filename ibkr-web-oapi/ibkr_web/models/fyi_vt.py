from typing import Any, Dict, List, Type, TypeVar, Union

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

T = TypeVar("T", bound="FyiVT")


@_attrs_define
class FyiVT:
    """
    Attributes:
        v (Union[Unset, int]): Returns 1 to state message was acknowledged.
        t (Union[Unset, int]): Returns the time in ms to complete the edit.
    """

    v: Union[Unset, int] = UNSET
    t: Union[Unset, int] = UNSET
    additional_properties: Dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> Dict[str, Any]:
        v = self.v

        t = self.t

        field_dict: Dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if v is not UNSET:
            field_dict["V"] = v
        if t is not UNSET:
            field_dict["T"] = t

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        d = src_dict.copy()
        v = d.pop("V", UNSET)

        t = d.pop("T", UNSET)

        fyi_vt = cls(
            v=v,
            t=t,
        )

        fyi_vt.additional_properties = d
        return fyi_vt

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
