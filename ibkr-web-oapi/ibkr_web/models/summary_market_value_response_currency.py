from typing import Any, Dict, List, Type, TypeVar, Union

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

T = TypeVar("T", bound="SummaryMarketValueResponseCurrency")


@_attrs_define
class SummaryMarketValueResponseCurrency:
    """Returns an object containing market value details of the currency and positions held using that currency.

    Attributes:
        total_cash (Union[Unset, str]): Lists the total cash held for the given currency.
        settled_cash (Union[Unset, str]): Cash recognized at the time of settlement minus the purchases at time of
            trade, commissions, taxes, and fees.
        mtd_interest (Union[Unset, str]): Total Month-to-date interest.
        stock (Union[Unset, str]): Total cash value of stocks held.
        options (Union[Unset, str]): Total cash value of options held.
        futures (Union[Unset, str]): Total cash value of futures held.
        future_options (Union[Unset, str]): Total cash value of future options held.
        funds (Union[Unset, str]): Total cash value of funds held.
        dividends_receivable (Union[Unset, str]): Total cash value of receivable dividends.
        mutual_funds (Union[Unset, str]): Total cash value of mutual funds held.
        money_market (Union[Unset, str]): Total cash value of money market securities held.
        bonds (Union[Unset, str]): Total cash value of bonds held.
        govt_bonds (Union[Unset, str]): Total cash value of goverment bonds held.
        t_bills (Union[Unset, str]): Total cash value of t-bill bonds held.
        warrants (Union[Unset, str]): Total cash value of warrants held.
        issuer_option (Union[Unset, str]): Total cash value of issuer options held.
        commodity (Union[Unset, str]): Total cash value of commodities held.
        notional_cfd (Union[Unset, str]): Total cash value of notional CFDs held.
        cfd (Union[Unset, str]): Total cash value of CFDs held.
        net_liquidation (Union[Unset, str]): Total cash value of your net liquidty.
        unrealized_pnl (Union[Unset, str]): Total daily unrealized profit and loss.
        realized_pnl (Union[Unset, str]): Total daily realized profit and loss.
        exchange_rate (Union[Unset, str]): Exchange rate of the labeled currency to the base currency.
    """

    total_cash: Union[Unset, str] = UNSET
    settled_cash: Union[Unset, str] = UNSET
    mtd_interest: Union[Unset, str] = UNSET
    stock: Union[Unset, str] = UNSET
    options: Union[Unset, str] = UNSET
    futures: Union[Unset, str] = UNSET
    future_options: Union[Unset, str] = UNSET
    funds: Union[Unset, str] = UNSET
    dividends_receivable: Union[Unset, str] = UNSET
    mutual_funds: Union[Unset, str] = UNSET
    money_market: Union[Unset, str] = UNSET
    bonds: Union[Unset, str] = UNSET
    govt_bonds: Union[Unset, str] = UNSET
    t_bills: Union[Unset, str] = UNSET
    warrants: Union[Unset, str] = UNSET
    issuer_option: Union[Unset, str] = UNSET
    commodity: Union[Unset, str] = UNSET
    notional_cfd: Union[Unset, str] = UNSET
    cfd: Union[Unset, str] = UNSET
    net_liquidation: Union[Unset, str] = UNSET
    unrealized_pnl: Union[Unset, str] = UNSET
    realized_pnl: Union[Unset, str] = UNSET
    exchange_rate: Union[Unset, str] = UNSET
    additional_properties: Dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> Dict[str, Any]:
        total_cash = self.total_cash

        settled_cash = self.settled_cash

        mtd_interest = self.mtd_interest

        stock = self.stock

        options = self.options

        futures = self.futures

        future_options = self.future_options

        funds = self.funds

        dividends_receivable = self.dividends_receivable

        mutual_funds = self.mutual_funds

        money_market = self.money_market

        bonds = self.bonds

        govt_bonds = self.govt_bonds

        t_bills = self.t_bills

        warrants = self.warrants

        issuer_option = self.issuer_option

        commodity = self.commodity

        notional_cfd = self.notional_cfd

        cfd = self.cfd

        net_liquidation = self.net_liquidation

        unrealized_pnl = self.unrealized_pnl

        realized_pnl = self.realized_pnl

        exchange_rate = self.exchange_rate

        field_dict: Dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if total_cash is not UNSET:
            field_dict["total_cash"] = total_cash
        if settled_cash is not UNSET:
            field_dict["settled_cash"] = settled_cash
        if mtd_interest is not UNSET:
            field_dict["MTD Interest"] = mtd_interest
        if stock is not UNSET:
            field_dict["stock"] = stock
        if options is not UNSET:
            field_dict["options"] = options
        if futures is not UNSET:
            field_dict["futures"] = futures
        if future_options is not UNSET:
            field_dict["future_options"] = future_options
        if funds is not UNSET:
            field_dict["funds"] = funds
        if dividends_receivable is not UNSET:
            field_dict["dividends_receivable"] = dividends_receivable
        if mutual_funds is not UNSET:
            field_dict["mutual_funds"] = mutual_funds
        if money_market is not UNSET:
            field_dict["money_market"] = money_market
        if bonds is not UNSET:
            field_dict["bonds"] = bonds
        if govt_bonds is not UNSET:
            field_dict["Govt Bonds"] = govt_bonds
        if t_bills is not UNSET:
            field_dict["t_bills"] = t_bills
        if warrants is not UNSET:
            field_dict["warrants"] = warrants
        if issuer_option is not UNSET:
            field_dict["issuer_option"] = issuer_option
        if commodity is not UNSET:
            field_dict["commodity"] = commodity
        if notional_cfd is not UNSET:
            field_dict["Notional CFD"] = notional_cfd
        if cfd is not UNSET:
            field_dict["cfd"] = cfd
        if net_liquidation is not UNSET:
            field_dict["net_liquidation"] = net_liquidation
        if unrealized_pnl is not UNSET:
            field_dict["unrealized_pnl"] = unrealized_pnl
        if realized_pnl is not UNSET:
            field_dict["realized_pnl"] = realized_pnl
        if exchange_rate is not UNSET:
            field_dict["Exchange Rate"] = exchange_rate

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        d = src_dict.copy()
        total_cash = d.pop("total_cash", UNSET)

        settled_cash = d.pop("settled_cash", UNSET)

        mtd_interest = d.pop("MTD Interest", UNSET)

        stock = d.pop("stock", UNSET)

        options = d.pop("options", UNSET)

        futures = d.pop("futures", UNSET)

        future_options = d.pop("future_options", UNSET)

        funds = d.pop("funds", UNSET)

        dividends_receivable = d.pop("dividends_receivable", UNSET)

        mutual_funds = d.pop("mutual_funds", UNSET)

        money_market = d.pop("money_market", UNSET)

        bonds = d.pop("bonds", UNSET)

        govt_bonds = d.pop("Govt Bonds", UNSET)

        t_bills = d.pop("t_bills", UNSET)

        warrants = d.pop("warrants", UNSET)

        issuer_option = d.pop("issuer_option", UNSET)

        commodity = d.pop("commodity", UNSET)

        notional_cfd = d.pop("Notional CFD", UNSET)

        cfd = d.pop("cfd", UNSET)

        net_liquidation = d.pop("net_liquidation", UNSET)

        unrealized_pnl = d.pop("unrealized_pnl", UNSET)

        realized_pnl = d.pop("realized_pnl", UNSET)

        exchange_rate = d.pop("Exchange Rate", UNSET)

        summary_market_value_response_currency = cls(
            total_cash=total_cash,
            settled_cash=settled_cash,
            mtd_interest=mtd_interest,
            stock=stock,
            options=options,
            futures=futures,
            future_options=future_options,
            funds=funds,
            dividends_receivable=dividends_receivable,
            mutual_funds=mutual_funds,
            money_market=money_market,
            bonds=bonds,
            govt_bonds=govt_bonds,
            t_bills=t_bills,
            warrants=warrants,
            issuer_option=issuer_option,
            commodity=commodity,
            notional_cfd=notional_cfd,
            cfd=cfd,
            net_liquidation=net_liquidation,
            unrealized_pnl=unrealized_pnl,
            realized_pnl=realized_pnl,
            exchange_rate=exchange_rate,
        )

        summary_market_value_response_currency.additional_properties = d
        return summary_market_value_response_currency

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
