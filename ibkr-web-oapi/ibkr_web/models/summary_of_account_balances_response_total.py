from typing import Any, Dict, List, Type, TypeVar, Union

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

T = TypeVar("T", bound="SummaryOfAccountBalancesResponseTotal")


@_attrs_define
class SummaryOfAccountBalancesResponseTotal:
    """Contains total balance details for the account.

    Attributes:
        net_liquidation (Union[Unset, str]): The basis for determining the price of the assets in your account.
        nt_lqdtn_uncrtnty (Union[Unset, str]): Displays the uncertainty of the Net Liquidating Value associated with
            after-hours price changes.
        equity_with_loan (Union[Unset, str]): * `Cash Accounts` Settled cash
             * `Margin Accounts` Total cash value + stock value + bond value + fund value + European & Asian options value.
        prvs_dy_eqty_wth_ln_vl (Union[Unset, str]): The accounts equity balance including loan value.
        sec_gross_pos_val (Union[Unset, str]): Equals the sum of the absolute value of all positions except cash, index
            futures and US treasuries.
        cash (Union[Unset, str]): Total cash balance in the account
        mtd_interest (Union[Unset, str]): Total Month-to-date interest.
        pndng_dbt_crd_chrgs (Union[Unset, str]): Any pending charges for the IBKR debit account.
    """

    net_liquidation: Union[Unset, str] = UNSET
    nt_lqdtn_uncrtnty: Union[Unset, str] = UNSET
    equity_with_loan: Union[Unset, str] = UNSET
    prvs_dy_eqty_wth_ln_vl: Union[Unset, str] = UNSET
    sec_gross_pos_val: Union[Unset, str] = UNSET
    cash: Union[Unset, str] = UNSET
    mtd_interest: Union[Unset, str] = UNSET
    pndng_dbt_crd_chrgs: Union[Unset, str] = UNSET
    additional_properties: Dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> Dict[str, Any]:
        net_liquidation = self.net_liquidation

        nt_lqdtn_uncrtnty = self.nt_lqdtn_uncrtnty

        equity_with_loan = self.equity_with_loan

        prvs_dy_eqty_wth_ln_vl = self.prvs_dy_eqty_wth_ln_vl

        sec_gross_pos_val = self.sec_gross_pos_val

        cash = self.cash

        mtd_interest = self.mtd_interest

        pndng_dbt_crd_chrgs = self.pndng_dbt_crd_chrgs

        field_dict: Dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if net_liquidation is not UNSET:
            field_dict["net_liquidation"] = net_liquidation
        if nt_lqdtn_uncrtnty is not UNSET:
            field_dict["Nt Lqdtn Uncrtnty"] = nt_lqdtn_uncrtnty
        if equity_with_loan is not UNSET:
            field_dict["equity_with_loan"] = equity_with_loan
        if prvs_dy_eqty_wth_ln_vl is not UNSET:
            field_dict["Prvs Dy Eqty Wth Ln Vl"] = prvs_dy_eqty_wth_ln_vl
        if sec_gross_pos_val is not UNSET:
            field_dict["sec_gross_pos_val"] = sec_gross_pos_val
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

        nt_lqdtn_uncrtnty = d.pop("Nt Lqdtn Uncrtnty", UNSET)

        equity_with_loan = d.pop("equity_with_loan", UNSET)

        prvs_dy_eqty_wth_ln_vl = d.pop("Prvs Dy Eqty Wth Ln Vl", UNSET)

        sec_gross_pos_val = d.pop("sec_gross_pos_val", UNSET)

        cash = d.pop("cash", UNSET)

        mtd_interest = d.pop("MTD Interest", UNSET)

        pndng_dbt_crd_chrgs = d.pop("Pndng Dbt Crd Chrgs", UNSET)

        summary_of_account_balances_response_total = cls(
            net_liquidation=net_liquidation,
            nt_lqdtn_uncrtnty=nt_lqdtn_uncrtnty,
            equity_with_loan=equity_with_loan,
            prvs_dy_eqty_wth_ln_vl=prvs_dy_eqty_wth_ln_vl,
            sec_gross_pos_val=sec_gross_pos_val,
            cash=cash,
            mtd_interest=mtd_interest,
            pndng_dbt_crd_chrgs=pndng_dbt_crd_chrgs,
        )

        summary_of_account_balances_response_total.additional_properties = d
        return summary_of_account_balances_response_total

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
