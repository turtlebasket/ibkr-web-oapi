import datetime
from typing import Any, Dict, List, Type, TypeVar, Union

from attrs import define as _attrs_define
from attrs import field as _attrs_field
from dateutil.parser import isoparse

from ..models.login_message_request_status import LoginMessageRequestStatus
from ..types import UNSET, Unset

T = TypeVar("T", bound="LoginMessageRequest")


@_attrs_define
class LoginMessageRequest:
    """
    Attributes:
        start_date (datetime.date):
        end_date (datetime.date):
        offset (Union[Unset, int]):
        limit (Union[Unset, int]):
        status (Union[Unset, LoginMessageRequestStatus]):
        type (Union[Unset, str]):
    """

    start_date: datetime.date
    end_date: datetime.date
    offset: Union[Unset, int] = UNSET
    limit: Union[Unset, int] = UNSET
    status: Union[Unset, LoginMessageRequestStatus] = UNSET
    type: Union[Unset, str] = UNSET
    additional_properties: Dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> Dict[str, Any]:
        start_date = self.start_date.isoformat()

        end_date = self.end_date.isoformat()

        offset = self.offset

        limit = self.limit

        status: Union[Unset, str] = UNSET
        if not isinstance(self.status, Unset):
            status = self.status.value

        type = self.type

        field_dict: Dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "startDate": start_date,
                "endDate": end_date,
            }
        )
        if offset is not UNSET:
            field_dict["offset"] = offset
        if limit is not UNSET:
            field_dict["limit"] = limit
        if status is not UNSET:
            field_dict["status"] = status
        if type is not UNSET:
            field_dict["type"] = type

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        d = src_dict.copy()
        start_date = isoparse(d.pop("startDate")).date()

        end_date = isoparse(d.pop("endDate")).date()

        offset = d.pop("offset", UNSET)

        limit = d.pop("limit", UNSET)

        _status = d.pop("status", UNSET)
        status: Union[Unset, LoginMessageRequestStatus]
        if isinstance(_status, Unset):
            status = UNSET
        else:
            status = LoginMessageRequestStatus(_status)

        type = d.pop("type", UNSET)

        login_message_request = cls(
            start_date=start_date,
            end_date=end_date,
            offset=offset,
            limit=limit,
            status=status,
            type=type,
        )

        login_message_request.additional_properties = d
        return login_message_request

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
