from typing import Any, Dict, List, Type, TypeVar, Union, cast

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..models.sec_def_info_response_right import SecDefInfoResponseRight
from ..types import UNSET, Unset

T = TypeVar("T", bound="SecDefInfoResponse")


@_attrs_define
class SecDefInfoResponse:
    """
    Attributes:
        conid (Union[Unset, int]): Contract Identifier of the given contract.
        ticker (Union[Unset, str]): Ticker symbol for the given contract
        sec_type (Union[Unset, str]): Security type for the given contract.
        listing_exchange (Union[Unset, str]): Primary listing exchange for the given contract.
        exchange (Union[Unset, str]): Exchange requesting data for.
        company_name (Union[Unset, str]): Name of the company for the given contract.
        currency (Union[Unset, str]): Traded currency allowed for the given contract.
        valid_exchanges (Union[Unset, str]): Series of all valid exchanges the contract can be traded on in a single
            comma-separated string.
        price_rendering (Union[Unset, Any]):
        maturity_date (Union[None, Unset, str]): Date of expiration for the given contract.
        right (Union[Unset, SecDefInfoResponseRight]): Set the right for the given contract. * `C` - for Call options. *
            `P` - for Put options.
        strike (Union[Unset, float]): Returns the given strike value for the given contract.
    """

    conid: Union[Unset, int] = UNSET
    ticker: Union[Unset, str] = UNSET
    sec_type: Union[Unset, str] = UNSET
    listing_exchange: Union[Unset, str] = UNSET
    exchange: Union[Unset, str] = UNSET
    company_name: Union[Unset, str] = UNSET
    currency: Union[Unset, str] = UNSET
    valid_exchanges: Union[Unset, str] = UNSET
    price_rendering: Union[Unset, Any] = UNSET
    maturity_date: Union[None, Unset, str] = UNSET
    right: Union[Unset, SecDefInfoResponseRight] = UNSET
    strike: Union[Unset, float] = UNSET
    additional_properties: Dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> Dict[str, Any]:
        conid = self.conid

        ticker = self.ticker

        sec_type = self.sec_type

        listing_exchange = self.listing_exchange

        exchange = self.exchange

        company_name = self.company_name

        currency = self.currency

        valid_exchanges = self.valid_exchanges

        price_rendering = self.price_rendering

        maturity_date: Union[None, Unset, str]
        if isinstance(self.maturity_date, Unset):
            maturity_date = UNSET
        else:
            maturity_date = self.maturity_date

        right: Union[Unset, str] = UNSET
        if not isinstance(self.right, Unset):
            right = self.right.value

        strike = self.strike

        field_dict: Dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if conid is not UNSET:
            field_dict["conid"] = conid
        if ticker is not UNSET:
            field_dict["ticker"] = ticker
        if sec_type is not UNSET:
            field_dict["secType"] = sec_type
        if listing_exchange is not UNSET:
            field_dict["listingExchange"] = listing_exchange
        if exchange is not UNSET:
            field_dict["exchange"] = exchange
        if company_name is not UNSET:
            field_dict["companyName"] = company_name
        if currency is not UNSET:
            field_dict["currency"] = currency
        if valid_exchanges is not UNSET:
            field_dict["validExchanges"] = valid_exchanges
        if price_rendering is not UNSET:
            field_dict["priceRendering"] = price_rendering
        if maturity_date is not UNSET:
            field_dict["maturityDate"] = maturity_date
        if right is not UNSET:
            field_dict["right"] = right
        if strike is not UNSET:
            field_dict["strike"] = strike

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        d = src_dict.copy()
        conid = d.pop("conid", UNSET)

        ticker = d.pop("ticker", UNSET)

        sec_type = d.pop("secType", UNSET)

        listing_exchange = d.pop("listingExchange", UNSET)

        exchange = d.pop("exchange", UNSET)

        company_name = d.pop("companyName", UNSET)

        currency = d.pop("currency", UNSET)

        valid_exchanges = d.pop("validExchanges", UNSET)

        price_rendering = d.pop("priceRendering", UNSET)

        def _parse_maturity_date(data: object) -> Union[None, Unset, str]:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(Union[None, Unset, str], data)

        maturity_date = _parse_maturity_date(d.pop("maturityDate", UNSET))

        _right = d.pop("right", UNSET)
        right: Union[Unset, SecDefInfoResponseRight]
        if isinstance(_right, Unset):
            right = UNSET
        else:
            right = SecDefInfoResponseRight(_right)

        strike = d.pop("strike", UNSET)

        sec_def_info_response = cls(
            conid=conid,
            ticker=ticker,
            sec_type=sec_type,
            listing_exchange=listing_exchange,
            exchange=exchange,
            company_name=company_name,
            currency=currency,
            valid_exchanges=valid_exchanges,
            price_rendering=price_rendering,
            maturity_date=maturity_date,
            right=right,
            strike=strike,
        )

        sec_def_info_response.additional_properties = d
        return sec_def_info_response

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
