from typing import Any, Dict, List, Type, TypeVar, Union, cast

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

T = TypeVar("T", bound="OrderReplyMessageItem")


@_attrs_define
class OrderReplyMessageItem:
    """An object containing order reply messages emitted against a single order ticket.

    Attributes:
        id (Union[Unset, str]): The replyId UUID of the order ticket's emitted order reply messages, used to confirm
            them and proceed.
        is_suppressed (Union[Unset, bool]): Internal use. Always delivers value 'false'.
        message (Union[Unset, List[str]]): An array containing the human-readable text of all order reply messages
            emitted for the order ticket.
        message_ids (Union[Unset, List[str]]): An array containing identifiers that categorize the types of order reply
            messages that have been emitted. Elements of this array are ordered so that indicies match the corresponding
            human-readable text strings in the 'message' array.
    """

    id: Union[Unset, str] = UNSET
    is_suppressed: Union[Unset, bool] = UNSET
    message: Union[Unset, List[str]] = UNSET
    message_ids: Union[Unset, List[str]] = UNSET
    additional_properties: Dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> Dict[str, Any]:
        id = self.id

        is_suppressed = self.is_suppressed

        message: Union[Unset, List[str]] = UNSET
        if not isinstance(self.message, Unset):
            message = self.message

        message_ids: Union[Unset, List[str]] = UNSET
        if not isinstance(self.message_ids, Unset):
            message_ids = self.message_ids

        field_dict: Dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if id is not UNSET:
            field_dict["id"] = id
        if is_suppressed is not UNSET:
            field_dict["isSuppressed"] = is_suppressed
        if message is not UNSET:
            field_dict["message"] = message
        if message_ids is not UNSET:
            field_dict["messageIds"] = message_ids

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        d = src_dict.copy()
        id = d.pop("id", UNSET)

        is_suppressed = d.pop("isSuppressed", UNSET)

        message = cast(List[str], d.pop("message", UNSET))

        message_ids = cast(List[str], d.pop("messageIds", UNSET))

        order_reply_message_item = cls(
            id=id,
            is_suppressed=is_suppressed,
            message=message,
            message_ids=message_ids,
        )

        order_reply_message_item.additional_properties = d
        return order_reply_message_item

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
