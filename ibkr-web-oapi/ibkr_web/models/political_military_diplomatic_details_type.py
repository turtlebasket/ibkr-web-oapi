from typing import Any, Dict, List, Type, TypeVar, Union

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

T = TypeVar("T", bound="PoliticalMilitaryDiplomaticDetailsType")


@_attrs_define
class PoliticalMilitaryDiplomaticDetailsType:
    """
    Attributes:
        person_name (Union[Unset, str]):
        title (Union[Unset, str]):
        organization (Union[Unset, str]):
        country (Union[Unset, str]):
    """

    person_name: Union[Unset, str] = UNSET
    title: Union[Unset, str] = UNSET
    organization: Union[Unset, str] = UNSET
    country: Union[Unset, str] = UNSET
    additional_properties: Dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> Dict[str, Any]:
        person_name = self.person_name

        title = self.title

        organization = self.organization

        country = self.country

        field_dict: Dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if person_name is not UNSET:
            field_dict["personName"] = person_name
        if title is not UNSET:
            field_dict["title"] = title
        if organization is not UNSET:
            field_dict["organization"] = organization
        if country is not UNSET:
            field_dict["country"] = country

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        d = src_dict.copy()
        person_name = d.pop("personName", UNSET)

        title = d.pop("title", UNSET)

        organization = d.pop("organization", UNSET)

        country = d.pop("country", UNSET)

        political_military_diplomatic_details_type = cls(
            person_name=person_name,
            title=title,
            organization=organization,
            country=country,
        )

        political_military_diplomatic_details_type.additional_properties = d
        return political_military_diplomatic_details_type

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
