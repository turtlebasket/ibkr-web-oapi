from typing import TYPE_CHECKING, Any, Dict, List, Type, TypeVar, Union

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..models.alert_details_order_status import AlertDetailsOrderStatus
from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.alert_condition import AlertCondition


T = TypeVar("T", bound="AlertDetails")


@_attrs_define
class AlertDetails:
    """details of the specified alert

    Attributes:
        account (Union[Unset, str]): Requestor’s account ID
        order_id (Union[Unset, int]): Alert’s tracking ID. Can be used for modifying or deleting alerts.
        alert_name (Union[Unset, str]): Human readable name of the alert.
        tif (Union[Unset, str]): Time in Force effective for the Alert
        expire_time (Union[Unset, str]): Returns the UTC formatted date used in GTD orders.
        alert_active (Union[Unset, int]): Returns if the alert is active [1] or disabled [0].
        alert_repeatable (Union[Unset, int]): Returns if the alert can be sent more than once.
        alert_email (Union[Unset, str]): Returns the designated email address for sendMessage functionality.
        alert_send_message (Union[Unset, int]): Returns whether or not the alert will send an email.
        alert_message (Union[Unset, str]): Returns the body content of what your alert will report once triggered
        alert_show_popup (Union[Unset, int]): Returns whether or not the alert will trigger TWS Pop-up messages
        alert_play_audio (Union[Unset, int]): Returns whether or not the alert will play audio
        order_status (Union[Unset, AlertDetailsOrderStatus]): represent order statusAlways returns “Presubmitted”.
        alert_triggered (Union[Unset, int]): Returns whether or not the alert was triggered yet.
        fg_color (Union[Unset, str]): Foreground color. Not applicable to API.
        bg_color (Union[Unset, str]): Background color. Not applicable to API.
        order_not_editable (Union[Unset, bool]): Returns if the order can be edited.
        itws_orders_only (Union[Unset, int]): Returns whether or not the alert will trigger mobile notifications.
        alert_mta_currency (Union[Unset, str]): Returns currency set for MTA alerts. Only valid for alert type 8 & 9.
        alert_mta_defaults (Union[Unset, str]): Returns current MTA default values.
        tool_id (Union[Unset, int]): Tracking ID for MTA alerts only. Returns ‘null’ for standard alerts.
        time_zone (Union[Unset, str]): Returned for time-specific conditions.
        alert_default_type (Union[Unset, int]): Returns default type set for alerts. Configured in Client Portal.
        condition_size (Union[Unset, int]): Returns the total number of conditions in the alert.
        condition_outside_rth (Union[Unset, int]): Returns whether or not the alert will trigger outside of regular
            trading hours.
        conditions (Union[Unset, List['AlertCondition']]): Returns all conditions
    """

    account: Union[Unset, str] = UNSET
    order_id: Union[Unset, int] = UNSET
    alert_name: Union[Unset, str] = UNSET
    tif: Union[Unset, str] = UNSET
    expire_time: Union[Unset, str] = UNSET
    alert_active: Union[Unset, int] = UNSET
    alert_repeatable: Union[Unset, int] = UNSET
    alert_email: Union[Unset, str] = UNSET
    alert_send_message: Union[Unset, int] = UNSET
    alert_message: Union[Unset, str] = UNSET
    alert_show_popup: Union[Unset, int] = UNSET
    alert_play_audio: Union[Unset, int] = UNSET
    order_status: Union[Unset, AlertDetailsOrderStatus] = UNSET
    alert_triggered: Union[Unset, int] = UNSET
    fg_color: Union[Unset, str] = UNSET
    bg_color: Union[Unset, str] = UNSET
    order_not_editable: Union[Unset, bool] = UNSET
    itws_orders_only: Union[Unset, int] = UNSET
    alert_mta_currency: Union[Unset, str] = UNSET
    alert_mta_defaults: Union[Unset, str] = UNSET
    tool_id: Union[Unset, int] = UNSET
    time_zone: Union[Unset, str] = UNSET
    alert_default_type: Union[Unset, int] = UNSET
    condition_size: Union[Unset, int] = UNSET
    condition_outside_rth: Union[Unset, int] = UNSET
    conditions: Union[Unset, List["AlertCondition"]] = UNSET
    additional_properties: Dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> Dict[str, Any]:
        account = self.account

        order_id = self.order_id

        alert_name = self.alert_name

        tif = self.tif

        expire_time = self.expire_time

        alert_active = self.alert_active

        alert_repeatable = self.alert_repeatable

        alert_email = self.alert_email

        alert_send_message = self.alert_send_message

        alert_message = self.alert_message

        alert_show_popup = self.alert_show_popup

        alert_play_audio = self.alert_play_audio

        order_status: Union[Unset, str] = UNSET
        if not isinstance(self.order_status, Unset):
            order_status = self.order_status.value

        alert_triggered = self.alert_triggered

        fg_color = self.fg_color

        bg_color = self.bg_color

        order_not_editable = self.order_not_editable

        itws_orders_only = self.itws_orders_only

        alert_mta_currency = self.alert_mta_currency

        alert_mta_defaults = self.alert_mta_defaults

        tool_id = self.tool_id

        time_zone = self.time_zone

        alert_default_type = self.alert_default_type

        condition_size = self.condition_size

        condition_outside_rth = self.condition_outside_rth

        conditions: Union[Unset, List[Dict[str, Any]]] = UNSET
        if not isinstance(self.conditions, Unset):
            conditions = []
            for conditions_item_data in self.conditions:
                conditions_item = conditions_item_data.to_dict()
                conditions.append(conditions_item)

        field_dict: Dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if account is not UNSET:
            field_dict["account"] = account
        if order_id is not UNSET:
            field_dict["order_id"] = order_id
        if alert_name is not UNSET:
            field_dict["alertName"] = alert_name
        if tif is not UNSET:
            field_dict["tif"] = tif
        if expire_time is not UNSET:
            field_dict["expire_time"] = expire_time
        if alert_active is not UNSET:
            field_dict["alert_active"] = alert_active
        if alert_repeatable is not UNSET:
            field_dict["alert_repeatable"] = alert_repeatable
        if alert_email is not UNSET:
            field_dict["alert_email"] = alert_email
        if alert_send_message is not UNSET:
            field_dict["alert_send_message"] = alert_send_message
        if alert_message is not UNSET:
            field_dict["alert_message"] = alert_message
        if alert_show_popup is not UNSET:
            field_dict["alert_show_popup"] = alert_show_popup
        if alert_play_audio is not UNSET:
            field_dict["alert_play_audio"] = alert_play_audio
        if order_status is not UNSET:
            field_dict["order_status"] = order_status
        if alert_triggered is not UNSET:
            field_dict["alert_triggered"] = alert_triggered
        if fg_color is not UNSET:
            field_dict["fg_color"] = fg_color
        if bg_color is not UNSET:
            field_dict["bg_color"] = bg_color
        if order_not_editable is not UNSET:
            field_dict["order_not_editable"] = order_not_editable
        if itws_orders_only is not UNSET:
            field_dict["itws_orders_only"] = itws_orders_only
        if alert_mta_currency is not UNSET:
            field_dict["alert_mta_currency"] = alert_mta_currency
        if alert_mta_defaults is not UNSET:
            field_dict["alert_mta_defaults"] = alert_mta_defaults
        if tool_id is not UNSET:
            field_dict["tool_id"] = tool_id
        if time_zone is not UNSET:
            field_dict["time_zone"] = time_zone
        if alert_default_type is not UNSET:
            field_dict["alert_default_type"] = alert_default_type
        if condition_size is not UNSET:
            field_dict["condition_size"] = condition_size
        if condition_outside_rth is not UNSET:
            field_dict["condition_outside_rth"] = condition_outside_rth
        if conditions is not UNSET:
            field_dict["conditions"] = conditions

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        from ..models.alert_condition import AlertCondition

        d = src_dict.copy()
        account = d.pop("account", UNSET)

        order_id = d.pop("order_id", UNSET)

        alert_name = d.pop("alertName", UNSET)

        tif = d.pop("tif", UNSET)

        expire_time = d.pop("expire_time", UNSET)

        alert_active = d.pop("alert_active", UNSET)

        alert_repeatable = d.pop("alert_repeatable", UNSET)

        alert_email = d.pop("alert_email", UNSET)

        alert_send_message = d.pop("alert_send_message", UNSET)

        alert_message = d.pop("alert_message", UNSET)

        alert_show_popup = d.pop("alert_show_popup", UNSET)

        alert_play_audio = d.pop("alert_play_audio", UNSET)

        _order_status = d.pop("order_status", UNSET)
        order_status: Union[Unset, AlertDetailsOrderStatus]
        if isinstance(_order_status, Unset):
            order_status = UNSET
        else:
            order_status = AlertDetailsOrderStatus(_order_status)

        alert_triggered = d.pop("alert_triggered", UNSET)

        fg_color = d.pop("fg_color", UNSET)

        bg_color = d.pop("bg_color", UNSET)

        order_not_editable = d.pop("order_not_editable", UNSET)

        itws_orders_only = d.pop("itws_orders_only", UNSET)

        alert_mta_currency = d.pop("alert_mta_currency", UNSET)

        alert_mta_defaults = d.pop("alert_mta_defaults", UNSET)

        tool_id = d.pop("tool_id", UNSET)

        time_zone = d.pop("time_zone", UNSET)

        alert_default_type = d.pop("alert_default_type", UNSET)

        condition_size = d.pop("condition_size", UNSET)

        condition_outside_rth = d.pop("condition_outside_rth", UNSET)

        conditions = []
        _conditions = d.pop("conditions", UNSET)
        for conditions_item_data in _conditions or []:
            conditions_item = AlertCondition.from_dict(conditions_item_data)

            conditions.append(conditions_item)

        alert_details = cls(
            account=account,
            order_id=order_id,
            alert_name=alert_name,
            tif=tif,
            expire_time=expire_time,
            alert_active=alert_active,
            alert_repeatable=alert_repeatable,
            alert_email=alert_email,
            alert_send_message=alert_send_message,
            alert_message=alert_message,
            alert_show_popup=alert_show_popup,
            alert_play_audio=alert_play_audio,
            order_status=order_status,
            alert_triggered=alert_triggered,
            fg_color=fg_color,
            bg_color=bg_color,
            order_not_editable=order_not_editable,
            itws_orders_only=itws_orders_only,
            alert_mta_currency=alert_mta_currency,
            alert_mta_defaults=alert_mta_defaults,
            tool_id=tool_id,
            time_zone=time_zone,
            alert_default_type=alert_default_type,
            condition_size=condition_size,
            condition_outside_rth=condition_outside_rth,
            conditions=conditions,
        )

        alert_details.additional_properties = d
        return alert_details

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
