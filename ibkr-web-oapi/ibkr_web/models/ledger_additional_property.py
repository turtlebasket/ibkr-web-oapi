from typing import Any, Dict, List, Type, TypeVar, Union

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..models.ledger_additional_property_key import LedgerAdditionalPropertyKey
from ..types import UNSET, Unset

T = TypeVar("T", bound="LedgerAdditionalProperty")


@_attrs_define
class LedgerAdditionalProperty:
    """Object describing the account's balances in its base currency, by asset class and account segments. Will be
    duplicated by another object in response bearing the currency's name.

        Attributes:
            acctcode (Union[Unset, str]): The Account ID of the requested account.
            cashbalance (Union[Unset, float]): The given account's cash balance in this currency.
            cashbalancefxsegment (Union[Unset, float]): The given account's cash balance in its dedicated forex segment in
                this currency, if applicable.
            commoditymarketvalue (Union[Unset, float]): Market value of the given account's commodity positions in this
                currency.
            corporatebondsmarketvalue (Union[Unset, float]): Market value of the given account's corporate bond positions in
                this currency.
            currency (Union[Unset, str]): Three-letter name of the currency reflected by this object, or 'BASE' for the
                account's base currency.
            dividends (Union[Unset, float]): The given account's receivable (not yet disbursed) dividend balance in this
                currency.
            exchangerate (Union[Unset, int]): Exchange rate of this currency relative to the account's base currency.
            funds (Union[Unset, float]): The value of the given account's mutual fund holdings in this currency.
            futuremarketvalue (Union[Unset, float]): Market value of the given account's futures positions in this currency.
            futureoptionmarketvalue (Union[Unset, float]): Market value of the given account's futures options positions in
                this currency.
            futuresonlypnl (Union[Unset, float]): PnL of the given account's futures positions in this currency.
            interest (Union[Unset, float]): The given account's receivable interest balance in this currency.
            issueroptionsmarketvalue (Union[Unset, float]): Market value of the given account's issuer options positions in
                this currency.
            key (Union[Unset, LedgerAdditionalPropertyKey]): Identifies the nature of data. Always takes values
                'LedgerList'.
            moneyfunds (Union[Unset, float]): The value of the given account's money market fund holdings in this currency.
            netliquidationvalue (Union[Unset, float]): The given account's net liquidation value of positions in this
                currency.
            realizedpnl (Union[Unset, float]): The given account's realized PnL for positions in this currency.
            secondkey (Union[Unset, str]): Additional identifier of the currency reflected in this object. Always matches
                'currency' field.
            sessionid (Union[Unset, int]):
            settledcash (Union[Unset, float]): The given account's settled cash balance in this currency.
            severity (Union[Unset, int]):
            stockmarketvalue (Union[Unset, float]): Market value of the given account's stock positions in this currency.
            stockoptionmarketvalue (Union[Unset, float]): Market value of the given account's stock options positions in
                this currency.
            tbillsmarketvalue (Union[Unset, float]): Market value of the given account's treasury bill positions in this
                currency.
            tbondsmarketvalue (Union[Unset, float]): Market value of the given account's treasury bond positions in this
                currency.
            timestamp (Union[Unset, int]): Timestamp of retrievable of this account ledger data.
            unrealizedpnl (Union[Unset, float]): The given account's unrealied PnL for positions in this currency.
            warrantsmarketvalue (Union[Unset, float]): Market value of the given account's warrant positions in this
                currency.
    """

    acctcode: Union[Unset, str] = UNSET
    cashbalance: Union[Unset, float] = UNSET
    cashbalancefxsegment: Union[Unset, float] = UNSET
    commoditymarketvalue: Union[Unset, float] = UNSET
    corporatebondsmarketvalue: Union[Unset, float] = UNSET
    currency: Union[Unset, str] = UNSET
    dividends: Union[Unset, float] = UNSET
    exchangerate: Union[Unset, int] = UNSET
    funds: Union[Unset, float] = UNSET
    futuremarketvalue: Union[Unset, float] = UNSET
    futureoptionmarketvalue: Union[Unset, float] = UNSET
    futuresonlypnl: Union[Unset, float] = UNSET
    interest: Union[Unset, float] = UNSET
    issueroptionsmarketvalue: Union[Unset, float] = UNSET
    key: Union[Unset, LedgerAdditionalPropertyKey] = UNSET
    moneyfunds: Union[Unset, float] = UNSET
    netliquidationvalue: Union[Unset, float] = UNSET
    realizedpnl: Union[Unset, float] = UNSET
    secondkey: Union[Unset, str] = UNSET
    sessionid: Union[Unset, int] = UNSET
    settledcash: Union[Unset, float] = UNSET
    severity: Union[Unset, int] = UNSET
    stockmarketvalue: Union[Unset, float] = UNSET
    stockoptionmarketvalue: Union[Unset, float] = UNSET
    tbillsmarketvalue: Union[Unset, float] = UNSET
    tbondsmarketvalue: Union[Unset, float] = UNSET
    timestamp: Union[Unset, int] = UNSET
    unrealizedpnl: Union[Unset, float] = UNSET
    warrantsmarketvalue: Union[Unset, float] = UNSET
    additional_properties: Dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> Dict[str, Any]:
        acctcode = self.acctcode

        cashbalance = self.cashbalance

        cashbalancefxsegment = self.cashbalancefxsegment

        commoditymarketvalue = self.commoditymarketvalue

        corporatebondsmarketvalue = self.corporatebondsmarketvalue

        currency = self.currency

        dividends = self.dividends

        exchangerate = self.exchangerate

        funds = self.funds

        futuremarketvalue = self.futuremarketvalue

        futureoptionmarketvalue = self.futureoptionmarketvalue

        futuresonlypnl = self.futuresonlypnl

        interest = self.interest

        issueroptionsmarketvalue = self.issueroptionsmarketvalue

        key: Union[Unset, str] = UNSET
        if not isinstance(self.key, Unset):
            key = self.key.value

        moneyfunds = self.moneyfunds

        netliquidationvalue = self.netliquidationvalue

        realizedpnl = self.realizedpnl

        secondkey = self.secondkey

        sessionid = self.sessionid

        settledcash = self.settledcash

        severity = self.severity

        stockmarketvalue = self.stockmarketvalue

        stockoptionmarketvalue = self.stockoptionmarketvalue

        tbillsmarketvalue = self.tbillsmarketvalue

        tbondsmarketvalue = self.tbondsmarketvalue

        timestamp = self.timestamp

        unrealizedpnl = self.unrealizedpnl

        warrantsmarketvalue = self.warrantsmarketvalue

        field_dict: Dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if acctcode is not UNSET:
            field_dict["acctcode"] = acctcode
        if cashbalance is not UNSET:
            field_dict["cashbalance"] = cashbalance
        if cashbalancefxsegment is not UNSET:
            field_dict["cashbalancefxsegment"] = cashbalancefxsegment
        if commoditymarketvalue is not UNSET:
            field_dict["commoditymarketvalue"] = commoditymarketvalue
        if corporatebondsmarketvalue is not UNSET:
            field_dict["corporatebondsmarketvalue"] = corporatebondsmarketvalue
        if currency is not UNSET:
            field_dict["currency"] = currency
        if dividends is not UNSET:
            field_dict["dividends"] = dividends
        if exchangerate is not UNSET:
            field_dict["exchangerate"] = exchangerate
        if funds is not UNSET:
            field_dict["funds"] = funds
        if futuremarketvalue is not UNSET:
            field_dict["futuremarketvalue"] = futuremarketvalue
        if futureoptionmarketvalue is not UNSET:
            field_dict["futureoptionmarketvalue"] = futureoptionmarketvalue
        if futuresonlypnl is not UNSET:
            field_dict["futuresonlypnl"] = futuresonlypnl
        if interest is not UNSET:
            field_dict["interest"] = interest
        if issueroptionsmarketvalue is not UNSET:
            field_dict["issueroptionsmarketvalue"] = issueroptionsmarketvalue
        if key is not UNSET:
            field_dict["key"] = key
        if moneyfunds is not UNSET:
            field_dict["moneyfunds"] = moneyfunds
        if netliquidationvalue is not UNSET:
            field_dict["netliquidationvalue"] = netliquidationvalue
        if realizedpnl is not UNSET:
            field_dict["realizedpnl"] = realizedpnl
        if secondkey is not UNSET:
            field_dict["secondkey"] = secondkey
        if sessionid is not UNSET:
            field_dict["sessionid"] = sessionid
        if settledcash is not UNSET:
            field_dict["settledcash"] = settledcash
        if severity is not UNSET:
            field_dict["severity"] = severity
        if stockmarketvalue is not UNSET:
            field_dict["stockmarketvalue"] = stockmarketvalue
        if stockoptionmarketvalue is not UNSET:
            field_dict["stockoptionmarketvalue"] = stockoptionmarketvalue
        if tbillsmarketvalue is not UNSET:
            field_dict["tbillsmarketvalue"] = tbillsmarketvalue
        if tbondsmarketvalue is not UNSET:
            field_dict["tbondsmarketvalue"] = tbondsmarketvalue
        if timestamp is not UNSET:
            field_dict["timestamp"] = timestamp
        if unrealizedpnl is not UNSET:
            field_dict["unrealizedpnl"] = unrealizedpnl
        if warrantsmarketvalue is not UNSET:
            field_dict["warrantsmarketvalue"] = warrantsmarketvalue

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        d = src_dict.copy()
        acctcode = d.pop("acctcode", UNSET)

        cashbalance = d.pop("cashbalance", UNSET)

        cashbalancefxsegment = d.pop("cashbalancefxsegment", UNSET)

        commoditymarketvalue = d.pop("commoditymarketvalue", UNSET)

        corporatebondsmarketvalue = d.pop("corporatebondsmarketvalue", UNSET)

        currency = d.pop("currency", UNSET)

        dividends = d.pop("dividends", UNSET)

        exchangerate = d.pop("exchangerate", UNSET)

        funds = d.pop("funds", UNSET)

        futuremarketvalue = d.pop("futuremarketvalue", UNSET)

        futureoptionmarketvalue = d.pop("futureoptionmarketvalue", UNSET)

        futuresonlypnl = d.pop("futuresonlypnl", UNSET)

        interest = d.pop("interest", UNSET)

        issueroptionsmarketvalue = d.pop("issueroptionsmarketvalue", UNSET)

        _key = d.pop("key", UNSET)
        key: Union[Unset, LedgerAdditionalPropertyKey]
        if isinstance(_key, Unset):
            key = UNSET
        else:
            key = LedgerAdditionalPropertyKey(_key)

        moneyfunds = d.pop("moneyfunds", UNSET)

        netliquidationvalue = d.pop("netliquidationvalue", UNSET)

        realizedpnl = d.pop("realizedpnl", UNSET)

        secondkey = d.pop("secondkey", UNSET)

        sessionid = d.pop("sessionid", UNSET)

        settledcash = d.pop("settledcash", UNSET)

        severity = d.pop("severity", UNSET)

        stockmarketvalue = d.pop("stockmarketvalue", UNSET)

        stockoptionmarketvalue = d.pop("stockoptionmarketvalue", UNSET)

        tbillsmarketvalue = d.pop("tbillsmarketvalue", UNSET)

        tbondsmarketvalue = d.pop("tbondsmarketvalue", UNSET)

        timestamp = d.pop("timestamp", UNSET)

        unrealizedpnl = d.pop("unrealizedpnl", UNSET)

        warrantsmarketvalue = d.pop("warrantsmarketvalue", UNSET)

        ledger_additional_property = cls(
            acctcode=acctcode,
            cashbalance=cashbalance,
            cashbalancefxsegment=cashbalancefxsegment,
            commoditymarketvalue=commoditymarketvalue,
            corporatebondsmarketvalue=corporatebondsmarketvalue,
            currency=currency,
            dividends=dividends,
            exchangerate=exchangerate,
            funds=funds,
            futuremarketvalue=futuremarketvalue,
            futureoptionmarketvalue=futureoptionmarketvalue,
            futuresonlypnl=futuresonlypnl,
            interest=interest,
            issueroptionsmarketvalue=issueroptionsmarketvalue,
            key=key,
            moneyfunds=moneyfunds,
            netliquidationvalue=netliquidationvalue,
            realizedpnl=realizedpnl,
            secondkey=secondkey,
            sessionid=sessionid,
            settledcash=settledcash,
            severity=severity,
            stockmarketvalue=stockmarketvalue,
            stockoptionmarketvalue=stockoptionmarketvalue,
            tbillsmarketvalue=tbillsmarketvalue,
            tbondsmarketvalue=tbondsmarketvalue,
            timestamp=timestamp,
            unrealizedpnl=unrealizedpnl,
            warrantsmarketvalue=warrantsmarketvalue,
        )

        ledger_additional_property.additional_properties = d
        return ledger_additional_property

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
