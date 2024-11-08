from typing import Any, Dict, List, Type, TypeVar, Union

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

T = TypeVar("T", bound="OrderSubmitSuccessItem")


@_attrs_define
class OrderSubmitSuccessItem:
    """Result of successful submission of one order ticket.

    Attributes:
        order_id (Union[Unset, str]): The order ID assigned to your order ticket by IB. Contains only numerals.
        order_status (Union[Unset, str]): Status describing where the order stands in its lifecycle.
        encrypt_message (Union[Unset, str]): Internal use only.
    """

    order_id: Union[Unset, str] = UNSET
    order_status: Union[Unset, str] = UNSET
    encrypt_message: Union[Unset, str] = UNSET
    additional_properties: Dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> Dict[str, Any]:
        order_id = self.order_id

        order_status = self.order_status

        encrypt_message = self.encrypt_message

        field_dict: Dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if order_id is not UNSET:
            field_dict["order_id"] = order_id
        if order_status is not UNSET:
            field_dict["order_status"] = order_status
        if encrypt_message is not UNSET:
            field_dict["encrypt_message"] = encrypt_message

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        d = src_dict.copy()
        order_id = d.pop("order_id", UNSET)

        order_status = d.pop("order_status", UNSET)

        encrypt_message = d.pop("encrypt_message", UNSET)

        order_submit_success_item = cls(
            order_id=order_id,
            order_status=order_status,
            encrypt_message=encrypt_message,
        )

        order_submit_success_item.additional_properties = d
        return order_submit_success_item

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
