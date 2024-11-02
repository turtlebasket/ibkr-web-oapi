from typing import Any, Dict, List, Type, TypeVar, Union

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

T = TypeVar("T", bound="AccountSummaryResponseCashBalancesItem")


@_attrs_define
class AccountSummaryResponseCashBalancesItem:
    """
    Attributes:
        currency (Union[Unset, str]): The currency the values represent. Base currency represented as "Total (in
            {BaseCurrency})"
        balance (Union[Unset, int]): The total available currency held in the account.
        settled_cash (Union[Unset, int]): The available settled cash that can be withdrawn from the account.
    """

    currency: Union[Unset, str] = UNSET
    balance: Union[Unset, int] = UNSET
    settled_cash: Union[Unset, int] = UNSET
    additional_properties: Dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> Dict[str, Any]:
        currency = self.currency

        balance = self.balance

        settled_cash = self.settled_cash

        field_dict: Dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if currency is not UNSET:
            field_dict["currency"] = currency
        if balance is not UNSET:
            field_dict["balance"] = balance
        if settled_cash is not UNSET:
            field_dict["settledCash"] = settled_cash

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        d = src_dict.copy()
        currency = d.pop("currency", UNSET)

        balance = d.pop("balance", UNSET)

        settled_cash = d.pop("settledCash", UNSET)

        account_summary_response_cash_balances_item = cls(
            currency=currency,
            balance=balance,
            settled_cash=settled_cash,
        )

        account_summary_response_cash_balances_item.additional_properties = d
        return account_summary_response_cash_balances_item

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
