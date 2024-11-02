from typing import Any, Dict, List, Type, TypeVar, Union

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

T = TypeVar("T", bound="SummaryOfAccountMarginResponseCommodities")


@_attrs_define
class SummaryOfAccountMarginResponseCommodities:
    """
    Attributes:
        current_initial (Union[Unset, str]): The minimum amount required to open a new position.
        prdctd_pst_xpry_mrgn_opn (Union[Unset, str]): Provides a projected “at expiration” margin value based on the
            soon-to-expire contracts in your portfolio.
        current_maint (Union[Unset, str]): The amount of equity required to maintain your positions.
        projected_liquidity_inital_margin (Union[Unset, str]): Provides a projected "liquid" initial margin value based
            on account liquidation value.
        prjctd_lk_ahd_mntnnc_mrgn (Union[Unset, str]): If it is 3:00 pm ET, the next calculation you’re looking ahead to
            is after the close, or the Overnight Initial Margin. If it’s 3:00 am ET, the next calculation will be at the
            market’s open.
             * `Securities` – Projected maintenance margin requirement as of next period’s margin change, in the base
            currency of the account.
             * `Commodities` – Maintenance margin requirement as of next period’s margin change in the base currency of the
            account based on current margin requirements, which are subject to change. This value depends on when you are
            viewing your margin requirements.
        projected_overnight_initial_margin (Union[Unset, str]): Overnight refers to the window of time after the local
            market trading day is closed.
              * Securities – Projected overnight initial margin requirement in the base currency of the account.
              * Commodities – Overnight initial margin requirement in the base currency of the account based on current
            margin requirements, which are subject to change.
        prjctd_ovrnght_mntnnc_mrgn (Union[Unset, str]): Overnight refers to the window of time after the local market
            trading day is closed.
              * `Securities` – Projected overnight maintenance margin requirement in the base currency of the account.
              * `Commodities` – Overnight maintenance margin requirement in the base currency of the account based on
            current margin requirements, which are subject to change.
    """

    current_initial: Union[Unset, str] = UNSET
    prdctd_pst_xpry_mrgn_opn: Union[Unset, str] = UNSET
    current_maint: Union[Unset, str] = UNSET
    projected_liquidity_inital_margin: Union[Unset, str] = UNSET
    prjctd_lk_ahd_mntnnc_mrgn: Union[Unset, str] = UNSET
    projected_overnight_initial_margin: Union[Unset, str] = UNSET
    prjctd_ovrnght_mntnnc_mrgn: Union[Unset, str] = UNSET
    additional_properties: Dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> Dict[str, Any]:
        current_initial = self.current_initial

        prdctd_pst_xpry_mrgn_opn = self.prdctd_pst_xpry_mrgn_opn

        current_maint = self.current_maint

        projected_liquidity_inital_margin = self.projected_liquidity_inital_margin

        prjctd_lk_ahd_mntnnc_mrgn = self.prjctd_lk_ahd_mntnnc_mrgn

        projected_overnight_initial_margin = self.projected_overnight_initial_margin

        prjctd_ovrnght_mntnnc_mrgn = self.prjctd_ovrnght_mntnnc_mrgn

        field_dict: Dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if current_initial is not UNSET:
            field_dict["current_initial"] = current_initial
        if prdctd_pst_xpry_mrgn_opn is not UNSET:
            field_dict["Prdctd Pst-xpry Mrgn @ Opn"] = prdctd_pst_xpry_mrgn_opn
        if current_maint is not UNSET:
            field_dict["current_maint"] = current_maint
        if projected_liquidity_inital_margin is not UNSET:
            field_dict["projected_liquidity_inital_margin"] = projected_liquidity_inital_margin
        if prjctd_lk_ahd_mntnnc_mrgn is not UNSET:
            field_dict["Prjctd Lk Ahd Mntnnc Mrgn"] = prjctd_lk_ahd_mntnnc_mrgn
        if projected_overnight_initial_margin is not UNSET:
            field_dict["projected_overnight_initial_margin"] = projected_overnight_initial_margin
        if prjctd_ovrnght_mntnnc_mrgn is not UNSET:
            field_dict["Prjctd Ovrnght Mntnnc Mrgn"] = prjctd_ovrnght_mntnnc_mrgn

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        d = src_dict.copy()
        current_initial = d.pop("current_initial", UNSET)

        prdctd_pst_xpry_mrgn_opn = d.pop("Prdctd Pst-xpry Mrgn @ Opn", UNSET)

        current_maint = d.pop("current_maint", UNSET)

        projected_liquidity_inital_margin = d.pop("projected_liquidity_inital_margin", UNSET)

        prjctd_lk_ahd_mntnnc_mrgn = d.pop("Prjctd Lk Ahd Mntnnc Mrgn", UNSET)

        projected_overnight_initial_margin = d.pop("projected_overnight_initial_margin", UNSET)

        prjctd_ovrnght_mntnnc_mrgn = d.pop("Prjctd Ovrnght Mntnnc Mrgn", UNSET)

        summary_of_account_margin_response_commodities = cls(
            current_initial=current_initial,
            prdctd_pst_xpry_mrgn_opn=prdctd_pst_xpry_mrgn_opn,
            current_maint=current_maint,
            projected_liquidity_inital_margin=projected_liquidity_inital_margin,
            prjctd_lk_ahd_mntnnc_mrgn=prjctd_lk_ahd_mntnnc_mrgn,
            projected_overnight_initial_margin=projected_overnight_initial_margin,
            prjctd_ovrnght_mntnnc_mrgn=prjctd_ovrnght_mntnnc_mrgn,
        )

        summary_of_account_margin_response_commodities.additional_properties = d
        return summary_of_account_margin_response_commodities

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
