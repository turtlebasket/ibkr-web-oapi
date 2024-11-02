from typing import TYPE_CHECKING, Any, Dict, List, Type, TypeVar, Union

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.notification_read_acknowledge_p import NotificationReadAcknowledgeP


T = TypeVar("T", bound="NotificationReadAcknowledge")


@_attrs_define
class NotificationReadAcknowledge:
    """
    Attributes:
        v (Union[Unset, int]): Returns 1 to state message was acknowledged.
        t (Union[Unset, int]): Returns the time in ms to complete the edit.
        p (Union[Unset, NotificationReadAcknowledgeP]): Returns details about the notification read status.
    """

    v: Union[Unset, int] = UNSET
    t: Union[Unset, int] = UNSET
    p: Union[Unset, "NotificationReadAcknowledgeP"] = UNSET
    additional_properties: Dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> Dict[str, Any]:
        v = self.v

        t = self.t

        p: Union[Unset, Dict[str, Any]] = UNSET
        if not isinstance(self.p, Unset):
            p = self.p.to_dict()

        field_dict: Dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if v is not UNSET:
            field_dict["V"] = v
        if t is not UNSET:
            field_dict["T"] = t
        if p is not UNSET:
            field_dict["P"] = p

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        from ..models.notification_read_acknowledge_p import NotificationReadAcknowledgeP

        d = src_dict.copy()
        v = d.pop("V", UNSET)

        t = d.pop("T", UNSET)

        _p = d.pop("P", UNSET)
        p: Union[Unset, NotificationReadAcknowledgeP]
        if isinstance(_p, Unset):
            p = UNSET
        else:
            p = NotificationReadAcknowledgeP.from_dict(_p)

        notification_read_acknowledge = cls(
            v=v,
            t=t,
            p=p,
        )

        notification_read_acknowledge.additional_properties = d
        return notification_read_acknowledge

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
