from typing import Any, Dict, List, Type, TypeVar, Union

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

T = TypeVar("T", bound="AlertActivationResponse")


@_attrs_define
class AlertActivationResponse:
    """
    Attributes:
        request_id (Union[Unset, int]):
        order_id (Union[Unset, int]): The tracking number of the alert. Occasssionally referenced as the alertId or
            alert_id.
        success (Union[Unset, bool]): Displays result status of alert request
        text (Union[Unset, str]): Response message to clarify success status reason.
        failure_list (Union[Unset, str]): If “success” returns false, will list failed order Ids
    """

    request_id: Union[Unset, int] = UNSET
    order_id: Union[Unset, int] = UNSET
    success: Union[Unset, bool] = UNSET
    text: Union[Unset, str] = UNSET
    failure_list: Union[Unset, str] = UNSET
    additional_properties: Dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> Dict[str, Any]:
        request_id = self.request_id

        order_id = self.order_id

        success = self.success

        text = self.text

        failure_list = self.failure_list

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
        if failure_list is not UNSET:
            field_dict["failure_list"] = failure_list

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        d = src_dict.copy()
        request_id = d.pop("request_id", UNSET)

        order_id = d.pop("order_id", UNSET)

        success = d.pop("success", UNSET)

        text = d.pop("text", UNSET)

        failure_list = d.pop("failure_list", UNSET)

        alert_activation_response = cls(
            request_id=request_id,
            order_id=order_id,
            success=success,
            text=text,
            failure_list=failure_list,
        )

        alert_activation_response.additional_properties = d
        return alert_activation_response

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
