from typing import Any, Dict, List, Type, TypeVar, Union

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..models.tax_residency_tin_type import TaxResidencyTinType
from ..types import UNSET, Unset

T = TypeVar("T", bound="TaxResidency")


@_attrs_define
class TaxResidency:
    """
    Attributes:
        country (Union[Unset, str]):
        tin (Union[Unset, str]):
        tin_type (Union[Unset, TaxResidencyTinType]):
    """

    country: Union[Unset, str] = UNSET
    tin: Union[Unset, str] = UNSET
    tin_type: Union[Unset, TaxResidencyTinType] = UNSET
    additional_properties: Dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> Dict[str, Any]:
        country = self.country

        tin = self.tin

        tin_type: Union[Unset, str] = UNSET
        if not isinstance(self.tin_type, Unset):
            tin_type = self.tin_type.value

        field_dict: Dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if country is not UNSET:
            field_dict["country"] = country
        if tin is not UNSET:
            field_dict["tin"] = tin
        if tin_type is not UNSET:
            field_dict["tinType"] = tin_type

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        d = src_dict.copy()
        country = d.pop("country", UNSET)

        tin = d.pop("tin", UNSET)

        _tin_type = d.pop("tinType", UNSET)
        tin_type: Union[Unset, TaxResidencyTinType]
        if isinstance(_tin_type, Unset):
            tin_type = UNSET
        else:
            tin_type = TaxResidencyTinType(_tin_type)

        tax_residency = cls(
            country=country,
            tin=tin,
            tin_type=tin_type,
        )

        tax_residency.additional_properties = d
        return tax_residency

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
