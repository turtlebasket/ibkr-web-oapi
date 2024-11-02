from typing import Any, Dict, List, Type, TypeVar, Union

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..models.trades_response_item_is_event_trading import TradesResponseItemIsEventTrading
from ..models.trades_response_item_liquidation_trade import TradesResponseItemLiquidationTrade
from ..models.trades_response_item_sec_type import TradesResponseItemSecType
from ..models.trades_response_item_side import TradesResponseItemSide
from ..models.trades_response_item_supports_tax_opt import TradesResponseItemSupportsTaxOpt
from ..types import UNSET, Unset

T = TypeVar("T", bound="TradesResponseItem")


@_attrs_define
class TradesResponseItem:
    """Object containing details of a single execution.

    Attributes:
        execution_id (Union[Unset, str]): IB-assigned execution identifier.
        symbol (Union[Unset, str]): Symbol of the instrument involved in the execution.
        supports_tax_opt (Union[Unset, TradesResponseItemSupportsTaxOpt]): Indicates whether the order is supported by
            IB's Tax Optimization tool.
        side (Union[Unset, TradesResponseItemSide]): Side of the execution.
        order_description (Union[Unset, str]): Human-readable description of the outcome of the execution.
        trade_time (Union[Unset, str]): UTC date and time of the execution in format YYYYMMDD-hh:mm:ss.
        trade_time_r (Union[Unset, int]): Unix timestamp of the execution time in milliseconds.
        size (Union[Unset, float]): The size of the execution in units of the instrument.
        price (Union[Unset, str]): The price at which the execution occurred.
        order_ref (Union[Unset, str]): The client-provided customer order identifier. Specified via cOID during order
            submission in the Web API.
        submitter (Union[Unset, str]): The IB username that originated the order ticket against which the execution
            occurred.
        exchange (Union[Unset, str]): The exchange or other venue on which the execution occurred.
        commission (Union[Unset, str]): Commissions incurred by the execution. May also include
        net_amount (Union[Unset, float]): net_amount
        account (Union[Unset, str]): The IB account ID of the account that received the execution.
        account_code (Union[Unset, str]): The IB account ID of the account that received the execution.
        account_allocation_name (Union[Unset, str]): The IB account ID of the account that received the execution.
        company_name (Union[Unset, str]): Name of business associated with instrument, or otherwise description of
            instrument.
        contract_description_1 (Union[Unset, str]): Human-readable description of the order's instrument.
        sec_type (Union[Unset, TradesResponseItemSecType]): IB asset class identifier.
        listing_exchange (Union[Unset, str]): The primary exchange on which the instrument is listed.
        conid (Union[Unset, str]): Contract ID of the order's instrument.
        conid_ex (Union[Unset, str]): Contract ID and routing destination in format 123456@EXCHANGE.
        clearing_id (Union[Unset, str]): Identifier of the firm clearing the trade. Value is "IB" if account is cleared
            by Interactive Brokers.
        clearing_name (Union[Unset, str]): Name of the firm clearing the trade. Value is "IB" if account is cleared by
            Interactive Brokers.
        liquidation_trade (Union[Unset, TradesResponseItemLiquidationTrade]): Indicates whether the trade is the result
            of a liquidiation by IB.
        is_event_trading (Union[Unset, TradesResponseItemIsEventTrading]): Indicates whether the order ticket is an
            Event Trading order.
    """

    execution_id: Union[Unset, str] = UNSET
    symbol: Union[Unset, str] = UNSET
    supports_tax_opt: Union[Unset, TradesResponseItemSupportsTaxOpt] = UNSET
    side: Union[Unset, TradesResponseItemSide] = UNSET
    order_description: Union[Unset, str] = UNSET
    trade_time: Union[Unset, str] = UNSET
    trade_time_r: Union[Unset, int] = UNSET
    size: Union[Unset, float] = UNSET
    price: Union[Unset, str] = UNSET
    order_ref: Union[Unset, str] = UNSET
    submitter: Union[Unset, str] = UNSET
    exchange: Union[Unset, str] = UNSET
    commission: Union[Unset, str] = UNSET
    net_amount: Union[Unset, float] = UNSET
    account: Union[Unset, str] = UNSET
    account_code: Union[Unset, str] = UNSET
    account_allocation_name: Union[Unset, str] = UNSET
    company_name: Union[Unset, str] = UNSET
    contract_description_1: Union[Unset, str] = UNSET
    sec_type: Union[Unset, TradesResponseItemSecType] = UNSET
    listing_exchange: Union[Unset, str] = UNSET
    conid: Union[Unset, str] = UNSET
    conid_ex: Union[Unset, str] = UNSET
    clearing_id: Union[Unset, str] = UNSET
    clearing_name: Union[Unset, str] = UNSET
    liquidation_trade: Union[Unset, TradesResponseItemLiquidationTrade] = UNSET
    is_event_trading: Union[Unset, TradesResponseItemIsEventTrading] = UNSET
    additional_properties: Dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> Dict[str, Any]:
        execution_id = self.execution_id

        symbol = self.symbol

        supports_tax_opt: Union[Unset, str] = UNSET
        if not isinstance(self.supports_tax_opt, Unset):
            supports_tax_opt = self.supports_tax_opt.value

        side: Union[Unset, str] = UNSET
        if not isinstance(self.side, Unset):
            side = self.side.value

        order_description = self.order_description

        trade_time = self.trade_time

        trade_time_r = self.trade_time_r

        size = self.size

        price = self.price

        order_ref = self.order_ref

        submitter = self.submitter

        exchange = self.exchange

        commission = self.commission

        net_amount = self.net_amount

        account = self.account

        account_code = self.account_code

        account_allocation_name = self.account_allocation_name

        company_name = self.company_name

        contract_description_1 = self.contract_description_1

        sec_type: Union[Unset, str] = UNSET
        if not isinstance(self.sec_type, Unset):
            sec_type = self.sec_type.value

        listing_exchange = self.listing_exchange

        conid = self.conid

        conid_ex = self.conid_ex

        clearing_id = self.clearing_id

        clearing_name = self.clearing_name

        liquidation_trade: Union[Unset, str] = UNSET
        if not isinstance(self.liquidation_trade, Unset):
            liquidation_trade = self.liquidation_trade.value

        is_event_trading: Union[Unset, str] = UNSET
        if not isinstance(self.is_event_trading, Unset):
            is_event_trading = self.is_event_trading.value

        field_dict: Dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if execution_id is not UNSET:
            field_dict["execution_id"] = execution_id
        if symbol is not UNSET:
            field_dict["symbol"] = symbol
        if supports_tax_opt is not UNSET:
            field_dict["supports_tax_opt"] = supports_tax_opt
        if side is not UNSET:
            field_dict["side"] = side
        if order_description is not UNSET:
            field_dict["order_description"] = order_description
        if trade_time is not UNSET:
            field_dict["trade_time"] = trade_time
        if trade_time_r is not UNSET:
            field_dict["trade_time_r"] = trade_time_r
        if size is not UNSET:
            field_dict["size"] = size
        if price is not UNSET:
            field_dict["price"] = price
        if order_ref is not UNSET:
            field_dict["order_ref"] = order_ref
        if submitter is not UNSET:
            field_dict["submitter"] = submitter
        if exchange is not UNSET:
            field_dict["exchange"] = exchange
        if commission is not UNSET:
            field_dict["commission"] = commission
        if net_amount is not UNSET:
            field_dict["net_amount"] = net_amount
        if account is not UNSET:
            field_dict["account"] = account
        if account_code is not UNSET:
            field_dict["accountCode"] = account_code
        if account_allocation_name is not UNSET:
            field_dict["account_allocation_name"] = account_allocation_name
        if company_name is not UNSET:
            field_dict["company_name"] = company_name
        if contract_description_1 is not UNSET:
            field_dict["contract_description_1"] = contract_description_1
        if sec_type is not UNSET:
            field_dict["sec_type"] = sec_type
        if listing_exchange is not UNSET:
            field_dict["listing_exchange"] = listing_exchange
        if conid is not UNSET:
            field_dict["conid"] = conid
        if conid_ex is not UNSET:
            field_dict["conidEx"] = conid_ex
        if clearing_id is not UNSET:
            field_dict["clearing_id"] = clearing_id
        if clearing_name is not UNSET:
            field_dict["clearing_name"] = clearing_name
        if liquidation_trade is not UNSET:
            field_dict["liquidation_trade"] = liquidation_trade
        if is_event_trading is not UNSET:
            field_dict["is_event_trading"] = is_event_trading

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        d = src_dict.copy()
        execution_id = d.pop("execution_id", UNSET)

        symbol = d.pop("symbol", UNSET)

        _supports_tax_opt = d.pop("supports_tax_opt", UNSET)
        supports_tax_opt: Union[Unset, TradesResponseItemSupportsTaxOpt]
        if isinstance(_supports_tax_opt, Unset):
            supports_tax_opt = UNSET
        else:
            supports_tax_opt = TradesResponseItemSupportsTaxOpt(_supports_tax_opt)

        _side = d.pop("side", UNSET)
        side: Union[Unset, TradesResponseItemSide]
        if isinstance(_side, Unset):
            side = UNSET
        else:
            side = TradesResponseItemSide(_side)

        order_description = d.pop("order_description", UNSET)

        trade_time = d.pop("trade_time", UNSET)

        trade_time_r = d.pop("trade_time_r", UNSET)

        size = d.pop("size", UNSET)

        price = d.pop("price", UNSET)

        order_ref = d.pop("order_ref", UNSET)

        submitter = d.pop("submitter", UNSET)

        exchange = d.pop("exchange", UNSET)

        commission = d.pop("commission", UNSET)

        net_amount = d.pop("net_amount", UNSET)

        account = d.pop("account", UNSET)

        account_code = d.pop("accountCode", UNSET)

        account_allocation_name = d.pop("account_allocation_name", UNSET)

        company_name = d.pop("company_name", UNSET)

        contract_description_1 = d.pop("contract_description_1", UNSET)

        _sec_type = d.pop("sec_type", UNSET)
        sec_type: Union[Unset, TradesResponseItemSecType]
        if isinstance(_sec_type, Unset):
            sec_type = UNSET
        else:
            sec_type = TradesResponseItemSecType(_sec_type)

        listing_exchange = d.pop("listing_exchange", UNSET)

        conid = d.pop("conid", UNSET)

        conid_ex = d.pop("conidEx", UNSET)

        clearing_id = d.pop("clearing_id", UNSET)

        clearing_name = d.pop("clearing_name", UNSET)

        _liquidation_trade = d.pop("liquidation_trade", UNSET)
        liquidation_trade: Union[Unset, TradesResponseItemLiquidationTrade]
        if isinstance(_liquidation_trade, Unset):
            liquidation_trade = UNSET
        else:
            liquidation_trade = TradesResponseItemLiquidationTrade(_liquidation_trade)

        _is_event_trading = d.pop("is_event_trading", UNSET)
        is_event_trading: Union[Unset, TradesResponseItemIsEventTrading]
        if isinstance(_is_event_trading, Unset):
            is_event_trading = UNSET
        else:
            is_event_trading = TradesResponseItemIsEventTrading(_is_event_trading)

        trades_response_item = cls(
            execution_id=execution_id,
            symbol=symbol,
            supports_tax_opt=supports_tax_opt,
            side=side,
            order_description=order_description,
            trade_time=trade_time,
            trade_time_r=trade_time_r,
            size=size,
            price=price,
            order_ref=order_ref,
            submitter=submitter,
            exchange=exchange,
            commission=commission,
            net_amount=net_amount,
            account=account,
            account_code=account_code,
            account_allocation_name=account_allocation_name,
            company_name=company_name,
            contract_description_1=contract_description_1,
            sec_type=sec_type,
            listing_exchange=listing_exchange,
            conid=conid,
            conid_ex=conid_ex,
            clearing_id=clearing_id,
            clearing_name=clearing_name,
            liquidation_trade=liquidation_trade,
            is_event_trading=is_event_trading,
        )

        trades_response_item.additional_properties = d
        return trades_response_item

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
