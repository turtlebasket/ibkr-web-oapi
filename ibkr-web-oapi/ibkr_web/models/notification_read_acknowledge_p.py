from typing import Any, Dict, List, Type, TypeVar, Union

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

T = TypeVar("T", bound="NotificationReadAcknowledgeP")


@_attrs_define
class NotificationReadAcknowledgeP:
    """Returns details about the notification read status.

    Attributes:
        r (Union[Unset, int]): Returns if the message was read (1) or unread (0).
        id (Union[Unset, str]): Returns the ID for the notification.
    """

    r: Union[Unset, int] = UNSET
    id: Union[Unset, str] = UNSET
    additional_properties: Dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> Dict[str, Any]:
        r = self.r

        id = self.id

        field_dict: Dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if r is not UNSET:
            field_dict["R"] = r
        if id is not UNSET:
            field_dict["ID"] = id

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        d = src_dict.copy()
        r = d.pop("R", UNSET)

        id = d.pop("ID", UNSET)

        notification_read_acknowledge_p = cls(
            r=r,
            id=id,
        )

        notification_read_acknowledge_p.additional_properties = d
        return notification_read_acknowledge_p

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
