from typing import Any, Dict, List, Type, TypeVar, Union

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

T = TypeVar("T", bound="StocksAdditionalPropertyItemContractsItem")


@_attrs_define
class StocksAdditionalPropertyItemContractsItem:
    """
    Attributes:
        conid (Union[Unset, int]): Contract ID for the specific contract.
        exchange (Union[Unset, str]): Primary exchange for the given contract.
        is_us (Union[Unset, bool]): States whether the contract is hosted in the United States or not.
    """

    conid: Union[Unset, int] = UNSET
    exchange: Union[Unset, str] = UNSET
    is_us: Union[Unset, bool] = UNSET
    additional_properties: Dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> Dict[str, Any]:
        conid = self.conid

        exchange = self.exchange

        is_us = self.is_us

        field_dict: Dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if conid is not UNSET:
            field_dict["conid"] = conid
        if exchange is not UNSET:
            field_dict["exchange"] = exchange
        if is_us is not UNSET:
            field_dict["isUS"] = is_us

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        d = src_dict.copy()
        conid = d.pop("conid", UNSET)

        exchange = d.pop("exchange", UNSET)

        is_us = d.pop("isUS", UNSET)

        stocks_additional_property_item_contracts_item = cls(
            conid=conid,
            exchange=exchange,
            is_us=is_us,
        )

        stocks_additional_property_item_contracts_item.additional_properties = d
        return stocks_additional_property_item_contracts_item

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
