from typing import Any, Dict, List, Type, TypeVar, Union

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

T = TypeVar("T", bound="FyiEnableDeviceOption")


@_attrs_define
class FyiEnableDeviceOption:
    """
    Attributes:
        device_name (Union[Unset, str]):
        device_id (Union[Unset, str]):
        ui_name (Union[Unset, str]):
        enabled (Union[Unset, bool]): enable or disable device
    """

    device_name: Union[Unset, str] = UNSET
    device_id: Union[Unset, str] = UNSET
    ui_name: Union[Unset, str] = UNSET
    enabled: Union[Unset, bool] = UNSET
    additional_properties: Dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> Dict[str, Any]:
        device_name = self.device_name

        device_id = self.device_id

        ui_name = self.ui_name

        enabled = self.enabled

        field_dict: Dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if device_name is not UNSET:
            field_dict["deviceName"] = device_name
        if device_id is not UNSET:
            field_dict["deviceId"] = device_id
        if ui_name is not UNSET:
            field_dict["uiName"] = ui_name
        if enabled is not UNSET:
            field_dict["enabled"] = enabled

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        d = src_dict.copy()
        device_name = d.pop("deviceName", UNSET)

        device_id = d.pop("deviceId", UNSET)

        ui_name = d.pop("uiName", UNSET)

        enabled = d.pop("enabled", UNSET)

        fyi_enable_device_option = cls(
            device_name=device_name,
            device_id=device_id,
            ui_name=ui_name,
            enabled=enabled,
        )

        fyi_enable_device_option.additional_properties = d
        return fyi_enable_device_option

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
