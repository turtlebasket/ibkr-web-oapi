from typing import Any, Dict, List, Type, TypeVar, Union

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..models.administrator_contact_person_type_suffix import AdministratorContactPersonTypeSuffix
from ..types import UNSET, Unset

T = TypeVar("T", bound="AdministratorContactPersonType")


@_attrs_define
class AdministratorContactPersonType:
    """
    Attributes:
        first_name (Union[Unset, str]):
        middle_initial (Union[Unset, str]):
        last_name (Union[Unset, str]):
        suffix (Union[Unset, AdministratorContactPersonTypeSuffix]):
        phone_number (Union[Unset, str]):
    """

    first_name: Union[Unset, str] = UNSET
    middle_initial: Union[Unset, str] = UNSET
    last_name: Union[Unset, str] = UNSET
    suffix: Union[Unset, AdministratorContactPersonTypeSuffix] = UNSET
    phone_number: Union[Unset, str] = UNSET
    additional_properties: Dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> Dict[str, Any]:
        first_name = self.first_name

        middle_initial = self.middle_initial

        last_name = self.last_name

        suffix: Union[Unset, str] = UNSET
        if not isinstance(self.suffix, Unset):
            suffix = self.suffix.value

        phone_number = self.phone_number

        field_dict: Dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if first_name is not UNSET:
            field_dict["firstName"] = first_name
        if middle_initial is not UNSET:
            field_dict["middleInitial"] = middle_initial
        if last_name is not UNSET:
            field_dict["lastName"] = last_name
        if suffix is not UNSET:
            field_dict["suffix"] = suffix
        if phone_number is not UNSET:
            field_dict["phoneNumber"] = phone_number

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        d = src_dict.copy()
        first_name = d.pop("firstName", UNSET)

        middle_initial = d.pop("middleInitial", UNSET)

        last_name = d.pop("lastName", UNSET)

        _suffix = d.pop("suffix", UNSET)
        suffix: Union[Unset, AdministratorContactPersonTypeSuffix]
        if isinstance(_suffix, Unset):
            suffix = UNSET
        else:
            suffix = AdministratorContactPersonTypeSuffix(_suffix)

        phone_number = d.pop("phoneNumber", UNSET)

        administrator_contact_person_type = cls(
            first_name=first_name,
            middle_initial=middle_initial,
            last_name=last_name,
            suffix=suffix,
            phone_number=phone_number,
        )

        administrator_contact_person_type.additional_properties = d
        return administrator_contact_person_type

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
