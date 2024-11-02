from typing import TYPE_CHECKING, Any, Dict, List, Type, TypeVar, Union

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..models.single_order_submission_request_side import SingleOrderSubmissionRequestSide
from ..models.single_order_submission_request_tif import SingleOrderSubmissionRequestTif
from ..models.single_order_submission_request_trailing_type import SingleOrderSubmissionRequestTrailingType
from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.single_order_submission_request_strategy_parameters import (
        SingleOrderSubmissionRequestStrategyParameters,
    )


T = TypeVar("T", bound="SingleOrderSubmissionRequest")


@_attrs_define
class SingleOrderSubmissionRequest:
    """A single order ticket.

    Attributes:
        conid (int): IB contract ID of the instrument.
        order_type (str): IB order type identifier.
        side (SingleOrderSubmissionRequestSide): Side of the order ticket.
        tif (SingleOrderSubmissionRequestTif): Time in force of the order ticket.
        quantity (float): Quantity of the order ticket in units of the instrument.
        acct_id (Union[Unset, str]): Receiving account of the order ticket.
        conidex (Union[Unset, str]): Contract ID and routing destination together in format 123456@EXCHANGE.
        sec_type (Union[Unset, str]): IB asset class identifier.
        c_oid (Union[Unset, str]): Client-configurable order identifier.
        parent_id (Union[Unset, str]): If the order ticket is a child order in a bracket, the parentId field must be set
            equal to the cOID provided for the parent order.
        listing_exchange (Union[Unset, str]): The listing exchange of the instrument.
        is_single_group (Union[Unset, bool]): Indicates that all orders in the containing array are to be treated as an
            OCA group.
        outside_rth (Union[Unset, bool]): Instructs IB to permit the order to execute outside of regular trading hours.
        aux_price (Union[Unset, float]): Additional price value used in certain order types, such as stop orders.
        ticker (Union[Unset, str]): Ticker symbol of the instrument.
        trailing_amt (Union[Unset, float]): Offset used with Trailing orders.
        trailing_type (Union[Unset, SingleOrderSubmissionRequestTrailingType]): Specifies the type of trailing used with
            a Trailing order.
        referrer (Union[Unset, str]): IB internal identifier for order entry UI element.
        cash_qty (Union[Unset, float]): Quantity of currency used with cash quantity orders.
        use_adaptive (Union[Unset, bool]): Instructs IB to apply the Price Management Algo.
        is_ccy_conv (Union[Unset, bool]): Indicates that a forex order is for currency conversion and should not entail
            a virtual forex position in the account, where applicable.
        price (Union[Unset, float]): Price of the order ticket, where applicable.
        strategy (Union[Unset, str]): The name of an execution algorithm.
        strategy_parameters (Union[Unset, SingleOrderSubmissionRequestStrategyParameters]): Parameters governing the
            selected algorithm, if applicable.
    """

    conid: int
    order_type: str
    side: SingleOrderSubmissionRequestSide
    tif: SingleOrderSubmissionRequestTif
    quantity: float
    acct_id: Union[Unset, str] = UNSET
    conidex: Union[Unset, str] = UNSET
    sec_type: Union[Unset, str] = UNSET
    c_oid: Union[Unset, str] = UNSET
    parent_id: Union[Unset, str] = UNSET
    listing_exchange: Union[Unset, str] = UNSET
    is_single_group: Union[Unset, bool] = UNSET
    outside_rth: Union[Unset, bool] = UNSET
    aux_price: Union[Unset, float] = UNSET
    ticker: Union[Unset, str] = UNSET
    trailing_amt: Union[Unset, float] = UNSET
    trailing_type: Union[Unset, SingleOrderSubmissionRequestTrailingType] = UNSET
    referrer: Union[Unset, str] = UNSET
    cash_qty: Union[Unset, float] = UNSET
    use_adaptive: Union[Unset, bool] = UNSET
    is_ccy_conv: Union[Unset, bool] = UNSET
    price: Union[Unset, float] = UNSET
    strategy: Union[Unset, str] = UNSET
    strategy_parameters: Union[Unset, "SingleOrderSubmissionRequestStrategyParameters"] = UNSET
    additional_properties: Dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> Dict[str, Any]:
        conid = self.conid

        order_type = self.order_type

        side = self.side.value

        tif = self.tif.value

        quantity = self.quantity

        acct_id = self.acct_id

        conidex = self.conidex

        sec_type = self.sec_type

        c_oid = self.c_oid

        parent_id = self.parent_id

        listing_exchange = self.listing_exchange

        is_single_group = self.is_single_group

        outside_rth = self.outside_rth

        aux_price = self.aux_price

        ticker = self.ticker

        trailing_amt = self.trailing_amt

        trailing_type: Union[Unset, str] = UNSET
        if not isinstance(self.trailing_type, Unset):
            trailing_type = self.trailing_type.value

        referrer = self.referrer

        cash_qty = self.cash_qty

        use_adaptive = self.use_adaptive

        is_ccy_conv = self.is_ccy_conv

        price = self.price

        strategy = self.strategy

        strategy_parameters: Union[Unset, Dict[str, Any]] = UNSET
        if not isinstance(self.strategy_parameters, Unset):
            strategy_parameters = self.strategy_parameters.to_dict()

        field_dict: Dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "conid": conid,
                "orderType": order_type,
                "side": side,
                "tif": tif,
                "quantity": quantity,
            }
        )
        if acct_id is not UNSET:
            field_dict["acctId"] = acct_id
        if conidex is not UNSET:
            field_dict["conidex"] = conidex
        if sec_type is not UNSET:
            field_dict["secType"] = sec_type
        if c_oid is not UNSET:
            field_dict["cOID"] = c_oid
        if parent_id is not UNSET:
            field_dict["parentId"] = parent_id
        if listing_exchange is not UNSET:
            field_dict["listingExchange"] = listing_exchange
        if is_single_group is not UNSET:
            field_dict["isSingleGroup"] = is_single_group
        if outside_rth is not UNSET:
            field_dict["outsideRTH"] = outside_rth
        if aux_price is not UNSET:
            field_dict["auxPrice"] = aux_price
        if ticker is not UNSET:
            field_dict["ticker"] = ticker
        if trailing_amt is not UNSET:
            field_dict["trailingAmt"] = trailing_amt
        if trailing_type is not UNSET:
            field_dict["trailingType"] = trailing_type
        if referrer is not UNSET:
            field_dict["referrer"] = referrer
        if cash_qty is not UNSET:
            field_dict["cashQty"] = cash_qty
        if use_adaptive is not UNSET:
            field_dict["useAdaptive"] = use_adaptive
        if is_ccy_conv is not UNSET:
            field_dict["isCcyConv"] = is_ccy_conv
        if price is not UNSET:
            field_dict["price"] = price
        if strategy is not UNSET:
            field_dict["strategy"] = strategy
        if strategy_parameters is not UNSET:
            field_dict["strategyParameters"] = strategy_parameters

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        from ..models.single_order_submission_request_strategy_parameters import (
            SingleOrderSubmissionRequestStrategyParameters,
        )

        d = src_dict.copy()
        conid = d.pop("conid")

        order_type = d.pop("orderType")

        side = SingleOrderSubmissionRequestSide(d.pop("side"))

        tif = SingleOrderSubmissionRequestTif(d.pop("tif"))

        quantity = d.pop("quantity")

        acct_id = d.pop("acctId", UNSET)

        conidex = d.pop("conidex", UNSET)

        sec_type = d.pop("secType", UNSET)

        c_oid = d.pop("cOID", UNSET)

        parent_id = d.pop("parentId", UNSET)

        listing_exchange = d.pop("listingExchange", UNSET)

        is_single_group = d.pop("isSingleGroup", UNSET)

        outside_rth = d.pop("outsideRTH", UNSET)

        aux_price = d.pop("auxPrice", UNSET)

        ticker = d.pop("ticker", UNSET)

        trailing_amt = d.pop("trailingAmt", UNSET)

        _trailing_type = d.pop("trailingType", UNSET)
        trailing_type: Union[Unset, SingleOrderSubmissionRequestTrailingType]
        if isinstance(_trailing_type, Unset):
            trailing_type = UNSET
        else:
            trailing_type = SingleOrderSubmissionRequestTrailingType(_trailing_type)

        referrer = d.pop("referrer", UNSET)

        cash_qty = d.pop("cashQty", UNSET)

        use_adaptive = d.pop("useAdaptive", UNSET)

        is_ccy_conv = d.pop("isCcyConv", UNSET)

        price = d.pop("price", UNSET)

        strategy = d.pop("strategy", UNSET)

        _strategy_parameters = d.pop("strategyParameters", UNSET)
        strategy_parameters: Union[Unset, SingleOrderSubmissionRequestStrategyParameters]
        if isinstance(_strategy_parameters, Unset):
            strategy_parameters = UNSET
        else:
            strategy_parameters = SingleOrderSubmissionRequestStrategyParameters.from_dict(_strategy_parameters)

        single_order_submission_request = cls(
            conid=conid,
            order_type=order_type,
            side=side,
            tif=tif,
            quantity=quantity,
            acct_id=acct_id,
            conidex=conidex,
            sec_type=sec_type,
            c_oid=c_oid,
            parent_id=parent_id,
            listing_exchange=listing_exchange,
            is_single_group=is_single_group,
            outside_rth=outside_rth,
            aux_price=aux_price,
            ticker=ticker,
            trailing_amt=trailing_amt,
            trailing_type=trailing_type,
            referrer=referrer,
            cash_qty=cash_qty,
            use_adaptive=use_adaptive,
            is_ccy_conv=is_ccy_conv,
            price=price,
            strategy=strategy,
            strategy_parameters=strategy_parameters,
        )

        single_order_submission_request.additional_properties = d
        return single_order_submission_request

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
