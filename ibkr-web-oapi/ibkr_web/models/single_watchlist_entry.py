from typing import Any, Dict, List, Type, TypeVar, Union

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..models.single_watchlist_entry_asset_class import SingleWatchlistEntryAssetClass
from ..models.single_watchlist_entry_st import SingleWatchlistEntryST
from ..types import UNSET, Unset

T = TypeVar("T", bound="SingleWatchlistEntry")


@_attrs_define
class SingleWatchlistEntry:
    """Object containing watchlist entry for a single instrument.

    Attributes:
        st (Union[Unset, SingleWatchlistEntryST]): All-capital, shorthand security type identifier of the instrument.
        c (Union[Unset, str]): Instrument conid as a string.
        conid (Union[Unset, int]): IB contract ID of the instrument.
        name (Union[Unset, str]): Complete display name of the instrument.
        full_name (Union[Unset, str]): Full display presentation of the instrument symbol.
        asset_class (Union[Unset, SingleWatchlistEntryAssetClass]): All-capital, shorthand security type identifier of
            the instrument.
        ticker (Union[Unset, str]): Symbol of the instrument.
        chinese_name (Union[Unset, str]): Rendering of the instrument name in Chinese.
    """

    st: Union[Unset, SingleWatchlistEntryST] = UNSET
    c: Union[Unset, str] = UNSET
    conid: Union[Unset, int] = UNSET
    name: Union[Unset, str] = UNSET
    full_name: Union[Unset, str] = UNSET
    asset_class: Union[Unset, SingleWatchlistEntryAssetClass] = UNSET
    ticker: Union[Unset, str] = UNSET
    chinese_name: Union[Unset, str] = UNSET
    additional_properties: Dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> Dict[str, Any]:
        st: Union[Unset, str] = UNSET
        if not isinstance(self.st, Unset):
            st = self.st.value

        c = self.c

        conid = self.conid

        name = self.name

        full_name = self.full_name

        asset_class: Union[Unset, str] = UNSET
        if not isinstance(self.asset_class, Unset):
            asset_class = self.asset_class.value

        ticker = self.ticker

        chinese_name = self.chinese_name

        field_dict: Dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if st is not UNSET:
            field_dict["ST"] = st
        if c is not UNSET:
            field_dict["C"] = c
        if conid is not UNSET:
            field_dict["conid"] = conid
        if name is not UNSET:
            field_dict["name"] = name
        if full_name is not UNSET:
            field_dict["fullName"] = full_name
        if asset_class is not UNSET:
            field_dict["assetClass"] = asset_class
        if ticker is not UNSET:
            field_dict["ticker"] = ticker
        if chinese_name is not UNSET:
            field_dict["chineseName"] = chinese_name

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        d = src_dict.copy()
        _st = d.pop("ST", UNSET)
        st: Union[Unset, SingleWatchlistEntryST]
        if isinstance(_st, Unset):
            st = UNSET
        else:
            st = SingleWatchlistEntryST(_st)

        c = d.pop("C", UNSET)

        conid = d.pop("conid", UNSET)

        name = d.pop("name", UNSET)

        full_name = d.pop("fullName", UNSET)

        _asset_class = d.pop("assetClass", UNSET)
        asset_class: Union[Unset, SingleWatchlistEntryAssetClass]
        if isinstance(_asset_class, Unset):
            asset_class = UNSET
        else:
            asset_class = SingleWatchlistEntryAssetClass(_asset_class)

        ticker = d.pop("ticker", UNSET)

        chinese_name = d.pop("chineseName", UNSET)

        single_watchlist_entry = cls(
            st=st,
            c=c,
            conid=conid,
            name=name,
            full_name=full_name,
            asset_class=asset_class,
            ticker=ticker,
            chinese_name=chinese_name,
        )

        single_watchlist_entry.additional_properties = d
        return single_watchlist_entry

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
