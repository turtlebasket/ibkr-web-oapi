from typing import Any, Dict, List, Type, TypeVar, Union

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

T = TypeVar("T", bound="UserAccountsResponseAllowFeatures")


@_attrs_define
class UserAccountsResponseAllowFeatures:
    """
    Attributes:
        show_gfis (Union[Unset, bool]):
        show_eu_cost_report (Union[Unset, bool]):
        allow_event_contract (Union[Unset, bool]):
        allow_fx_conv (Union[Unset, bool]):
        allow_financial_lens (Union[Unset, bool]):
        allow_mta (Union[Unset, bool]):
        allow_type_ahead (Union[Unset, bool]):
        allow_event_trading (Union[Unset, bool]):
        snapshot_refresh_timeout (Union[Unset, int]):  Example: 30.
        lite_user (Union[Unset, bool]):
        show_web_news (Union[Unset, bool]):
        research (Union[Unset, bool]):
        debug_pnl (Union[Unset, bool]):
        show_tax_opt (Union[Unset, bool]):
        show_impact_dashboard (Union[Unset, bool]):
        allow_dyn_account (Union[Unset, bool]):
        allow_crypto (Union[Unset, bool]):
        allowed_asset_types (Union[Unset, str]):
    """

    show_gfis: Union[Unset, bool] = UNSET
    show_eu_cost_report: Union[Unset, bool] = UNSET
    allow_event_contract: Union[Unset, bool] = UNSET
    allow_fx_conv: Union[Unset, bool] = UNSET
    allow_financial_lens: Union[Unset, bool] = UNSET
    allow_mta: Union[Unset, bool] = UNSET
    allow_type_ahead: Union[Unset, bool] = UNSET
    allow_event_trading: Union[Unset, bool] = UNSET
    snapshot_refresh_timeout: Union[Unset, int] = UNSET
    lite_user: Union[Unset, bool] = UNSET
    show_web_news: Union[Unset, bool] = UNSET
    research: Union[Unset, bool] = UNSET
    debug_pnl: Union[Unset, bool] = UNSET
    show_tax_opt: Union[Unset, bool] = UNSET
    show_impact_dashboard: Union[Unset, bool] = UNSET
    allow_dyn_account: Union[Unset, bool] = UNSET
    allow_crypto: Union[Unset, bool] = UNSET
    allowed_asset_types: Union[Unset, str] = UNSET
    additional_properties: Dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> Dict[str, Any]:
        show_gfis = self.show_gfis

        show_eu_cost_report = self.show_eu_cost_report

        allow_event_contract = self.allow_event_contract

        allow_fx_conv = self.allow_fx_conv

        allow_financial_lens = self.allow_financial_lens

        allow_mta = self.allow_mta

        allow_type_ahead = self.allow_type_ahead

        allow_event_trading = self.allow_event_trading

        snapshot_refresh_timeout = self.snapshot_refresh_timeout

        lite_user = self.lite_user

        show_web_news = self.show_web_news

        research = self.research

        debug_pnl = self.debug_pnl

        show_tax_opt = self.show_tax_opt

        show_impact_dashboard = self.show_impact_dashboard

        allow_dyn_account = self.allow_dyn_account

        allow_crypto = self.allow_crypto

        allowed_asset_types = self.allowed_asset_types

        field_dict: Dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if show_gfis is not UNSET:
            field_dict["showGFIS"] = show_gfis
        if show_eu_cost_report is not UNSET:
            field_dict["showEUCostReport"] = show_eu_cost_report
        if allow_event_contract is not UNSET:
            field_dict["allowEventContract"] = allow_event_contract
        if allow_fx_conv is not UNSET:
            field_dict["allowFXConv"] = allow_fx_conv
        if allow_financial_lens is not UNSET:
            field_dict["allowFinancialLens"] = allow_financial_lens
        if allow_mta is not UNSET:
            field_dict["allowMTA"] = allow_mta
        if allow_type_ahead is not UNSET:
            field_dict["allowTypeAhead"] = allow_type_ahead
        if allow_event_trading is not UNSET:
            field_dict["allowEventTrading"] = allow_event_trading
        if snapshot_refresh_timeout is not UNSET:
            field_dict["snapshotRefreshTimeout"] = snapshot_refresh_timeout
        if lite_user is not UNSET:
            field_dict["liteUser"] = lite_user
        if show_web_news is not UNSET:
            field_dict["showWebNews"] = show_web_news
        if research is not UNSET:
            field_dict["research"] = research
        if debug_pnl is not UNSET:
            field_dict["debugPnl"] = debug_pnl
        if show_tax_opt is not UNSET:
            field_dict["showTaxOpt"] = show_tax_opt
        if show_impact_dashboard is not UNSET:
            field_dict["showImpactDashboard"] = show_impact_dashboard
        if allow_dyn_account is not UNSET:
            field_dict["allowDynAccount"] = allow_dyn_account
        if allow_crypto is not UNSET:
            field_dict["allowCrypto"] = allow_crypto
        if allowed_asset_types is not UNSET:
            field_dict["allowedAssetTypes"] = allowed_asset_types

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        d = src_dict.copy()
        show_gfis = d.pop("showGFIS", UNSET)

        show_eu_cost_report = d.pop("showEUCostReport", UNSET)

        allow_event_contract = d.pop("allowEventContract", UNSET)

        allow_fx_conv = d.pop("allowFXConv", UNSET)

        allow_financial_lens = d.pop("allowFinancialLens", UNSET)

        allow_mta = d.pop("allowMTA", UNSET)

        allow_type_ahead = d.pop("allowTypeAhead", UNSET)

        allow_event_trading = d.pop("allowEventTrading", UNSET)

        snapshot_refresh_timeout = d.pop("snapshotRefreshTimeout", UNSET)

        lite_user = d.pop("liteUser", UNSET)

        show_web_news = d.pop("showWebNews", UNSET)

        research = d.pop("research", UNSET)

        debug_pnl = d.pop("debugPnl", UNSET)

        show_tax_opt = d.pop("showTaxOpt", UNSET)

        show_impact_dashboard = d.pop("showImpactDashboard", UNSET)

        allow_dyn_account = d.pop("allowDynAccount", UNSET)

        allow_crypto = d.pop("allowCrypto", UNSET)

        allowed_asset_types = d.pop("allowedAssetTypes", UNSET)

        user_accounts_response_allow_features = cls(
            show_gfis=show_gfis,
            show_eu_cost_report=show_eu_cost_report,
            allow_event_contract=allow_event_contract,
            allow_fx_conv=allow_fx_conv,
            allow_financial_lens=allow_financial_lens,
            allow_mta=allow_mta,
            allow_type_ahead=allow_type_ahead,
            allow_event_trading=allow_event_trading,
            snapshot_refresh_timeout=snapshot_refresh_timeout,
            lite_user=lite_user,
            show_web_news=show_web_news,
            research=research,
            debug_pnl=debug_pnl,
            show_tax_opt=show_tax_opt,
            show_impact_dashboard=show_impact_dashboard,
            allow_dyn_account=allow_dyn_account,
            allow_crypto=allow_crypto,
            allowed_asset_types=allowed_asset_types,
        )

        user_accounts_response_allow_features.additional_properties = d
        return user_accounts_response_allow_features

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
