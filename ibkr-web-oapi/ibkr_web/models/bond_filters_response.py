from typing import TYPE_CHECKING, Any, Dict, List, Type, TypeVar, Union

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.bond_filters_response_bond_filters_item import BondFiltersResponseBondFiltersItem


T = TypeVar("T", bound="BondFiltersResponse")


@_attrs_define
class BondFiltersResponse:
    """
    Attributes:
        bond_filters (Union[Unset, List['BondFiltersResponseBondFiltersItem']]): Contains all filters pertaining to the
            given issuerId
    """

    bond_filters: Union[Unset, List["BondFiltersResponseBondFiltersItem"]] = UNSET
    additional_properties: Dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> Dict[str, Any]:
        bond_filters: Union[Unset, List[Dict[str, Any]]] = UNSET
        if not isinstance(self.bond_filters, Unset):
            bond_filters = []
            for bond_filters_item_data in self.bond_filters:
                bond_filters_item = bond_filters_item_data.to_dict()
                bond_filters.append(bond_filters_item)

        field_dict: Dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if bond_filters is not UNSET:
            field_dict["bondFilters"] = bond_filters

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        from ..models.bond_filters_response_bond_filters_item import BondFiltersResponseBondFiltersItem

        d = src_dict.copy()
        bond_filters = []
        _bond_filters = d.pop("bondFilters", UNSET)
        for bond_filters_item_data in _bond_filters or []:
            bond_filters_item = BondFiltersResponseBondFiltersItem.from_dict(bond_filters_item_data)

            bond_filters.append(bond_filters_item)

        bond_filters_response = cls(
            bond_filters=bond_filters,
        )

        bond_filters_response.additional_properties = d
        return bond_filters_response

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
