from typing import Any, Dict, List, Type, TypeVar, Union

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

T = TypeVar("T", bound="SecdefSearchResponseItemSectionsItem")


@_attrs_define
class SecdefSearchResponseItemSectionsItem:
    """
    Attributes:
        sec_type (Union[Unset, str]):
        months (Union[Unset, str]): semicolon separated list of months
        exchange (Union[Unset, str]): semicolon separated list of exchanges
    """

    sec_type: Union[Unset, str] = UNSET
    months: Union[Unset, str] = UNSET
    exchange: Union[Unset, str] = UNSET
    additional_properties: Dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> Dict[str, Any]:
        sec_type = self.sec_type

        months = self.months

        exchange = self.exchange

        field_dict: Dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if sec_type is not UNSET:
            field_dict["secType"] = sec_type
        if months is not UNSET:
            field_dict["months"] = months
        if exchange is not UNSET:
            field_dict["exchange"] = exchange

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        d = src_dict.copy()
        sec_type = d.pop("secType", UNSET)

        months = d.pop("months", UNSET)

        exchange = d.pop("exchange", UNSET)

        secdef_search_response_item_sections_item = cls(
            sec_type=sec_type,
            months=months,
            exchange=exchange,
        )

        secdef_search_response_item_sections_item.additional_properties = d
        return secdef_search_response_item_sections_item

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
