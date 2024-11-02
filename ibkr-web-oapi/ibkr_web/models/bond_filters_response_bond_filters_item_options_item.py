from typing import Any, Dict, List, Type, TypeVar, Union

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

T = TypeVar("T", bound="BondFiltersResponseBondFiltersItemOptionsItem")


@_attrs_define
class BondFiltersResponseBondFiltersItemOptionsItem:
    """
    Attributes:
        value (str): Returns value directly correlating to the displayText key. This may include exchange, maturity
            date, issue date, coupon, or currency.
        text (Union[Unset, str]): In some instances, a text value will be returned, which indicates the standardized
            value format such as plaintext dates, rather than solely numerical values.
    """

    value: str
    text: Union[Unset, str] = UNSET
    additional_properties: Dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> Dict[str, Any]:
        value = self.value

        text = self.text

        field_dict: Dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "value": value,
            }
        )
        if text is not UNSET:
            field_dict["text"] = text

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        d = src_dict.copy()
        value = d.pop("value")

        text = d.pop("text", UNSET)

        bond_filters_response_bond_filters_item_options_item = cls(
            value=value,
            text=text,
        )

        bond_filters_response_bond_filters_item_options_item.additional_properties = d
        return bond_filters_response_bond_filters_item_options_item

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
