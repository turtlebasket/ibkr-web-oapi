from typing import Any, Dict, List, Type, TypeVar, Union

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

T = TypeVar("T", bound="AUSExposureDetailsType")


@_attrs_define
class AUSExposureDetailsType:
    """
    Attributes:
        aus_exposure_relationship (Union[Unset, str]):
        person_name (Union[Unset, str]):
        license_number (Union[Unset, int]):
    """

    aus_exposure_relationship: Union[Unset, str] = UNSET
    person_name: Union[Unset, str] = UNSET
    license_number: Union[Unset, int] = UNSET
    additional_properties: Dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> Dict[str, Any]:
        aus_exposure_relationship = self.aus_exposure_relationship

        person_name = self.person_name

        license_number = self.license_number

        field_dict: Dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if aus_exposure_relationship is not UNSET:
            field_dict["ausExposureRelationship"] = aus_exposure_relationship
        if person_name is not UNSET:
            field_dict["personName"] = person_name
        if license_number is not UNSET:
            field_dict["licenseNumber"] = license_number

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        d = src_dict.copy()
        aus_exposure_relationship = d.pop("ausExposureRelationship", UNSET)

        person_name = d.pop("personName", UNSET)

        license_number = d.pop("licenseNumber", UNSET)

        aus_exposure_details_type = cls(
            aus_exposure_relationship=aus_exposure_relationship,
            person_name=person_name,
            license_number=license_number,
        )

        aus_exposure_details_type.additional_properties = d
        return aus_exposure_details_type

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
