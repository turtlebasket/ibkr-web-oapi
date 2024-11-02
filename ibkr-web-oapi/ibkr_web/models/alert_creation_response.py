from typing import Any, Dict, List, Type, TypeVar, Union

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

T = TypeVar("T", bound="AlertCreationResponse")


@_attrs_define
class AlertCreationResponse:
    """
    Attributes:
        request_id (Union[Unset, int]): Not applicable
        order_id (Union[Unset, int]): The tracking number of the alert. Alert identifier internally referenced as order
            id.
        success (Union[Unset, bool]): Displays result status of alert request
        text (Union[Unset, str]): Response message to clarify submission status.
        order_status (Union[Unset, str]): Not applicable
        warning_message (Union[Unset, str]): Returns ‘null’
    """

    request_id: Union[Unset, int] = UNSET
    order_id: Union[Unset, int] = UNSET
    success: Union[Unset, bool] = UNSET
    text: Union[Unset, str] = UNSET
    order_status: Union[Unset, str] = UNSET
    warning_message: Union[Unset, str] = UNSET
    additional_properties: Dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> Dict[str, Any]:
        request_id = self.request_id

        order_id = self.order_id

        success = self.success

        text = self.text

        order_status = self.order_status

        warning_message = self.warning_message

        field_dict: Dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if request_id is not UNSET:
            field_dict["request_id"] = request_id
        if order_id is not UNSET:
            field_dict["order_id"] = order_id
        if success is not UNSET:
            field_dict["success"] = success
        if text is not UNSET:
            field_dict["text"] = text
        if order_status is not UNSET:
            field_dict["order_status"] = order_status
        if warning_message is not UNSET:
            field_dict["warning_message"] = warning_message

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        d = src_dict.copy()
        request_id = d.pop("request_id", UNSET)

        order_id = d.pop("order_id", UNSET)

        success = d.pop("success", UNSET)

        text = d.pop("text", UNSET)

        order_status = d.pop("order_status", UNSET)

        warning_message = d.pop("warning_message", UNSET)

        alert_creation_response = cls(
            request_id=request_id,
            order_id=order_id,
            success=success,
            text=text,
            order_status=order_status,
            warning_message=warning_message,
        )

        alert_creation_response.additional_properties = d
        return alert_creation_response

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
