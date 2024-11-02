from typing import Any, Dict, List, Type, TypeVar, Union

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

T = TypeVar("T", bound="DisclaimerInfo")


@_attrs_define
class DisclaimerInfo:
    """
    Attributes:
        fc (Union[Unset, str]): Returns the Typecode for the given disclaimer.
        dt (Union[Unset, str]): Returns the Disclaimer message.
    """

    fc: Union[Unset, str] = UNSET
    dt: Union[Unset, str] = UNSET
    additional_properties: Dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> Dict[str, Any]:
        fc = self.fc

        dt = self.dt

        field_dict: Dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if fc is not UNSET:
            field_dict["FC"] = fc
        if dt is not UNSET:
            field_dict["DT"] = dt

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        d = src_dict.copy()
        fc = d.pop("FC", UNSET)

        dt = d.pop("DT", UNSET)

        disclaimer_info = cls(
            fc=fc,
            dt=dt,
        )

        disclaimer_info.additional_properties = d
        return disclaimer_info

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
