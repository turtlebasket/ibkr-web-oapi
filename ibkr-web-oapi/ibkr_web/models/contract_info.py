from typing import Any, Dict, List, Type, TypeVar, Union

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

T = TypeVar("T", bound="ContractInfo")


@_attrs_define
class ContractInfo:
    """
    Attributes:
        cfi_code (Union[Unset, str]): Classification of Financial Instrument codes
        symbol (Union[Unset, str]): Underlying symbol
        cusip (Union[Unset, str]): Returns the CUSIP for the given instrument. Only used in BOND trading.
        expiry_full (Union[Unset, str]): Returns the expiration month of the contract.
        con_id (Union[Unset, int]): Indicates the contract identifier of the given contract.
        maturity_date (Union[Unset, str]): Indicates the final maturity date of the given contract.
        industry (Union[Unset, str]): Specific group of companies or businesses.
        instrument_type (Union[Unset, str]): Asset class of the instrument.
        trading_class (Union[Unset, str]): Designated trading class of the contract.
        valid_exchanges (Union[Unset, str]): Comma separated list of support exchanges or trading venues.
        allow_sell_long (Union[Unset, bool]): Allowed to sell shares you own.
        is_zero_commission_security (Union[Unset, bool]): Indicates if the contract supports zero commission trading.
        local_symbol (Union[Unset, str]): Contract’s symbol from primary exchange. For options it is the OCC symbol.
        contract_clarification_type (Union[Unset, str]):
        classifier (Union[Unset, str]):
        currency (Union[Unset, str]): Base currency contract is traded in.
        text (Union[Unset, str]): Indicates the display name of the contract, as shown with Client Portal.
        underlying_con_id (Union[Unset, int]): Underlying contract identifier for the requested contract.
        r_t_h (Union[Unset, bool]): Indicates if the contract can be traded outside regular trading hours or not.
        multiplier (Union[Unset, str]): Indicates the multiplier of the contract.
        underlying_issuer (Union[Unset, str]): Indicates the issuer of the underlying.
        contract_month (Union[Unset, str]): Indicates the year and month the contract expires.
        company_name (Union[Unset, str]): Indicates the name of the company or index.
        smart_available (Union[Unset, bool]): Indicates if the contract can be smart routed or not.
        exchange (Union[Unset, str]): Indicates the primary exchange for which the contract can be traded.
        category (Union[Unset, str]): Indicates the industry category of the instrument.
    """

    cfi_code: Union[Unset, str] = UNSET
    symbol: Union[Unset, str] = UNSET
    cusip: Union[Unset, str] = UNSET
    expiry_full: Union[Unset, str] = UNSET
    con_id: Union[Unset, int] = UNSET
    maturity_date: Union[Unset, str] = UNSET
    industry: Union[Unset, str] = UNSET
    instrument_type: Union[Unset, str] = UNSET
    trading_class: Union[Unset, str] = UNSET
    valid_exchanges: Union[Unset, str] = UNSET
    allow_sell_long: Union[Unset, bool] = UNSET
    is_zero_commission_security: Union[Unset, bool] = UNSET
    local_symbol: Union[Unset, str] = UNSET
    contract_clarification_type: Union[Unset, str] = UNSET
    classifier: Union[Unset, str] = UNSET
    currency: Union[Unset, str] = UNSET
    text: Union[Unset, str] = UNSET
    underlying_con_id: Union[Unset, int] = UNSET
    r_t_h: Union[Unset, bool] = UNSET
    multiplier: Union[Unset, str] = UNSET
    underlying_issuer: Union[Unset, str] = UNSET
    contract_month: Union[Unset, str] = UNSET
    company_name: Union[Unset, str] = UNSET
    smart_available: Union[Unset, bool] = UNSET
    exchange: Union[Unset, str] = UNSET
    category: Union[Unset, str] = UNSET
    additional_properties: Dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> Dict[str, Any]:
        cfi_code = self.cfi_code

        symbol = self.symbol

        cusip = self.cusip

        expiry_full = self.expiry_full

        con_id = self.con_id

        maturity_date = self.maturity_date

        industry = self.industry

        instrument_type = self.instrument_type

        trading_class = self.trading_class

        valid_exchanges = self.valid_exchanges

        allow_sell_long = self.allow_sell_long

        is_zero_commission_security = self.is_zero_commission_security

        local_symbol = self.local_symbol

        contract_clarification_type = self.contract_clarification_type

        classifier = self.classifier

        currency = self.currency

        text = self.text

        underlying_con_id = self.underlying_con_id

        r_t_h = self.r_t_h

        multiplier = self.multiplier

        underlying_issuer = self.underlying_issuer

        contract_month = self.contract_month

        company_name = self.company_name

        smart_available = self.smart_available

        exchange = self.exchange

        category = self.category

        field_dict: Dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if cfi_code is not UNSET:
            field_dict["cfi_code"] = cfi_code
        if symbol is not UNSET:
            field_dict["symbol"] = symbol
        if cusip is not UNSET:
            field_dict["cusip"] = cusip
        if expiry_full is not UNSET:
            field_dict["expiry_full"] = expiry_full
        if con_id is not UNSET:
            field_dict["con_id"] = con_id
        if maturity_date is not UNSET:
            field_dict["maturity_date"] = maturity_date
        if industry is not UNSET:
            field_dict["industry"] = industry
        if instrument_type is not UNSET:
            field_dict["instrument_type"] = instrument_type
        if trading_class is not UNSET:
            field_dict["trading_class"] = trading_class
        if valid_exchanges is not UNSET:
            field_dict["valid_exchanges"] = valid_exchanges
        if allow_sell_long is not UNSET:
            field_dict["allow_sell_long"] = allow_sell_long
        if is_zero_commission_security is not UNSET:
            field_dict["is_zero_commission_security"] = is_zero_commission_security
        if local_symbol is not UNSET:
            field_dict["local_symbol"] = local_symbol
        if contract_clarification_type is not UNSET:
            field_dict["contract_clarification_type"] = contract_clarification_type
        if classifier is not UNSET:
            field_dict["classifier"] = classifier
        if currency is not UNSET:
            field_dict["currency"] = currency
        if text is not UNSET:
            field_dict["text"] = text
        if underlying_con_id is not UNSET:
            field_dict["underlying_con_id"] = underlying_con_id
        if r_t_h is not UNSET:
            field_dict["r_t_h"] = r_t_h
        if multiplier is not UNSET:
            field_dict["multiplier"] = multiplier
        if underlying_issuer is not UNSET:
            field_dict["underlying_issuer"] = underlying_issuer
        if contract_month is not UNSET:
            field_dict["contract_month"] = contract_month
        if company_name is not UNSET:
            field_dict["company_name"] = company_name
        if smart_available is not UNSET:
            field_dict["smart_available"] = smart_available
        if exchange is not UNSET:
            field_dict["exchange"] = exchange
        if category is not UNSET:
            field_dict["category"] = category

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        d = src_dict.copy()
        cfi_code = d.pop("cfi_code", UNSET)

        symbol = d.pop("symbol", UNSET)

        cusip = d.pop("cusip", UNSET)

        expiry_full = d.pop("expiry_full", UNSET)

        con_id = d.pop("con_id", UNSET)

        maturity_date = d.pop("maturity_date", UNSET)

        industry = d.pop("industry", UNSET)

        instrument_type = d.pop("instrument_type", UNSET)

        trading_class = d.pop("trading_class", UNSET)

        valid_exchanges = d.pop("valid_exchanges", UNSET)

        allow_sell_long = d.pop("allow_sell_long", UNSET)

        is_zero_commission_security = d.pop("is_zero_commission_security", UNSET)

        local_symbol = d.pop("local_symbol", UNSET)

        contract_clarification_type = d.pop("contract_clarification_type", UNSET)

        classifier = d.pop("classifier", UNSET)

        currency = d.pop("currency", UNSET)

        text = d.pop("text", UNSET)

        underlying_con_id = d.pop("underlying_con_id", UNSET)

        r_t_h = d.pop("r_t_h", UNSET)

        multiplier = d.pop("multiplier", UNSET)

        underlying_issuer = d.pop("underlying_issuer", UNSET)

        contract_month = d.pop("contract_month", UNSET)

        company_name = d.pop("company_name", UNSET)

        smart_available = d.pop("smart_available", UNSET)

        exchange = d.pop("exchange", UNSET)

        category = d.pop("category", UNSET)

        contract_info = cls(
            cfi_code=cfi_code,
            symbol=symbol,
            cusip=cusip,
            expiry_full=expiry_full,
            con_id=con_id,
            maturity_date=maturity_date,
            industry=industry,
            instrument_type=instrument_type,
            trading_class=trading_class,
            valid_exchanges=valid_exchanges,
            allow_sell_long=allow_sell_long,
            is_zero_commission_security=is_zero_commission_security,
            local_symbol=local_symbol,
            contract_clarification_type=contract_clarification_type,
            classifier=classifier,
            currency=currency,
            text=text,
            underlying_con_id=underlying_con_id,
            r_t_h=r_t_h,
            multiplier=multiplier,
            underlying_issuer=underlying_issuer,
            contract_month=contract_month,
            company_name=company_name,
            smart_available=smart_available,
            exchange=exchange,
            category=category,
        )

        contract_info.additional_properties = d
        return contract_info

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
