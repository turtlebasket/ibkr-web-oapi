from typing import Any, Dict, List, Type, TypeVar, Union

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

T = TypeVar("T", bound="IserverScannerRunResponseContractsItem")


@_attrs_define
class IserverScannerRunResponseContractsItem:
    """
    Attributes:
        server_id (Union[Unset, str]): Contract’s index in relation to the market scanner type’s sorting priority.
        column_name (Union[Unset, str]): Always returned for the first contract.
        symbol (Union[Unset, str]): Returns the contract’s ticker symbol.
        conidex (Union[Unset, str]): Returns the contract ID of the contract.
        con_id (Union[Unset, int]): Returns the contract ID of the contract.
        available_chart_periods (Union[Unset, str]): Internal Use Only
        company_name (Union[Unset, str]): Returns the company long name.
        contract_description_1 (Union[Unset, str]): For derivatives like Futures, the local symbol of the contract will
            be returned.
        listing_exchange (Union[Unset, str]): Returns the primary listing exchange of the contract.
        sec_type (Union[Unset, str]): Returns the security type of the contract.
    """

    server_id: Union[Unset, str] = UNSET
    column_name: Union[Unset, str] = UNSET
    symbol: Union[Unset, str] = UNSET
    conidex: Union[Unset, str] = UNSET
    con_id: Union[Unset, int] = UNSET
    available_chart_periods: Union[Unset, str] = UNSET
    company_name: Union[Unset, str] = UNSET
    contract_description_1: Union[Unset, str] = UNSET
    listing_exchange: Union[Unset, str] = UNSET
    sec_type: Union[Unset, str] = UNSET
    additional_properties: Dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> Dict[str, Any]:
        server_id = self.server_id

        column_name = self.column_name

        symbol = self.symbol

        conidex = self.conidex

        con_id = self.con_id

        available_chart_periods = self.available_chart_periods

        company_name = self.company_name

        contract_description_1 = self.contract_description_1

        listing_exchange = self.listing_exchange

        sec_type = self.sec_type

        field_dict: Dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if server_id is not UNSET:
            field_dict["server_id"] = server_id
        if column_name is not UNSET:
            field_dict["column_name"] = column_name
        if symbol is not UNSET:
            field_dict["symbol"] = symbol
        if conidex is not UNSET:
            field_dict["conidex"] = conidex
        if con_id is not UNSET:
            field_dict["con_id"] = con_id
        if available_chart_periods is not UNSET:
            field_dict["available_chart_periods"] = available_chart_periods
        if company_name is not UNSET:
            field_dict["company_name"] = company_name
        if contract_description_1 is not UNSET:
            field_dict["contract_description_1"] = contract_description_1
        if listing_exchange is not UNSET:
            field_dict["listing_exchange"] = listing_exchange
        if sec_type is not UNSET:
            field_dict["sec_type"] = sec_type

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        d = src_dict.copy()
        server_id = d.pop("server_id", UNSET)

        column_name = d.pop("column_name", UNSET)

        symbol = d.pop("symbol", UNSET)

        conidex = d.pop("conidex", UNSET)

        con_id = d.pop("con_id", UNSET)

        available_chart_periods = d.pop("available_chart_periods", UNSET)

        company_name = d.pop("company_name", UNSET)

        contract_description_1 = d.pop("contract_description_1", UNSET)

        listing_exchange = d.pop("listing_exchange", UNSET)

        sec_type = d.pop("sec_type", UNSET)

        iserver_scanner_run_response_contracts_item = cls(
            server_id=server_id,
            column_name=column_name,
            symbol=symbol,
            conidex=conidex,
            con_id=con_id,
            available_chart_periods=available_chart_periods,
            company_name=company_name,
            contract_description_1=contract_description_1,
            listing_exchange=listing_exchange,
            sec_type=sec_type,
        )

        iserver_scanner_run_response_contracts_item.additional_properties = d
        return iserver_scanner_run_response_contracts_item

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
