from typing import Any, Dict, List, Type, TypeVar, Union

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

T = TypeVar("T", bound="CurrencyPairsAdditionalPropertyItem")


@_attrs_define
class CurrencyPairsAdditionalPropertyItem:
    """
    Attributes:
        symbol (Union[Unset, str]): The official symbol of the given currency pair.
        conid (Union[Unset, int]): The official contract identifier of the given currency pair.
        ccy_pair (Union[Unset, int]): Returns the symbol counterpart.
    """

    symbol: Union[Unset, str] = UNSET
    conid: Union[Unset, int] = UNSET
    ccy_pair: Union[Unset, int] = UNSET
    additional_properties: Dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> Dict[str, Any]:
        symbol = self.symbol

        conid = self.conid

        ccy_pair = self.ccy_pair

        field_dict: Dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if symbol is not UNSET:
            field_dict["symbol"] = symbol
        if conid is not UNSET:
            field_dict["conid"] = conid
        if ccy_pair is not UNSET:
            field_dict["ccyPair"] = ccy_pair

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        d = src_dict.copy()
        symbol = d.pop("symbol", UNSET)

        conid = d.pop("conid", UNSET)

        ccy_pair = d.pop("ccyPair", UNSET)

        currency_pairs_additional_property_item = cls(
            symbol=symbol,
            conid=conid,
            ccy_pair=ccy_pair,
        )

        currency_pairs_additional_property_item.additional_properties = d
        return currency_pairs_additional_property_item

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
