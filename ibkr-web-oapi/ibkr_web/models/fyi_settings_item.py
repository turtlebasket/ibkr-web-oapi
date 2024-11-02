from typing import Any, Dict, List, Type, TypeVar, Union

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

T = TypeVar("T", bound="FyiSettingsItem")


@_attrs_define
class FyiSettingsItem:
    """
    Attributes:
        a (Union[Unset, int]): Returns ony if the subscription can be disabled/enabled manually. See
            /fyi/settings/{typecode} for how to enable/disable.
        fc (Union[Unset, str]): Fyi code for enabling or disabling the notification.
        h (Union[Unset, int]): Disclaimer if the notification was read.
        fd (Union[Unset, str]): Returns a detailed description of the topic.
        fn (Union[Unset, str]): Returns a human readable title for the notification.
    """

    a: Union[Unset, int] = UNSET
    fc: Union[Unset, str] = UNSET
    h: Union[Unset, int] = UNSET
    fd: Union[Unset, str] = UNSET
    fn: Union[Unset, str] = UNSET
    additional_properties: Dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> Dict[str, Any]:
        a = self.a

        fc = self.fc

        h = self.h

        fd = self.fd

        fn = self.fn

        field_dict: Dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if a is not UNSET:
            field_dict["A"] = a
        if fc is not UNSET:
            field_dict["FC"] = fc
        if h is not UNSET:
            field_dict["H"] = h
        if fd is not UNSET:
            field_dict["FD"] = fd
        if fn is not UNSET:
            field_dict["FN"] = fn

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        d = src_dict.copy()
        a = d.pop("A", UNSET)

        fc = d.pop("FC", UNSET)

        h = d.pop("H", UNSET)

        fd = d.pop("FD", UNSET)

        fn = d.pop("FN", UNSET)

        fyi_settings_item = cls(
            a=a,
            fc=fc,
            h=h,
            fd=fd,
            fn=fn,
        )

        fyi_settings_item.additional_properties = d
        return fyi_settings_item

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
