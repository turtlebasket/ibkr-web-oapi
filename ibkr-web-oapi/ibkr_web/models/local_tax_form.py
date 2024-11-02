from typing import Any, Dict, List, Type, TypeVar, Union

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..models.local_tax_form_tax_authority import LocalTaxFormTaxAuthority
from ..types import UNSET, Unset

T = TypeVar("T", bound="LocalTaxForm")


@_attrs_define
class LocalTaxForm:
    """
    Attributes:
        tax_authority (Union[Unset, LocalTaxFormTaxAuthority]):
        qualified (Union[Unset, bool]):
        treaty_country (Union[Unset, str]):
    """

    tax_authority: Union[Unset, LocalTaxFormTaxAuthority] = UNSET
    qualified: Union[Unset, bool] = UNSET
    treaty_country: Union[Unset, str] = UNSET
    additional_properties: Dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> Dict[str, Any]:
        tax_authority: Union[Unset, str] = UNSET
        if not isinstance(self.tax_authority, Unset):
            tax_authority = self.tax_authority.value

        qualified = self.qualified

        treaty_country = self.treaty_country

        field_dict: Dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if tax_authority is not UNSET:
            field_dict["taxAuthority"] = tax_authority
        if qualified is not UNSET:
            field_dict["qualified"] = qualified
        if treaty_country is not UNSET:
            field_dict["treatyCountry"] = treaty_country

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        d = src_dict.copy()
        _tax_authority = d.pop("taxAuthority", UNSET)
        tax_authority: Union[Unset, LocalTaxFormTaxAuthority]
        if isinstance(_tax_authority, Unset):
            tax_authority = UNSET
        else:
            tax_authority = LocalTaxFormTaxAuthority(_tax_authority)

        qualified = d.pop("qualified", UNSET)

        treaty_country = d.pop("treatyCountry", UNSET)

        local_tax_form = cls(
            tax_authority=tax_authority,
            qualified=qualified,
            treaty_country=treaty_country,
        )

        local_tax_form.additional_properties = d
        return local_tax_form

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
