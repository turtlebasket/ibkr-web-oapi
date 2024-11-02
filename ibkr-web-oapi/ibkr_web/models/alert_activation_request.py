from typing import Any, Dict, List, Type, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

T = TypeVar("T", bound="AlertActivationRequest")


@_attrs_define
class AlertActivationRequest:
    """
    Attributes:
        alert_id (int): The alert Identifier
        alert_active (int): Set whether or not the alert should be active (1) or inactive (0).
    """

    alert_id: int
    alert_active: int
    additional_properties: Dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> Dict[str, Any]:
        alert_id = self.alert_id

        alert_active = self.alert_active

        field_dict: Dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "alertId": alert_id,
                "alertActive": alert_active,
            }
        )

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        d = src_dict.copy()
        alert_id = d.pop("alertId")

        alert_active = d.pop("alertActive")

        alert_activation_request = cls(
            alert_id=alert_id,
            alert_active=alert_active,
        )

        alert_activation_request.additional_properties = d
        return alert_activation_request

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
