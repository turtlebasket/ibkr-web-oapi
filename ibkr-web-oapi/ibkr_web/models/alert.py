from typing import Any, Dict, List, Type, TypeVar, Union

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

T = TypeVar("T", bound="Alert")


@_attrs_define
class Alert:
    """An array containing all alerts as separate objects.

    Attributes:
        order_id (Union[Unset, int]): The order id (alert id)
        account (Union[Unset, str]): The account the alert was attributed to.
        alert_name (Union[Unset, str]): The requested name for the alert.
        alert_active (Union[Unset, int]): Determines if the alert is active [1] or not [0]
        order_time (Union[Unset, str]): UTC-formatted time of the alert’s creation.
        alert_triggered (Union[Unset, bool]): Confirms if the order is triggered or not.
        alert_repeatable (Union[Unset, int]): Confirms if the alert is enabled to occur more than once.
    """

    order_id: Union[Unset, int] = UNSET
    account: Union[Unset, str] = UNSET
    alert_name: Union[Unset, str] = UNSET
    alert_active: Union[Unset, int] = UNSET
    order_time: Union[Unset, str] = UNSET
    alert_triggered: Union[Unset, bool] = UNSET
    alert_repeatable: Union[Unset, int] = UNSET
    additional_properties: Dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> Dict[str, Any]:
        order_id = self.order_id

        account = self.account

        alert_name = self.alert_name

        alert_active = self.alert_active

        order_time = self.order_time

        alert_triggered = self.alert_triggered

        alert_repeatable = self.alert_repeatable

        field_dict: Dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if order_id is not UNSET:
            field_dict["order_id"] = order_id
        if account is not UNSET:
            field_dict["account"] = account
        if alert_name is not UNSET:
            field_dict["alert_name"] = alert_name
        if alert_active is not UNSET:
            field_dict["alert_active"] = alert_active
        if order_time is not UNSET:
            field_dict["order_time"] = order_time
        if alert_triggered is not UNSET:
            field_dict["alert_triggered"] = alert_triggered
        if alert_repeatable is not UNSET:
            field_dict["alert_repeatable"] = alert_repeatable

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        d = src_dict.copy()
        order_id = d.pop("order_id", UNSET)

        account = d.pop("account", UNSET)

        alert_name = d.pop("alert_name", UNSET)

        alert_active = d.pop("alert_active", UNSET)

        order_time = d.pop("order_time", UNSET)

        alert_triggered = d.pop("alert_triggered", UNSET)

        alert_repeatable = d.pop("alert_repeatable", UNSET)

        alert = cls(
            order_id=order_id,
            account=account,
            alert_name=alert_name,
            alert_active=alert_active,
            order_time=order_time,
            alert_triggered=alert_triggered,
            alert_repeatable=alert_repeatable,
        )

        alert.additional_properties = d
        return alert

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
