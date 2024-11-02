from typing import Any, Dict, List, Type, TypeVar, Union

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..models.order_status_child_order_type import OrderStatusChildOrderType
from ..models.order_status_order_status import OrderStatusOrderStatus
from ..models.order_status_sec_type import OrderStatusSecType
from ..models.order_status_side import OrderStatusSide
from ..models.order_status_tif import OrderStatusTif
from ..types import UNSET, Unset

T = TypeVar("T", bound="OrderStatus")


@_attrs_define
class OrderStatus:
    """Object containing information about the status of an order ticket.

    Attributes:
        sub_type (Union[Unset, str]): Internal use only.
        request_id (Union[Unset, str]): Internal use only. IB-assigned identifier for the status request.
        server_id (Union[Unset, str]): IB-assigned meta-identifier used to associate rejected and resubmitted orders
            following Server Prompts.
        order_id (Union[Unset, int]): The IB-assigned order identifier of the order, as provided in the request path.
        conidex (Union[Unset, str]): Contract ID and routing destination in format 123456@EXCHANGE.
        conid (Union[Unset, str]): Contract ID of the order's instrument.
        symbol (Union[Unset, str]): Symbol of the order ticket's instrument.
        side (Union[Unset, OrderStatusSide]): Side of the order ticket.
        contract_description_1 (Union[Unset, str]): Human-readable description of the order's instrument.
        listing_exchange (Union[Unset, str]): Primary listing exchange of the order ticket's instrument.
        option_acct (Union[Unset, str]): Internal use only.
        company_name (Union[Unset, str]): Name of the company or asset associated with the instrument.
        size (Union[Unset, str]): Remaining unfilled size of the order ticket. Will reflect 0.0 if order is filled in
            full, cancelled, or otherwise resolved and no longer working.
        total_size (Union[Unset, str]): The total size of the order ticket.
        currency (Union[Unset, str]): The currency in which the instrument trades and executions are conducted.
        account (Union[Unset, str]): The account receiving executions against this order ticket.
        order_type (Union[Unset, str]): The order's  IB order type.
        cum_fill (Union[Unset, str]): Cumulative filled quantity of the instrument against the order ticket.
        order_status (Union[Unset, OrderStatusOrderStatus]): Status of the order ticket.
        order_ccp_status (Union[Unset, str]): IB internal order status.
        order_status_description (Union[Unset, str]): Human-readable rendering of the order's status meant for
            presentation in UI.
        tif (Union[Unset, OrderStatusTif]): Time in force of the order ticket.
        fg_color (Union[Unset, str]): Internal use. IB's UI foreground color in hex.
        bg_color (Union[Unset, str]): Internal use. IB's UI background color in hex.
        order_not_editable (Union[Unset, bool]): Indicates whether the order ticket can be modified.
        editable_fields (Union[Unset, str]): Indicates which fields of the order ticket can be modified currently.
        cannot_cancel_order (Union[Unset, bool]): Indicates whether the order ticket can be cancelled.
        deactivate_order (Union[Unset, bool]): Indicates whether the order ticket can be deactivated.
        sec_type (Union[Unset, OrderStatusSecType]): IB asset class identifier.
        available_chart_periods (Union[Unset, str]): Internal use. Indicates chart periods available for the instrument.
        order_description (Union[Unset, str]): Human-readable description of the status or current result of the order
            ticket, meant for UI presentation.
        order_description_with_contract (Union[Unset, str]): Human-readable description of the status or current result
            of the order ticket, meant for UI presentation. Includes instrument name.
        alert_active (Union[Unset, int]): Indicates that an alert is active for the order ticket.
        child_order_type (Union[Unset, OrderStatusChildOrderType]): Indicates if the order ticket is hedged, and if so,
            in what way. 0 = No hedge, A = Attached child hedge order, B = Beta/portfolio hedge
        order_clearing_account (Union[Unset, str]): The IB account to which the order ticket clears.
        size_and_fills (Union[Unset, str]): A string reflecting the cumulative fills and total size of the order.
        exit_strategy_display_price (Union[Unset, str]): Internal use. The UI-displayed price associated with a Client
            Portal exist strategy.
        exit_strategy_chart_description (Union[Unset, str]): Internal use. A string describing an active Client Portal
            exit strategy, or the result of its execution.
        average_price (Union[Unset, str]): Average price of fills against the order, if any.
        exit_strategy_tool_availability (Union[Unset, str]): Internal use. Indicates the availability of Client Portal
            exit strategy tool for the order.
        allowed_duplicate_opposite (Union[Unset, bool]): Indicates whether an identical order on the opposite side can
            be placed.
        order_time (Union[Unset, str]): Time of the order's submission in format YYMMDDhhmmss.
    """

    sub_type: Union[Unset, str] = UNSET
    request_id: Union[Unset, str] = UNSET
    server_id: Union[Unset, str] = UNSET
    order_id: Union[Unset, int] = UNSET
    conidex: Union[Unset, str] = UNSET
    conid: Union[Unset, str] = UNSET
    symbol: Union[Unset, str] = UNSET
    side: Union[Unset, OrderStatusSide] = UNSET
    contract_description_1: Union[Unset, str] = UNSET
    listing_exchange: Union[Unset, str] = UNSET
    option_acct: Union[Unset, str] = UNSET
    company_name: Union[Unset, str] = UNSET
    size: Union[Unset, str] = UNSET
    total_size: Union[Unset, str] = UNSET
    currency: Union[Unset, str] = UNSET
    account: Union[Unset, str] = UNSET
    order_type: Union[Unset, str] = UNSET
    cum_fill: Union[Unset, str] = UNSET
    order_status: Union[Unset, OrderStatusOrderStatus] = UNSET
    order_ccp_status: Union[Unset, str] = UNSET
    order_status_description: Union[Unset, str] = UNSET
    tif: Union[Unset, OrderStatusTif] = UNSET
    fg_color: Union[Unset, str] = UNSET
    bg_color: Union[Unset, str] = UNSET
    order_not_editable: Union[Unset, bool] = UNSET
    editable_fields: Union[Unset, str] = UNSET
    cannot_cancel_order: Union[Unset, bool] = UNSET
    deactivate_order: Union[Unset, bool] = UNSET
    sec_type: Union[Unset, OrderStatusSecType] = UNSET
    available_chart_periods: Union[Unset, str] = UNSET
    order_description: Union[Unset, str] = UNSET
    order_description_with_contract: Union[Unset, str] = UNSET
    alert_active: Union[Unset, int] = UNSET
    child_order_type: Union[Unset, OrderStatusChildOrderType] = UNSET
    order_clearing_account: Union[Unset, str] = UNSET
    size_and_fills: Union[Unset, str] = UNSET
    exit_strategy_display_price: Union[Unset, str] = UNSET
    exit_strategy_chart_description: Union[Unset, str] = UNSET
    average_price: Union[Unset, str] = UNSET
    exit_strategy_tool_availability: Union[Unset, str] = UNSET
    allowed_duplicate_opposite: Union[Unset, bool] = UNSET
    order_time: Union[Unset, str] = UNSET
    additional_properties: Dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> Dict[str, Any]:
        sub_type = self.sub_type

        request_id = self.request_id

        server_id = self.server_id

        order_id = self.order_id

        conidex = self.conidex

        conid = self.conid

        symbol = self.symbol

        side: Union[Unset, str] = UNSET
        if not isinstance(self.side, Unset):
            side = self.side.value

        contract_description_1 = self.contract_description_1

        listing_exchange = self.listing_exchange

        option_acct = self.option_acct

        company_name = self.company_name

        size = self.size

        total_size = self.total_size

        currency = self.currency

        account = self.account

        order_type = self.order_type

        cum_fill = self.cum_fill

        order_status: Union[Unset, str] = UNSET
        if not isinstance(self.order_status, Unset):
            order_status = self.order_status.value

        order_ccp_status = self.order_ccp_status

        order_status_description = self.order_status_description

        tif: Union[Unset, str] = UNSET
        if not isinstance(self.tif, Unset):
            tif = self.tif.value

        fg_color = self.fg_color

        bg_color = self.bg_color

        order_not_editable = self.order_not_editable

        editable_fields = self.editable_fields

        cannot_cancel_order = self.cannot_cancel_order

        deactivate_order = self.deactivate_order

        sec_type: Union[Unset, str] = UNSET
        if not isinstance(self.sec_type, Unset):
            sec_type = self.sec_type.value

        available_chart_periods = self.available_chart_periods

        order_description = self.order_description

        order_description_with_contract = self.order_description_with_contract

        alert_active = self.alert_active

        child_order_type: Union[Unset, str] = UNSET
        if not isinstance(self.child_order_type, Unset):
            child_order_type = self.child_order_type.value

        order_clearing_account = self.order_clearing_account

        size_and_fills = self.size_and_fills

        exit_strategy_display_price = self.exit_strategy_display_price

        exit_strategy_chart_description = self.exit_strategy_chart_description

        average_price = self.average_price

        exit_strategy_tool_availability = self.exit_strategy_tool_availability

        allowed_duplicate_opposite = self.allowed_duplicate_opposite

        order_time = self.order_time

        field_dict: Dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if sub_type is not UNSET:
            field_dict["sub_type"] = sub_type
        if request_id is not UNSET:
            field_dict["request_id"] = request_id
        if server_id is not UNSET:
            field_dict["server_id"] = server_id
        if order_id is not UNSET:
            field_dict["order_id"] = order_id
        if conidex is not UNSET:
            field_dict["conidex"] = conidex
        if conid is not UNSET:
            field_dict["conid"] = conid
        if symbol is not UNSET:
            field_dict["symbol"] = symbol
        if side is not UNSET:
            field_dict["side"] = side
        if contract_description_1 is not UNSET:
            field_dict["contract_description_1"] = contract_description_1
        if listing_exchange is not UNSET:
            field_dict["listing_exchange"] = listing_exchange
        if option_acct is not UNSET:
            field_dict["option_acct"] = option_acct
        if company_name is not UNSET:
            field_dict["company_name"] = company_name
        if size is not UNSET:
            field_dict["size"] = size
        if total_size is not UNSET:
            field_dict["total_size"] = total_size
        if currency is not UNSET:
            field_dict["currency"] = currency
        if account is not UNSET:
            field_dict["account"] = account
        if order_type is not UNSET:
            field_dict["order_type"] = order_type
        if cum_fill is not UNSET:
            field_dict["cum_fill"] = cum_fill
        if order_status is not UNSET:
            field_dict["order_status"] = order_status
        if order_ccp_status is not UNSET:
            field_dict["order_ccp_status"] = order_ccp_status
        if order_status_description is not UNSET:
            field_dict["order_status_description"] = order_status_description
        if tif is not UNSET:
            field_dict["tif"] = tif
        if fg_color is not UNSET:
            field_dict["fgColor"] = fg_color
        if bg_color is not UNSET:
            field_dict["bgColor"] = bg_color
        if order_not_editable is not UNSET:
            field_dict["order_not_editable"] = order_not_editable
        if editable_fields is not UNSET:
            field_dict["editable_fields"] = editable_fields
        if cannot_cancel_order is not UNSET:
            field_dict["cannot_cancel_order"] = cannot_cancel_order
        if deactivate_order is not UNSET:
            field_dict["deactivate_order"] = deactivate_order
        if sec_type is not UNSET:
            field_dict["sec_type"] = sec_type
        if available_chart_periods is not UNSET:
            field_dict["available_chart_periods"] = available_chart_periods
        if order_description is not UNSET:
            field_dict["order_description"] = order_description
        if order_description_with_contract is not UNSET:
            field_dict["order_description_with_contract"] = order_description_with_contract
        if alert_active is not UNSET:
            field_dict["alert_active"] = alert_active
        if child_order_type is not UNSET:
            field_dict["child_order_type"] = child_order_type
        if order_clearing_account is not UNSET:
            field_dict["order_clearing_account"] = order_clearing_account
        if size_and_fills is not UNSET:
            field_dict["size_and_fills"] = size_and_fills
        if exit_strategy_display_price is not UNSET:
            field_dict["exit_strategy_display_price"] = exit_strategy_display_price
        if exit_strategy_chart_description is not UNSET:
            field_dict["exit_strategy_chart_description"] = exit_strategy_chart_description
        if average_price is not UNSET:
            field_dict["average_price"] = average_price
        if exit_strategy_tool_availability is not UNSET:
            field_dict["exit_strategy_tool_availability"] = exit_strategy_tool_availability
        if allowed_duplicate_opposite is not UNSET:
            field_dict["allowed_duplicate_opposite"] = allowed_duplicate_opposite
        if order_time is not UNSET:
            field_dict["order_time"] = order_time

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        d = src_dict.copy()
        sub_type = d.pop("sub_type", UNSET)

        request_id = d.pop("request_id", UNSET)

        server_id = d.pop("server_id", UNSET)

        order_id = d.pop("order_id", UNSET)

        conidex = d.pop("conidex", UNSET)

        conid = d.pop("conid", UNSET)

        symbol = d.pop("symbol", UNSET)

        _side = d.pop("side", UNSET)
        side: Union[Unset, OrderStatusSide]
        if isinstance(_side, Unset):
            side = UNSET
        else:
            side = OrderStatusSide(_side)

        contract_description_1 = d.pop("contract_description_1", UNSET)

        listing_exchange = d.pop("listing_exchange", UNSET)

        option_acct = d.pop("option_acct", UNSET)

        company_name = d.pop("company_name", UNSET)

        size = d.pop("size", UNSET)

        total_size = d.pop("total_size", UNSET)

        currency = d.pop("currency", UNSET)

        account = d.pop("account", UNSET)

        order_type = d.pop("order_type", UNSET)

        cum_fill = d.pop("cum_fill", UNSET)

        _order_status = d.pop("order_status", UNSET)
        order_status: Union[Unset, OrderStatusOrderStatus]
        if isinstance(_order_status, Unset):
            order_status = UNSET
        else:
            order_status = OrderStatusOrderStatus(_order_status)

        order_ccp_status = d.pop("order_ccp_status", UNSET)

        order_status_description = d.pop("order_status_description", UNSET)

        _tif = d.pop("tif", UNSET)
        tif: Union[Unset, OrderStatusTif]
        if isinstance(_tif, Unset):
            tif = UNSET
        else:
            tif = OrderStatusTif(_tif)

        fg_color = d.pop("fgColor", UNSET)

        bg_color = d.pop("bgColor", UNSET)

        order_not_editable = d.pop("order_not_editable", UNSET)

        editable_fields = d.pop("editable_fields", UNSET)

        cannot_cancel_order = d.pop("cannot_cancel_order", UNSET)

        deactivate_order = d.pop("deactivate_order", UNSET)

        _sec_type = d.pop("sec_type", UNSET)
        sec_type: Union[Unset, OrderStatusSecType]
        if isinstance(_sec_type, Unset):
            sec_type = UNSET
        else:
            sec_type = OrderStatusSecType(_sec_type)

        available_chart_periods = d.pop("available_chart_periods", UNSET)

        order_description = d.pop("order_description", UNSET)

        order_description_with_contract = d.pop("order_description_with_contract", UNSET)

        alert_active = d.pop("alert_active", UNSET)

        _child_order_type = d.pop("child_order_type", UNSET)
        child_order_type: Union[Unset, OrderStatusChildOrderType]
        if isinstance(_child_order_type, Unset):
            child_order_type = UNSET
        else:
            child_order_type = OrderStatusChildOrderType(_child_order_type)

        order_clearing_account = d.pop("order_clearing_account", UNSET)

        size_and_fills = d.pop("size_and_fills", UNSET)

        exit_strategy_display_price = d.pop("exit_strategy_display_price", UNSET)

        exit_strategy_chart_description = d.pop("exit_strategy_chart_description", UNSET)

        average_price = d.pop("average_price", UNSET)

        exit_strategy_tool_availability = d.pop("exit_strategy_tool_availability", UNSET)

        allowed_duplicate_opposite = d.pop("allowed_duplicate_opposite", UNSET)

        order_time = d.pop("order_time", UNSET)

        order_status = cls(
            sub_type=sub_type,
            request_id=request_id,
            server_id=server_id,
            order_id=order_id,
            conidex=conidex,
            conid=conid,
            symbol=symbol,
            side=side,
            contract_description_1=contract_description_1,
            listing_exchange=listing_exchange,
            option_acct=option_acct,
            company_name=company_name,
            size=size,
            total_size=total_size,
            currency=currency,
            account=account,
            order_type=order_type,
            cum_fill=cum_fill,
            order_status=order_status,
            order_ccp_status=order_ccp_status,
            order_status_description=order_status_description,
            tif=tif,
            fg_color=fg_color,
            bg_color=bg_color,
            order_not_editable=order_not_editable,
            editable_fields=editable_fields,
            cannot_cancel_order=cannot_cancel_order,
            deactivate_order=deactivate_order,
            sec_type=sec_type,
            available_chart_periods=available_chart_periods,
            order_description=order_description,
            order_description_with_contract=order_description_with_contract,
            alert_active=alert_active,
            child_order_type=child_order_type,
            order_clearing_account=order_clearing_account,
            size_and_fills=size_and_fills,
            exit_strategy_display_price=exit_strategy_display_price,
            exit_strategy_chart_description=exit_strategy_chart_description,
            average_price=average_price,
            exit_strategy_tool_availability=exit_strategy_tool_availability,
            allowed_duplicate_opposite=allowed_duplicate_opposite,
            order_time=order_time,
        )

        order_status.additional_properties = d
        return order_status

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
