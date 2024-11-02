import datetime
from typing import Any, Dict, List, Type, TypeVar, Union

from attrs import define as _attrs_define
from attrs import field as _attrs_field
from dateutil.parser import isoparse

from ..types import UNSET, Unset

T = TypeVar("T", bound="LoginMessage")


@_attrs_define
class LoginMessage:
    """
    Attributes:
        record_date (Union[Unset, datetime.datetime]):
        id (Union[Unset, int]):
        username (Union[Unset, str]):
        message_type (Union[Unset, str]):
        content_id (Union[Unset, int]):
        state (Union[Unset, str]):
        description (Union[Unset, str]):
    """

    record_date: Union[Unset, datetime.datetime] = UNSET
    id: Union[Unset, int] = UNSET
    username: Union[Unset, str] = UNSET
    message_type: Union[Unset, str] = UNSET
    content_id: Union[Unset, int] = UNSET
    state: Union[Unset, str] = UNSET
    description: Union[Unset, str] = UNSET
    additional_properties: Dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> Dict[str, Any]:
        record_date: Union[Unset, str] = UNSET
        if not isinstance(self.record_date, Unset):
            record_date = self.record_date.isoformat()

        id = self.id

        username = self.username

        message_type = self.message_type

        content_id = self.content_id

        state = self.state

        description = self.description

        field_dict: Dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if record_date is not UNSET:
            field_dict["recordDate"] = record_date
        if id is not UNSET:
            field_dict["id"] = id
        if username is not UNSET:
            field_dict["username"] = username
        if message_type is not UNSET:
            field_dict["messageType"] = message_type
        if content_id is not UNSET:
            field_dict["contentId"] = content_id
        if state is not UNSET:
            field_dict["state"] = state
        if description is not UNSET:
            field_dict["description"] = description

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        d = src_dict.copy()
        _record_date = d.pop("recordDate", UNSET)
        record_date: Union[Unset, datetime.datetime]
        if isinstance(_record_date, Unset):
            record_date = UNSET
        else:
            record_date = isoparse(_record_date)

        id = d.pop("id", UNSET)

        username = d.pop("username", UNSET)

        message_type = d.pop("messageType", UNSET)

        content_id = d.pop("contentId", UNSET)

        state = d.pop("state", UNSET)

        description = d.pop("description", UNSET)

        login_message = cls(
            record_date=record_date,
            id=id,
            username=username,
            message_type=message_type,
            content_id=content_id,
            state=state,
            description=description,
        )

        login_message.additional_properties = d
        return login_message

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
