from typing import Any, Dict, List, Type, TypeVar, Union

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

T = TypeVar("T", bound="PostIserverNotificationBody")


@_attrs_define
class PostIserverNotificationBody:
    """
    Attributes:
        order_id (Union[Unset, int]): IB-assigned order identifier obtained from the ntf websocket message that
            delivered the server prompt. Example: 987654321.
        req_id (Union[Unset, str]): IB-assigned request identifier obtained from the ntf websocket message that
            delivered the server prompt. Example: 12345.
        text (Union[Unset, str]): The selected value from the "options" array delivered in the server prompt ntf
            websocket message. Example: Yes.
    """

    order_id: Union[Unset, int] = UNSET
    req_id: Union[Unset, str] = UNSET
    text: Union[Unset, str] = UNSET
    additional_properties: Dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> Dict[str, Any]:
        order_id = self.order_id

        req_id = self.req_id

        text = self.text

        field_dict: Dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if order_id is not UNSET:
            field_dict["orderId"] = order_id
        if req_id is not UNSET:
            field_dict["reqId"] = req_id
        if text is not UNSET:
            field_dict["text"] = text

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        d = src_dict.copy()
        order_id = d.pop("orderId", UNSET)

        req_id = d.pop("reqId", UNSET)

        text = d.pop("text", UNSET)

        post_iserver_notification_body = cls(
            order_id=order_id,
            req_id=req_id,
            text=text,
        )

        post_iserver_notification_body.additional_properties = d
        return post_iserver_notification_body

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
