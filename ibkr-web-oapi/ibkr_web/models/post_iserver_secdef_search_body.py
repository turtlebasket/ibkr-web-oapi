from typing import Any, Dict, List, Type, TypeVar, Union

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..models.post_iserver_secdef_search_body_sec_type import PostIserverSecdefSearchBodySecType
from ..types import UNSET, Unset

T = TypeVar("T", bound="PostIserverSecdefSearchBody")


@_attrs_define
class PostIserverSecdefSearchBody:
    """
    Attributes:
        symbol (str): The ticker symbol, bond issuer type, or company name of the equity you are looking to trade.
            Example: AAPL.
        sec_type (Union[Unset, PostIserverSecdefSearchBodySecType]): Available underlying security types:
              * `STK` - Represents an underlying as a Stock security type.
              * `IND` - Represents an underlying as an Index security type.
              * `BOND` - Represents an underlying as a Bond security type.
             Default: PostIserverSecdefSearchBodySecType.STK.
        name (Union[Unset, bool]): Denotes if the symbol value is the ticker symbol or part of the company's name.
        more (Union[Unset, bool]):
        fund (Union[Unset, bool]): fund search
        fund_family_conid_ex (Union[Unset, str]):
        pattern (Union[Unset, bool]): pattern search
        referrer (Union[Unset, str]):
    """

    symbol: str
    sec_type: Union[Unset, PostIserverSecdefSearchBodySecType] = PostIserverSecdefSearchBodySecType.STK
    name: Union[Unset, bool] = UNSET
    more: Union[Unset, bool] = UNSET
    fund: Union[Unset, bool] = UNSET
    fund_family_conid_ex: Union[Unset, str] = UNSET
    pattern: Union[Unset, bool] = UNSET
    referrer: Union[Unset, str] = UNSET
    additional_properties: Dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> Dict[str, Any]:
        symbol = self.symbol

        sec_type: Union[Unset, str] = UNSET
        if not isinstance(self.sec_type, Unset):
            sec_type = self.sec_type.value

        name = self.name

        more = self.more

        fund = self.fund

        fund_family_conid_ex = self.fund_family_conid_ex

        pattern = self.pattern

        referrer = self.referrer

        field_dict: Dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "symbol": symbol,
            }
        )
        if sec_type is not UNSET:
            field_dict["secType"] = sec_type
        if name is not UNSET:
            field_dict["name"] = name
        if more is not UNSET:
            field_dict["more"] = more
        if fund is not UNSET:
            field_dict["fund"] = fund
        if fund_family_conid_ex is not UNSET:
            field_dict["fundFamilyConidEx"] = fund_family_conid_ex
        if pattern is not UNSET:
            field_dict["pattern"] = pattern
        if referrer is not UNSET:
            field_dict["referrer"] = referrer

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        d = src_dict.copy()
        symbol = d.pop("symbol")

        _sec_type = d.pop("secType", UNSET)
        sec_type: Union[Unset, PostIserverSecdefSearchBodySecType]
        if isinstance(_sec_type, Unset):
            sec_type = UNSET
        else:
            sec_type = PostIserverSecdefSearchBodySecType(_sec_type)

        name = d.pop("name", UNSET)

        more = d.pop("more", UNSET)

        fund = d.pop("fund", UNSET)

        fund_family_conid_ex = d.pop("fundFamilyConidEx", UNSET)

        pattern = d.pop("pattern", UNSET)

        referrer = d.pop("referrer", UNSET)

        post_iserver_secdef_search_body = cls(
            symbol=symbol,
            sec_type=sec_type,
            name=name,
            more=more,
            fund=fund,
            fund_family_conid_ex=fund_family_conid_ex,
            pattern=pattern,
            referrer=referrer,
        )

        post_iserver_secdef_search_body.additional_properties = d
        return post_iserver_secdef_search_body

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
