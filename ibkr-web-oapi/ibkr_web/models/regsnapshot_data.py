from typing import Any, Dict, List, Type, TypeVar, Union

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

T = TypeVar("T", bound="RegsnapshotData")


@_attrs_define
class RegsnapshotData:
    """Object containing regulatory snapshot data.

    Attributes:
        conid (Union[Unset, int]): IB contract ID.
        conid_ex (Union[Unset, str]): Contract ID and routing destination in format 123456@EXCHANGE.
        size_min_tick (Union[Unset, float]): Internal use. Minimum size display increment.
        bbo_exchange (Union[Unset, str]): Internal use. Exchange map code.
        has_delayed (Union[Unset, bool]): Indicates whether delayed data is available.
        field_84 (Union[Unset, str]): Bid price.
        field_86 (Union[Unset, str]): Ask price.
        field_88 (Union[Unset, int]): Bid size in round lots (100 shares).
        field_85 (Union[Unset, int]): Ask size in round lots (100 shares).
        best_bid_exch (Union[Unset, int]): Internal use. Equivalent binary encoding of field 7068.
        best_ask_exch (Union[Unset, int]): Internal use. Equivalent binary encoding of field 7057.
        field_31 (Union[Unset, str]): Last traded price.
        field_7059 (Union[Unset, str]): Last traded size in round lots (100 shares).
        last_exch (Union[Unset, int]): Internal use. Equivalent binary encoding of field 7058.
        field_7057 (Union[Unset, str]): Best ask exchanges(s). String of single, capital-letter MCOIDs.
        field_7068 (Union[Unset, str]): Best bid exchange(s). String of single, capital-letter MCOIDs.
        field_7058 (Union[Unset, str]): Exchange of last trade. A single, capital-letter MCOID.
    """

    conid: Union[Unset, int] = UNSET
    conid_ex: Union[Unset, str] = UNSET
    size_min_tick: Union[Unset, float] = UNSET
    bbo_exchange: Union[Unset, str] = UNSET
    has_delayed: Union[Unset, bool] = UNSET
    field_84: Union[Unset, str] = UNSET
    field_86: Union[Unset, str] = UNSET
    field_88: Union[Unset, int] = UNSET
    field_85: Union[Unset, int] = UNSET
    best_bid_exch: Union[Unset, int] = UNSET
    best_ask_exch: Union[Unset, int] = UNSET
    field_31: Union[Unset, str] = UNSET
    field_7059: Union[Unset, str] = UNSET
    last_exch: Union[Unset, int] = UNSET
    field_7057: Union[Unset, str] = UNSET
    field_7068: Union[Unset, str] = UNSET
    field_7058: Union[Unset, str] = UNSET
    additional_properties: Dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> Dict[str, Any]:
        conid = self.conid

        conid_ex = self.conid_ex

        size_min_tick = self.size_min_tick

        bbo_exchange = self.bbo_exchange

        has_delayed = self.has_delayed

        field_84 = self.field_84

        field_86 = self.field_86

        field_88 = self.field_88

        field_85 = self.field_85

        best_bid_exch = self.best_bid_exch

        best_ask_exch = self.best_ask_exch

        field_31 = self.field_31

        field_7059 = self.field_7059

        last_exch = self.last_exch

        field_7057 = self.field_7057

        field_7068 = self.field_7068

        field_7058 = self.field_7058

        field_dict: Dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if conid is not UNSET:
            field_dict["conid"] = conid
        if conid_ex is not UNSET:
            field_dict["conidEx"] = conid_ex
        if size_min_tick is not UNSET:
            field_dict["sizeMinTick"] = size_min_tick
        if bbo_exchange is not UNSET:
            field_dict["BboExchange"] = bbo_exchange
        if has_delayed is not UNSET:
            field_dict["HasDelayed"] = has_delayed
        if field_84 is not UNSET:
            field_dict["84"] = field_84
        if field_86 is not UNSET:
            field_dict["86"] = field_86
        if field_88 is not UNSET:
            field_dict["88"] = field_88
        if field_85 is not UNSET:
            field_dict["85"] = field_85
        if best_bid_exch is not UNSET:
            field_dict["BestBidExch"] = best_bid_exch
        if best_ask_exch is not UNSET:
            field_dict["BestAskExch"] = best_ask_exch
        if field_31 is not UNSET:
            field_dict["31"] = field_31
        if field_7059 is not UNSET:
            field_dict["7059"] = field_7059
        if last_exch is not UNSET:
            field_dict["LastExch"] = last_exch
        if field_7057 is not UNSET:
            field_dict["7057"] = field_7057
        if field_7068 is not UNSET:
            field_dict["7068"] = field_7068
        if field_7058 is not UNSET:
            field_dict["7058"] = field_7058

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        d = src_dict.copy()
        conid = d.pop("conid", UNSET)

        conid_ex = d.pop("conidEx", UNSET)

        size_min_tick = d.pop("sizeMinTick", UNSET)

        bbo_exchange = d.pop("BboExchange", UNSET)

        has_delayed = d.pop("HasDelayed", UNSET)

        field_84 = d.pop("84", UNSET)

        field_86 = d.pop("86", UNSET)

        field_88 = d.pop("88", UNSET)

        field_85 = d.pop("85", UNSET)

        best_bid_exch = d.pop("BestBidExch", UNSET)

        best_ask_exch = d.pop("BestAskExch", UNSET)

        field_31 = d.pop("31", UNSET)

        field_7059 = d.pop("7059", UNSET)

        last_exch = d.pop("LastExch", UNSET)

        field_7057 = d.pop("7057", UNSET)

        field_7068 = d.pop("7068", UNSET)

        field_7058 = d.pop("7058", UNSET)

        regsnapshot_data = cls(
            conid=conid,
            conid_ex=conid_ex,
            size_min_tick=size_min_tick,
            bbo_exchange=bbo_exchange,
            has_delayed=has_delayed,
            field_84=field_84,
            field_86=field_86,
            field_88=field_88,
            field_85=field_85,
            best_bid_exch=best_bid_exch,
            best_ask_exch=best_ask_exch,
            field_31=field_31,
            field_7059=field_7059,
            last_exch=last_exch,
            field_7057=field_7057,
            field_7068=field_7068,
            field_7058=field_7058,
        )

        regsnapshot_data.additional_properties = d
        return regsnapshot_data

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
