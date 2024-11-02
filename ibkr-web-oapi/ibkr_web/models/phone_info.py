from typing import Any, Dict, List, Type, TypeVar, Union

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..models.phone_info_type import PhoneInfoType
from ..types import UNSET, Unset

T = TypeVar("T", bound="PhoneInfo")


@_attrs_define
class PhoneInfo:
    """
    Attributes:
        type (Union[Unset, PhoneInfoType]):
        number (Union[Unset, str]):
        country (Union[Unset, str]):
        verified (Union[Unset, bool]):
    """

    type: Union[Unset, PhoneInfoType] = UNSET
    number: Union[Unset, str] = UNSET
    country: Union[Unset, str] = UNSET
    verified: Union[Unset, bool] = UNSET
    additional_properties: Dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> Dict[str, Any]:
        type: Union[Unset, str] = UNSET
        if not isinstance(self.type, Unset):
            type = self.type.value

        number = self.number

        country = self.country

        verified = self.verified

        field_dict: Dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if type is not UNSET:
            field_dict["type"] = type
        if number is not UNSET:
            field_dict["number"] = number
        if country is not UNSET:
            field_dict["country"] = country
        if verified is not UNSET:
            field_dict["verified"] = verified

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        d = src_dict.copy()
        _type = d.pop("type", UNSET)
        type: Union[Unset, PhoneInfoType]
        if isinstance(_type, Unset):
            type = UNSET
        else:
            type = PhoneInfoType(_type)

        number = d.pop("number", UNSET)

        country = d.pop("country", UNSET)

        verified = d.pop("verified", UNSET)

        phone_info = cls(
            type=type,
            number=number,
            country=country,
            verified=verified,
        )

        phone_info.additional_properties = d
        return phone_info

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
