from typing import Any, Dict, List, Type, TypeVar, Union

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

T = TypeVar("T", bound="SummaryOfAccountBalancesResponseCommodities")


@_attrs_define
class SummaryOfAccountBalancesResponseCommodities:
    """Contains Commodity-specific balance details.

    Attributes:
        net_liquidation (Union[Unset, str]): The basis for determining the price of the assets in your account.
        equity_with_loan (Union[Unset, str]): * `Cash Accounts` Settled cash
             * `Margin Accounts` Total cash value + stock value + bond value + fund value + European & Asian options value.
        cash (Union[Unset, str]): Total cash balance in the account
        mtd_interest (Union[Unset, str]): Total Month-to-date interest.
        pndng_dbt_crd_chrgs (Union[Unset, str]): Any pending charges for the IBKR debit account.
    """

    net_liquidation: Union[Unset, str] = UNSET
    equity_with_loan: Union[Unset, str] = UNSET
    cash: Union[Unset, str] = UNSET
    mtd_interest: Union[Unset, str] = UNSET
    pndng_dbt_crd_chrgs: Union[Unset, str] = UNSET
    additional_properties: Dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> Dict[str, Any]:
        net_liquidation = self.net_liquidation

        equity_with_loan = self.equity_with_loan

        cash = self.cash

        mtd_interest = self.mtd_interest

        pndng_dbt_crd_chrgs = self.pndng_dbt_crd_chrgs

        field_dict: Dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if net_liquidation is not UNSET:
            field_dict["net_liquidation"] = net_liquidation
        if equity_with_loan is not UNSET:
            field_dict["equity_with_loan"] = equity_with_loan
        if cash is not UNSET:
            field_dict["cash"] = cash
        if mtd_interest is not UNSET:
            field_dict["MTD Interest"] = mtd_interest
        if pndng_dbt_crd_chrgs is not UNSET:
            field_dict["Pndng Dbt Crd Chrgs"] = pndng_dbt_crd_chrgs

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        d = src_dict.copy()
        net_liquidation = d.pop("net_liquidation", UNSET)

        equity_with_loan = d.pop("equity_with_loan", UNSET)

        cash = d.pop("cash", UNSET)

        mtd_interest = d.pop("MTD Interest", UNSET)

        pndng_dbt_crd_chrgs = d.pop("Pndng Dbt Crd Chrgs", UNSET)

        summary_of_account_balances_response_commodities = cls(
            net_liquidation=net_liquidation,
            equity_with_loan=equity_with_loan,
            cash=cash,
            mtd_interest=mtd_interest,
            pndng_dbt_crd_chrgs=pndng_dbt_crd_chrgs,
        )

        summary_of_account_balances_response_commodities.additional_properties = d
        return summary_of_account_balances_response_commodities

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
