from typing import Any, Dict, List, Type, TypeVar, Union

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

T = TypeVar("T", bound="PublicCompanyInfoType")


@_attrs_define
class PublicCompanyInfoType:
    """
    Attributes:
        exchange_traded_on (Union[Unset, str]):
        quoted_symbol (Union[Unset, str]):
    """

    exchange_traded_on: Union[Unset, str] = UNSET
    quoted_symbol: Union[Unset, str] = UNSET
    additional_properties: Dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> Dict[str, Any]:
        exchange_traded_on = self.exchange_traded_on

        quoted_symbol = self.quoted_symbol

        field_dict: Dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if exchange_traded_on is not UNSET:
            field_dict["exchangeTradedOn"] = exchange_traded_on
        if quoted_symbol is not UNSET:
            field_dict["quotedSymbol"] = quoted_symbol

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        d = src_dict.copy()
        exchange_traded_on = d.pop("exchangeTradedOn", UNSET)

        quoted_symbol = d.pop("quotedSymbol", UNSET)

        public_company_info_type = cls(
            exchange_traded_on=exchange_traded_on,
            quoted_symbol=quoted_symbol,
        )

        public_company_info_type.additional_properties = d
        return public_company_info_type

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
