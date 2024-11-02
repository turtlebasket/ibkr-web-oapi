from typing import Any, Dict, List, Type, TypeVar, Union

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..models.live_orders_response_orders_item_is_event_trading import LiveOrdersResponseOrdersItemIsEventTrading
from ..models.live_orders_response_orders_item_status import LiveOrdersResponseOrdersItemStatus
from ..models.live_orders_response_orders_item_supports_tax_opt import LiveOrdersResponseOrdersItemSupportsTaxOpt
from ..types import UNSET, Unset

T = TypeVar("T", bound="LiveOrdersResponseOrdersItem")


@_attrs_define
class LiveOrdersResponseOrdersItem:
    """Object representing one order.

    Attributes:
        acct (Union[Unset, str]): IB account ID to which the order was placed.
        exchange (Union[Unset, str]): Routing destination of the order ticket.
        conidex (Union[Unset, str]): Contract ID and routing destination in format 123456@EXCHANGE.
        conid (Union[Unset, str]): Contract ID of the order's instrument.
        account (Union[Unset, str]): IB account ID to which the order was placed.
        order_id (Union[Unset, int]): IB-assigned order identifier.
        cash_ccy (Union[Unset, str]): Currency of the order ticket's Cash Quantity, if applicable.
        size_and_fills (Union[Unset, str]): Human-readable shorthand rendering of the filled and total quantities of the
            order.
        order_desc (Union[Unset, str]): Human-readable shorthand rendering of the order ticket.
        description1 (Union[Unset, str]): Descriptive text, or additional details that specific the instrument.
        ticker (Union[Unset, str]): Symbol or base product code of the instrument.
        sec_type (Union[Unset, str]): Asset class of the instrument.
        listing_exchange (Union[Unset, str]): Exchange on which the instrument is listed.
        remaining_quantity (Union[Unset, str]): Quantity remaining to be filled in units of the instrument.
        filled_quantity (Union[Unset, str]): Quantity filled in units of the instrument.
        total_size (Union[Unset, str]): Total size of an order in the instrument's units.
        total_cash_size (Union[Unset, str]): Total size of a cash quantity order.
        company_name (Union[Unset, str]): Name of business associated with instrument, or otherwise description of
            instrument.
        status (Union[Unset, LiveOrdersResponseOrdersItemStatus]): Status of the order ticket.
        order_ccp_status (Union[Unset, str]): IB internal order status.
        orig_order_type (Union[Unset, str]): Order type of a filled order.
        supports_tax_opt (Union[Unset, LiveOrdersResponseOrdersItemSupportsTaxOpt]): Indicates whether the order is
            supported by IB's Tax Optimization tool.
        last_execution_time (Union[Unset, str]): Time of last execution against the order in format YYMMDDhhmmss.
        order_type (Union[Unset, str]): Order type of a working order ticket.
        bg_color (Union[Unset, str]): Internal use. IB's UI background color in hex.
        fg_color (Union[Unset, str]): Internal use. IB's UI foreground color in hex.
        is_event_trading (Union[Unset, LiveOrdersResponseOrdersItemIsEventTrading]): Indicates whether the order ticket
            is an Event Trading order.
        price (Union[Unset, str]): Price of the order, if applicable to the order type.
        time_in_force (Union[Unset, str]): Time of force of the order.
        last_execution_time_r (Union[Unset, str]): Unix timestamp of the last execution against the order.
        side (Union[Unset, str]): Side of the order.
        avg_price (Union[Unset, str]): Average price of fills against the order, if any.
    """

    acct: Union[Unset, str] = UNSET
    exchange: Union[Unset, str] = UNSET
    conidex: Union[Unset, str] = UNSET
    conid: Union[Unset, str] = UNSET
    account: Union[Unset, str] = UNSET
    order_id: Union[Unset, int] = UNSET
    cash_ccy: Union[Unset, str] = UNSET
    size_and_fills: Union[Unset, str] = UNSET
    order_desc: Union[Unset, str] = UNSET
    description1: Union[Unset, str] = UNSET
    ticker: Union[Unset, str] = UNSET
    sec_type: Union[Unset, str] = UNSET
    listing_exchange: Union[Unset, str] = UNSET
    remaining_quantity: Union[Unset, str] = UNSET
    filled_quantity: Union[Unset, str] = UNSET
    total_size: Union[Unset, str] = UNSET
    total_cash_size: Union[Unset, str] = UNSET
    company_name: Union[Unset, str] = UNSET
    status: Union[Unset, LiveOrdersResponseOrdersItemStatus] = UNSET
    order_ccp_status: Union[Unset, str] = UNSET
    orig_order_type: Union[Unset, str] = UNSET
    supports_tax_opt: Union[Unset, LiveOrdersResponseOrdersItemSupportsTaxOpt] = UNSET
    last_execution_time: Union[Unset, str] = UNSET
    order_type: Union[Unset, str] = UNSET
    bg_color: Union[Unset, str] = UNSET
    fg_color: Union[Unset, str] = UNSET
    is_event_trading: Union[Unset, LiveOrdersResponseOrdersItemIsEventTrading] = UNSET
    price: Union[Unset, str] = UNSET
    time_in_force: Union[Unset, str] = UNSET
    last_execution_time_r: Union[Unset, str] = UNSET
    side: Union[Unset, str] = UNSET
    avg_price: Union[Unset, str] = UNSET
    additional_properties: Dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> Dict[str, Any]:
        acct = self.acct

        exchange = self.exchange

        conidex = self.conidex

        conid = self.conid

        account = self.account

        order_id = self.order_id

        cash_ccy = self.cash_ccy

        size_and_fills = self.size_and_fills

        order_desc = self.order_desc

        description1 = self.description1

        ticker = self.ticker

        sec_type = self.sec_type

        listing_exchange = self.listing_exchange

        remaining_quantity = self.remaining_quantity

        filled_quantity = self.filled_quantity

        total_size = self.total_size

        total_cash_size = self.total_cash_size

        company_name = self.company_name

        status: Union[Unset, str] = UNSET
        if not isinstance(self.status, Unset):
            status = self.status.value

        order_ccp_status = self.order_ccp_status

        orig_order_type = self.orig_order_type

        supports_tax_opt: Union[Unset, str] = UNSET
        if not isinstance(self.supports_tax_opt, Unset):
            supports_tax_opt = self.supports_tax_opt.value

        last_execution_time = self.last_execution_time

        order_type = self.order_type

        bg_color = self.bg_color

        fg_color = self.fg_color

        is_event_trading: Union[Unset, str] = UNSET
        if not isinstance(self.is_event_trading, Unset):
            is_event_trading = self.is_event_trading.value

        price = self.price

        time_in_force = self.time_in_force

        last_execution_time_r = self.last_execution_time_r

        side = self.side

        avg_price = self.avg_price

        field_dict: Dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if acct is not UNSET:
            field_dict["acct"] = acct
        if exchange is not UNSET:
            field_dict["exchange"] = exchange
        if conidex is not UNSET:
            field_dict["conidex"] = conidex
        if conid is not UNSET:
            field_dict["conid"] = conid
        if account is not UNSET:
            field_dict["account"] = account
        if order_id is not UNSET:
            field_dict["orderId"] = order_id
        if cash_ccy is not UNSET:
            field_dict["cashCcy"] = cash_ccy
        if size_and_fills is not UNSET:
            field_dict["sizeAndFills"] = size_and_fills
        if order_desc is not UNSET:
            field_dict["orderDesc"] = order_desc
        if description1 is not UNSET:
            field_dict["description1"] = description1
        if ticker is not UNSET:
            field_dict["ticker"] = ticker
        if sec_type is not UNSET:
            field_dict["secType"] = sec_type
        if listing_exchange is not UNSET:
            field_dict["listingExchange"] = listing_exchange
        if remaining_quantity is not UNSET:
            field_dict["remainingQuantity"] = remaining_quantity
        if filled_quantity is not UNSET:
            field_dict["filledQuantity"] = filled_quantity
        if total_size is not UNSET:
            field_dict["totalSize"] = total_size
        if total_cash_size is not UNSET:
            field_dict["totalCashSize"] = total_cash_size
        if company_name is not UNSET:
            field_dict["companyName"] = company_name
        if status is not UNSET:
            field_dict["status"] = status
        if order_ccp_status is not UNSET:
            field_dict["order_ccp_status"] = order_ccp_status
        if orig_order_type is not UNSET:
            field_dict["origOrderType"] = orig_order_type
        if supports_tax_opt is not UNSET:
            field_dict["supportsTaxOpt"] = supports_tax_opt
        if last_execution_time is not UNSET:
            field_dict["lastExecutionTime"] = last_execution_time
        if order_type is not UNSET:
            field_dict["orderType"] = order_type
        if bg_color is not UNSET:
            field_dict["bgColor"] = bg_color
        if fg_color is not UNSET:
            field_dict["fgColor"] = fg_color
        if is_event_trading is not UNSET:
            field_dict["isEventTrading"] = is_event_trading
        if price is not UNSET:
            field_dict["price"] = price
        if time_in_force is not UNSET:
            field_dict["timeInForce"] = time_in_force
        if last_execution_time_r is not UNSET:
            field_dict["lastExecutionTime_r"] = last_execution_time_r
        if side is not UNSET:
            field_dict["side"] = side
        if avg_price is not UNSET:
            field_dict["avgPrice"] = avg_price

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        d = src_dict.copy()
        acct = d.pop("acct", UNSET)

        exchange = d.pop("exchange", UNSET)

        conidex = d.pop("conidex", UNSET)

        conid = d.pop("conid", UNSET)

        account = d.pop("account", UNSET)

        order_id = d.pop("orderId", UNSET)

        cash_ccy = d.pop("cashCcy", UNSET)

        size_and_fills = d.pop("sizeAndFills", UNSET)

        order_desc = d.pop("orderDesc", UNSET)

        description1 = d.pop("description1", UNSET)

        ticker = d.pop("ticker", UNSET)

        sec_type = d.pop("secType", UNSET)

        listing_exchange = d.pop("listingExchange", UNSET)

        remaining_quantity = d.pop("remainingQuantity", UNSET)

        filled_quantity = d.pop("filledQuantity", UNSET)

        total_size = d.pop("totalSize", UNSET)

        total_cash_size = d.pop("totalCashSize", UNSET)

        company_name = d.pop("companyName", UNSET)

        _status = d.pop("status", UNSET)
        status: Union[Unset, LiveOrdersResponseOrdersItemStatus]
        if isinstance(_status, Unset):
            status = UNSET
        else:
            status = LiveOrdersResponseOrdersItemStatus(_status)

        order_ccp_status = d.pop("order_ccp_status", UNSET)

        orig_order_type = d.pop("origOrderType", UNSET)

        _supports_tax_opt = d.pop("supportsTaxOpt", UNSET)
        supports_tax_opt: Union[Unset, LiveOrdersResponseOrdersItemSupportsTaxOpt]
        if isinstance(_supports_tax_opt, Unset):
            supports_tax_opt = UNSET
        else:
            supports_tax_opt = LiveOrdersResponseOrdersItemSupportsTaxOpt(_supports_tax_opt)

        last_execution_time = d.pop("lastExecutionTime", UNSET)

        order_type = d.pop("orderType", UNSET)

        bg_color = d.pop("bgColor", UNSET)

        fg_color = d.pop("fgColor", UNSET)

        _is_event_trading = d.pop("isEventTrading", UNSET)
        is_event_trading: Union[Unset, LiveOrdersResponseOrdersItemIsEventTrading]
        if isinstance(_is_event_trading, Unset):
            is_event_trading = UNSET
        else:
            is_event_trading = LiveOrdersResponseOrdersItemIsEventTrading(_is_event_trading)

        price = d.pop("price", UNSET)

        time_in_force = d.pop("timeInForce", UNSET)

        last_execution_time_r = d.pop("lastExecutionTime_r", UNSET)

        side = d.pop("side", UNSET)

        avg_price = d.pop("avgPrice", UNSET)

        live_orders_response_orders_item = cls(
            acct=acct,
            exchange=exchange,
            conidex=conidex,
            conid=conid,
            account=account,
            order_id=order_id,
            cash_ccy=cash_ccy,
            size_and_fills=size_and_fills,
            order_desc=order_desc,
            description1=description1,
            ticker=ticker,
            sec_type=sec_type,
            listing_exchange=listing_exchange,
            remaining_quantity=remaining_quantity,
            filled_quantity=filled_quantity,
            total_size=total_size,
            total_cash_size=total_cash_size,
            company_name=company_name,
            status=status,
            order_ccp_status=order_ccp_status,
            orig_order_type=orig_order_type,
            supports_tax_opt=supports_tax_opt,
            last_execution_time=last_execution_time,
            order_type=order_type,
            bg_color=bg_color,
            fg_color=fg_color,
            is_event_trading=is_event_trading,
            price=price,
            time_in_force=time_in_force,
            last_execution_time_r=last_execution_time_r,
            side=side,
            avg_price=avg_price,
        )

        live_orders_response_orders_item.additional_properties = d
        return live_orders_response_orders_item

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
