from typing import TYPE_CHECKING, Any, Dict, List, Type, TypeVar, Union

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..models.bond_filters_response_bond_filters_item_display_text import BondFiltersResponseBondFiltersItemDisplayText
from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.bond_filters_response_bond_filters_item_options_item import (
        BondFiltersResponseBondFiltersItemOptionsItem,
    )


T = TypeVar("T", bound="BondFiltersResponseBondFiltersItem")


@_attrs_define
class BondFiltersResponseBondFiltersItem:
    """
    Attributes:
        display_text (Union[Unset, BondFiltersResponseBondFiltersItemDisplayText]): An identifier used to document
            returned options/values. This can be thought of as a key value.
        column_id (Union[Unset, int]): Used for user interfaces. Internal use only.
        options (Union[Unset, List['BondFiltersResponseBondFiltersItemOptionsItem']]): Contains all objects with values
            corresponding to the parent displayText key.
    """

    display_text: Union[Unset, BondFiltersResponseBondFiltersItemDisplayText] = UNSET
    column_id: Union[Unset, int] = UNSET
    options: Union[Unset, List["BondFiltersResponseBondFiltersItemOptionsItem"]] = UNSET
    additional_properties: Dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> Dict[str, Any]:
        display_text: Union[Unset, str] = UNSET
        if not isinstance(self.display_text, Unset):
            display_text = self.display_text.value

        column_id = self.column_id

        options: Union[Unset, List[Dict[str, Any]]] = UNSET
        if not isinstance(self.options, Unset):
            options = []
            for options_item_data in self.options:
                options_item = options_item_data.to_dict()
                options.append(options_item)

        field_dict: Dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if display_text is not UNSET:
            field_dict["displayText"] = display_text
        if column_id is not UNSET:
            field_dict["columnId"] = column_id
        if options is not UNSET:
            field_dict["options"] = options

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        from ..models.bond_filters_response_bond_filters_item_options_item import (
            BondFiltersResponseBondFiltersItemOptionsItem,
        )

        d = src_dict.copy()
        _display_text = d.pop("displayText", UNSET)
        display_text: Union[Unset, BondFiltersResponseBondFiltersItemDisplayText]
        if isinstance(_display_text, Unset):
            display_text = UNSET
        else:
            display_text = BondFiltersResponseBondFiltersItemDisplayText(_display_text)

        column_id = d.pop("columnId", UNSET)

        options = []
        _options = d.pop("options", UNSET)
        for options_item_data in _options or []:
            options_item = BondFiltersResponseBondFiltersItemOptionsItem.from_dict(options_item_data)

            options.append(options_item)

        bond_filters_response_bond_filters_item = cls(
            display_text=display_text,
            column_id=column_id,
            options=options,
        )

        bond_filters_response_bond_filters_item.additional_properties = d
        return bond_filters_response_bond_filters_item

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
