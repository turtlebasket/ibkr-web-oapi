from typing import Any, Dict, List, Type, TypeVar, Union

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

T = TypeVar("T", bound="NonDisclosedDetail")


@_attrs_define
class NonDisclosedDetail:
    """
    Attributes:
        trade_date (str):  Example: 2023-07-08.
        settle_date (str):  Example: 2023-07-18.
        pset_bic (Union[Unset, str]):  Example: DTCYUS33XXX.
        reag_deag_bic (Union[Unset, str]):  Example: CH100164.
        buyer_sell_bic (Union[Unset, str]):  Example: 320043.
        member_account_id (Union[Unset, str]):  Example: 123456.
        safe_keeping_account_id (Union[Unset, str]):  Example: 123456.
    """

    trade_date: str
    settle_date: str
    pset_bic: Union[Unset, str] = UNSET
    reag_deag_bic: Union[Unset, str] = UNSET
    buyer_sell_bic: Union[Unset, str] = UNSET
    member_account_id: Union[Unset, str] = UNSET
    safe_keeping_account_id: Union[Unset, str] = UNSET
    additional_properties: Dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> Dict[str, Any]:
        trade_date = self.trade_date

        settle_date = self.settle_date

        pset_bic = self.pset_bic

        reag_deag_bic = self.reag_deag_bic

        buyer_sell_bic = self.buyer_sell_bic

        member_account_id = self.member_account_id

        safe_keeping_account_id = self.safe_keeping_account_id

        field_dict: Dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "tradeDate": trade_date,
                "settleDate": settle_date,
            }
        )
        if pset_bic is not UNSET:
            field_dict["psetBic"] = pset_bic
        if reag_deag_bic is not UNSET:
            field_dict["reagDeagBic"] = reag_deag_bic
        if buyer_sell_bic is not UNSET:
            field_dict["buyerSellBic"] = buyer_sell_bic
        if member_account_id is not UNSET:
            field_dict["memberAccountId"] = member_account_id
        if safe_keeping_account_id is not UNSET:
            field_dict["safeKeepingAccountId"] = safe_keeping_account_id

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        d = src_dict.copy()
        trade_date = d.pop("tradeDate")

        settle_date = d.pop("settleDate")

        pset_bic = d.pop("psetBic", UNSET)

        reag_deag_bic = d.pop("reagDeagBic", UNSET)

        buyer_sell_bic = d.pop("buyerSellBic", UNSET)

        member_account_id = d.pop("memberAccountId", UNSET)

        safe_keeping_account_id = d.pop("safeKeepingAccountId", UNSET)

        non_disclosed_detail = cls(
            trade_date=trade_date,
            settle_date=settle_date,
            pset_bic=pset_bic,
            reag_deag_bic=reag_deag_bic,
            buyer_sell_bic=buyer_sell_bic,
            member_account_id=member_account_id,
            safe_keeping_account_id=safe_keeping_account_id,
        )

        non_disclosed_detail.additional_properties = d
        return non_disclosed_detail

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
