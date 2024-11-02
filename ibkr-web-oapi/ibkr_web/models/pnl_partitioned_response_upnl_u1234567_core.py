from typing import Any, Dict, List, Type, TypeVar, Union

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

T = TypeVar("T", bound="PnlPartitionedResponseUpnlU1234567Core")


@_attrs_define
class PnlPartitionedResponseUpnlU1234567Core:
    """The account or model's Profit and Loss.

    Attributes:
        row_type (Union[Unset, int]): Returns the positional value of the returned account. Always returns 1 for
            individual accounts.
        dpl (Union[Unset, int]): Daily PnL for the specified account profile.
        nl (Union[Unset, int]): Net Liquidity for the specified account profile.
        upl (Union[Unset, int]): Unrealized PnL for the specified account profile.
        el (Union[Unset, int]): Excess Liquidity for the specified account profile.
        mv (Union[Unset, int]): Margin value for the specified account profile.
    """

    row_type: Union[Unset, int] = UNSET
    dpl: Union[Unset, int] = UNSET
    nl: Union[Unset, int] = UNSET
    upl: Union[Unset, int] = UNSET
    el: Union[Unset, int] = UNSET
    mv: Union[Unset, int] = UNSET
    additional_properties: Dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> Dict[str, Any]:
        row_type = self.row_type

        dpl = self.dpl

        nl = self.nl

        upl = self.upl

        el = self.el

        mv = self.mv

        field_dict: Dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if row_type is not UNSET:
            field_dict["rowType"] = row_type
        if dpl is not UNSET:
            field_dict["dpl"] = dpl
        if nl is not UNSET:
            field_dict["nl"] = nl
        if upl is not UNSET:
            field_dict["upl"] = upl
        if el is not UNSET:
            field_dict["el"] = el
        if mv is not UNSET:
            field_dict["mv"] = mv

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        d = src_dict.copy()
        row_type = d.pop("rowType", UNSET)

        dpl = d.pop("dpl", UNSET)

        nl = d.pop("nl", UNSET)

        upl = d.pop("upl", UNSET)

        el = d.pop("el", UNSET)

        mv = d.pop("mv", UNSET)

        pnl_partitioned_response_upnl_u1234567_core = cls(
            row_type=row_type,
            dpl=dpl,
            nl=nl,
            upl=upl,
            el=el,
            mv=mv,
        )

        pnl_partitioned_response_upnl_u1234567_core.additional_properties = d
        return pnl_partitioned_response_upnl_u1234567_core

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
