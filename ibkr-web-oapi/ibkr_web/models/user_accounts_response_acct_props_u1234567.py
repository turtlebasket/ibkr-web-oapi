from typing import Any, Dict, List, Type, TypeVar, Union

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

T = TypeVar("T", bound="UserAccountsResponseAcctPropsU1234567")


@_attrs_define
class UserAccountsResponseAcctPropsU1234567:
    """
    Attributes:
        has_child_accounts (Union[Unset, bool]):
        supports_cash_qty (Union[Unset, bool]):
        no_fx_conv (Union[Unset, bool]):
        is_prop (Union[Unset, bool]):
        supports_fractions (Union[Unset, bool]):
        allow_customer_time (Union[Unset, bool]):
    """

    has_child_accounts: Union[Unset, bool] = UNSET
    supports_cash_qty: Union[Unset, bool] = UNSET
    no_fx_conv: Union[Unset, bool] = UNSET
    is_prop: Union[Unset, bool] = UNSET
    supports_fractions: Union[Unset, bool] = UNSET
    allow_customer_time: Union[Unset, bool] = UNSET
    additional_properties: Dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> Dict[str, Any]:
        has_child_accounts = self.has_child_accounts

        supports_cash_qty = self.supports_cash_qty

        no_fx_conv = self.no_fx_conv

        is_prop = self.is_prop

        supports_fractions = self.supports_fractions

        allow_customer_time = self.allow_customer_time

        field_dict: Dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if has_child_accounts is not UNSET:
            field_dict["hasChildAccounts"] = has_child_accounts
        if supports_cash_qty is not UNSET:
            field_dict["supportsCashQty"] = supports_cash_qty
        if no_fx_conv is not UNSET:
            field_dict["noFXConv"] = no_fx_conv
        if is_prop is not UNSET:
            field_dict["isProp"] = is_prop
        if supports_fractions is not UNSET:
            field_dict["supportsFractions"] = supports_fractions
        if allow_customer_time is not UNSET:
            field_dict["allowCustomerTime"] = allow_customer_time

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        d = src_dict.copy()
        has_child_accounts = d.pop("hasChildAccounts", UNSET)

        supports_cash_qty = d.pop("supportsCashQty", UNSET)

        no_fx_conv = d.pop("noFXConv", UNSET)

        is_prop = d.pop("isProp", UNSET)

        supports_fractions = d.pop("supportsFractions", UNSET)

        allow_customer_time = d.pop("allowCustomerTime", UNSET)

        user_accounts_response_acct_props_u1234567 = cls(
            has_child_accounts=has_child_accounts,
            supports_cash_qty=supports_cash_qty,
            no_fx_conv=no_fx_conv,
            is_prop=is_prop,
            supports_fractions=supports_fractions,
            allow_customer_time=allow_customer_time,
        )

        user_accounts_response_acct_props_u1234567.additional_properties = d
        return user_accounts_response_acct_props_u1234567

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
