from typing import Any, Dict, List, Type, TypeVar, Union

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

T = TypeVar("T", bound="Residence")


@_attrs_define
class Residence:
    """
    Attributes:
        street1 (Union[Unset, str]):
        postal_code (Union[Unset, str]):
        country (Union[Unset, str]):
        city (Union[Unset, str]):
        state (Union[Unset, str]):
    """

    street1: Union[Unset, str] = UNSET
    postal_code: Union[Unset, str] = UNSET
    country: Union[Unset, str] = UNSET
    city: Union[Unset, str] = UNSET
    state: Union[Unset, str] = UNSET
    additional_properties: Dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> Dict[str, Any]:
        street1 = self.street1

        postal_code = self.postal_code

        country = self.country

        city = self.city

        state = self.state

        field_dict: Dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if street1 is not UNSET:
            field_dict["street1"] = street1
        if postal_code is not UNSET:
            field_dict["postalCode"] = postal_code
        if country is not UNSET:
            field_dict["country"] = country
        if city is not UNSET:
            field_dict["city"] = city
        if state is not UNSET:
            field_dict["state"] = state

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        d = src_dict.copy()
        street1 = d.pop("street1", UNSET)

        postal_code = d.pop("postalCode", UNSET)

        country = d.pop("country", UNSET)

        city = d.pop("city", UNSET)

        state = d.pop("state", UNSET)

        residence = cls(
            street1=street1,
            postal_code=postal_code,
            country=country,
            city=city,
            state=state,
        )

        residence.additional_properties = d
        return residence

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
