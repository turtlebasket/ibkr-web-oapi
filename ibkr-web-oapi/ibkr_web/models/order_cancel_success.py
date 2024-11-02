from typing import Any, Dict, List, Type, TypeVar, Union

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..models.order_cancel_success_msg import OrderCancelSuccessMsg
from ..types import UNSET, Unset

T = TypeVar("T", bound="OrderCancelSuccess")


@_attrs_define
class OrderCancelSuccess:
    """Acknowledges IB's acceptance of the request to cancel the order. Does not report whether the cancellation can or
    will ultimately be enacted.

        Attributes:
            msg (Union[Unset, OrderCancelSuccessMsg]): Indicates success with value 'Request was submitted'
            order_id (Union[Unset, str]): IB order ID of the order ticket requested for cancellation.
            conid (Union[Unset, str]): IB contract ID of the order ticket's instrument.
            account (Union[Unset, str]): IB account to which the order was originally set to clear.
    """

    msg: Union[Unset, OrderCancelSuccessMsg] = UNSET
    order_id: Union[Unset, str] = UNSET
    conid: Union[Unset, str] = UNSET
    account: Union[Unset, str] = UNSET
    additional_properties: Dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> Dict[str, Any]:
        msg: Union[Unset, str] = UNSET
        if not isinstance(self.msg, Unset):
            msg = self.msg.value

        order_id = self.order_id

        conid = self.conid

        account = self.account

        field_dict: Dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if msg is not UNSET:
            field_dict["msg"] = msg
        if order_id is not UNSET:
            field_dict["order_id"] = order_id
        if conid is not UNSET:
            field_dict["conid"] = conid
        if account is not UNSET:
            field_dict["account"] = account

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        d = src_dict.copy()
        _msg = d.pop("msg", UNSET)
        msg: Union[Unset, OrderCancelSuccessMsg]
        if isinstance(_msg, Unset):
            msg = UNSET
        else:
            msg = OrderCancelSuccessMsg(_msg)

        order_id = d.pop("order_id", UNSET)

        conid = d.pop("conid", UNSET)

        account = d.pop("account", UNSET)

        order_cancel_success = cls(
            msg=msg,
            order_id=order_id,
            conid=conid,
            account=account,
        )

        order_cancel_success.additional_properties = d
        return order_cancel_success

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
