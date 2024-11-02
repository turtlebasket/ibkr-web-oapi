from typing import Any, Dict, List, Type, TypeVar, Union

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

T = TypeVar("T", bound="NotificationsItem")


@_attrs_define
class NotificationsItem:
    """
    Attributes:
        d (Union[Unset, str]): Notification date as an epoch string.
        id (Union[Unset, str]): Unique way to reference the notification.
        fc (Union[Unset, str]): FYI code, we can use it to find whether the disclaimer is accepted or not in settings
        md (Union[Unset, str]): Content of notification.
        ms (Union[Unset, str]): Title of notification.
        r (Union[Unset, str]): Return if the notification was read or not. Value Format: 0: Disabled; 1: Enabled.
    """

    d: Union[Unset, str] = UNSET
    id: Union[Unset, str] = UNSET
    fc: Union[Unset, str] = UNSET
    md: Union[Unset, str] = UNSET
    ms: Union[Unset, str] = UNSET
    r: Union[Unset, str] = UNSET
    additional_properties: Dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> Dict[str, Any]:
        d = self.d

        id = self.id

        fc = self.fc

        md = self.md

        ms = self.ms

        r = self.r

        field_dict: Dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if d is not UNSET:
            field_dict["D"] = d
        if id is not UNSET:
            field_dict["ID"] = id
        if fc is not UNSET:
            field_dict["FC"] = fc
        if md is not UNSET:
            field_dict["MD"] = md
        if ms is not UNSET:
            field_dict["MS"] = ms
        if r is not UNSET:
            field_dict["R"] = r

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        d = src_dict.copy()
        d = d.pop("D", UNSET)

        id = d.pop("ID", UNSET)

        fc = d.pop("FC", UNSET)

        md = d.pop("MD", UNSET)

        ms = d.pop("MS", UNSET)

        r = d.pop("R", UNSET)

        notifications_item = cls(
            d=d,
            id=id,
            fc=fc,
            md=md,
            ms=ms,
            r=r,
        )

        notifications_item.additional_properties = d
        return notifications_item

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
