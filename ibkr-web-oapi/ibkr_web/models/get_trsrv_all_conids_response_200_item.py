from typing import Any, Dict, List, Type, TypeVar, Union

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

T = TypeVar("T", bound="GetTrsrvAllConidsResponse200Item")


@_attrs_define
class GetTrsrvAllConidsResponse200Item:
    """
    Attributes:
        ticker (Union[Unset, str]): The ticker symbol of the contract.
        conid (Union[Unset, int]): The contract identifier of the returned contract.
        exchange (Union[Unset, str]): The primary exchange of the returned contract.
    """

    ticker: Union[Unset, str] = UNSET
    conid: Union[Unset, int] = UNSET
    exchange: Union[Unset, str] = UNSET
    additional_properties: Dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> Dict[str, Any]:
        ticker = self.ticker

        conid = self.conid

        exchange = self.exchange

        field_dict: Dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if ticker is not UNSET:
            field_dict["ticker"] = ticker
        if conid is not UNSET:
            field_dict["conid"] = conid
        if exchange is not UNSET:
            field_dict["exchange"] = exchange

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        d = src_dict.copy()
        ticker = d.pop("ticker", UNSET)

        conid = d.pop("conid", UNSET)

        exchange = d.pop("exchange", UNSET)

        get_trsrv_all_conids_response_200_item = cls(
            ticker=ticker,
            conid=conid,
            exchange=exchange,
        )

        get_trsrv_all_conids_response_200_item.additional_properties = d
        return get_trsrv_all_conids_response_200_item

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
