from typing import Any, Dict, List, Type, TypeVar, Union

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

T = TypeVar("T", bound="PartialBondPosition")


@_attrs_define
class PartialBondPosition:
    """
    Attributes:
        cusip_number (Union[Unset, str]):
        number_of_bonds (Union[Unset, int]):
        all_ (Union[Unset, bool]):
    """

    cusip_number: Union[Unset, str] = UNSET
    number_of_bonds: Union[Unset, int] = UNSET
    all_: Union[Unset, bool] = UNSET
    additional_properties: Dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> Dict[str, Any]:
        cusip_number = self.cusip_number

        number_of_bonds = self.number_of_bonds

        all_ = self.all_

        field_dict: Dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if cusip_number is not UNSET:
            field_dict["cusipNumber"] = cusip_number
        if number_of_bonds is not UNSET:
            field_dict["numberOfBonds"] = number_of_bonds
        if all_ is not UNSET:
            field_dict["all"] = all_

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        d = src_dict.copy()
        cusip_number = d.pop("cusipNumber", UNSET)

        number_of_bonds = d.pop("numberOfBonds", UNSET)

        all_ = d.pop("all", UNSET)

        partial_bond_position = cls(
            cusip_number=cusip_number,
            number_of_bonds=number_of_bonds,
            all_=all_,
        )

        partial_bond_position.additional_properties = d
        return partial_bond_position

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
