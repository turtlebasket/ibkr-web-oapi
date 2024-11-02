from typing import TYPE_CHECKING, Any, Dict, List, Type, TypeVar, Union

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..models.administrator_type_suffix import AdministratorTypeSuffix
from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.address import Address


T = TypeVar("T", bound="AdministratorType")


@_attrs_define
class AdministratorType:
    """
    Attributes:
        first_name (Union[Unset, str]):
        middle_initial (Union[Unset, str]):
        last_name (Union[Unset, str]):
        suffix (Union[Unset, AdministratorTypeSuffix]):
        address (Union[Unset, Address]):
    """

    first_name: Union[Unset, str] = UNSET
    middle_initial: Union[Unset, str] = UNSET
    last_name: Union[Unset, str] = UNSET
    suffix: Union[Unset, AdministratorTypeSuffix] = UNSET
    address: Union[Unset, "Address"] = UNSET
    additional_properties: Dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> Dict[str, Any]:
        first_name = self.first_name

        middle_initial = self.middle_initial

        last_name = self.last_name

        suffix: Union[Unset, str] = UNSET
        if not isinstance(self.suffix, Unset):
            suffix = self.suffix.value

        address: Union[Unset, Dict[str, Any]] = UNSET
        if not isinstance(self.address, Unset):
            address = self.address.to_dict()

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
        if address is not UNSET:
            field_dict["address"] = address

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        from ..models.address import Address

        d = src_dict.copy()
        first_name = d.pop("firstName", UNSET)

        middle_initial = d.pop("middleInitial", UNSET)

        last_name = d.pop("lastName", UNSET)

        _suffix = d.pop("suffix", UNSET)
        suffix: Union[Unset, AdministratorTypeSuffix]
        if isinstance(_suffix, Unset):
            suffix = UNSET
        else:
            suffix = AdministratorTypeSuffix(_suffix)

        _address = d.pop("address", UNSET)
        address: Union[Unset, Address]
        if isinstance(_address, Unset):
            address = UNSET
        else:
            address = Address.from_dict(_address)

        administrator_type = cls(
            first_name=first_name,
            middle_initial=middle_initial,
            last_name=last_name,
            suffix=suffix,
            address=address,
        )

        administrator_type.additional_properties = d
        return administrator_type

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
