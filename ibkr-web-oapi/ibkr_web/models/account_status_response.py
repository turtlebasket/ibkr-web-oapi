import datetime
from typing import Any, Dict, List, Type, TypeVar, Union

from attrs import define as _attrs_define
from attrs import field as _attrs_field
from dateutil.parser import isoparse

from ..types import UNSET, Unset

T = TypeVar("T", bound="AccountStatusResponse")


@_attrs_define
class AccountStatusResponse:
    """
    Attributes:
        date_opened (Union[Unset, datetime.datetime]):
        date_started (Union[Unset, datetime.datetime]):
        date_closed (Union[Unset, datetime.datetime]):
        account_id (Union[Unset, str]):
        status (Union[Unset, str]):
        description (Union[Unset, str]):
        master_account_id (Union[Unset, str]):
        state (Union[Unset, str]):
    """

    date_opened: Union[Unset, datetime.datetime] = UNSET
    date_started: Union[Unset, datetime.datetime] = UNSET
    date_closed: Union[Unset, datetime.datetime] = UNSET
    account_id: Union[Unset, str] = UNSET
    status: Union[Unset, str] = UNSET
    description: Union[Unset, str] = UNSET
    master_account_id: Union[Unset, str] = UNSET
    state: Union[Unset, str] = UNSET
    additional_properties: Dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> Dict[str, Any]:
        date_opened: Union[Unset, str] = UNSET
        if not isinstance(self.date_opened, Unset):
            date_opened = self.date_opened.isoformat()

        date_started: Union[Unset, str] = UNSET
        if not isinstance(self.date_started, Unset):
            date_started = self.date_started.isoformat()

        date_closed: Union[Unset, str] = UNSET
        if not isinstance(self.date_closed, Unset):
            date_closed = self.date_closed.isoformat()

        account_id = self.account_id

        status = self.status

        description = self.description

        master_account_id = self.master_account_id

        state = self.state

        field_dict: Dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if date_opened is not UNSET:
            field_dict["dateOpened"] = date_opened
        if date_started is not UNSET:
            field_dict["dateStarted"] = date_started
        if date_closed is not UNSET:
            field_dict["dateClosed"] = date_closed
        if account_id is not UNSET:
            field_dict["accountId"] = account_id
        if status is not UNSET:
            field_dict["status"] = status
        if description is not UNSET:
            field_dict["description"] = description
        if master_account_id is not UNSET:
            field_dict["masterAccountId"] = master_account_id
        if state is not UNSET:
            field_dict["state"] = state

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        d = src_dict.copy()
        _date_opened = d.pop("dateOpened", UNSET)
        date_opened: Union[Unset, datetime.datetime]
        if isinstance(_date_opened, Unset):
            date_opened = UNSET
        else:
            date_opened = isoparse(_date_opened)

        _date_started = d.pop("dateStarted", UNSET)
        date_started: Union[Unset, datetime.datetime]
        if isinstance(_date_started, Unset):
            date_started = UNSET
        else:
            date_started = isoparse(_date_started)

        _date_closed = d.pop("dateClosed", UNSET)
        date_closed: Union[Unset, datetime.datetime]
        if isinstance(_date_closed, Unset):
            date_closed = UNSET
        else:
            date_closed = isoparse(_date_closed)

        account_id = d.pop("accountId", UNSET)

        status = d.pop("status", UNSET)

        description = d.pop("description", UNSET)

        master_account_id = d.pop("masterAccountId", UNSET)

        state = d.pop("state", UNSET)

        account_status_response = cls(
            date_opened=date_opened,
            date_started=date_started,
            date_closed=date_closed,
            account_id=account_id,
            status=status,
            description=description,
            master_account_id=master_account_id,
            state=state,
        )

        account_status_response.additional_properties = d
        return account_status_response

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
