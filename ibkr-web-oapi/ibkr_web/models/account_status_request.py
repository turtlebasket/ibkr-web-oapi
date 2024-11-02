import datetime
from typing import Any, Dict, List, Type, TypeVar, Union

from attrs import define as _attrs_define
from attrs import field as _attrs_field
from dateutil.parser import isoparse

from ..models.account_status_request_status import AccountStatusRequestStatus
from ..types import UNSET, Unset

T = TypeVar("T", bound="AccountStatusRequest")


@_attrs_define
class AccountStatusRequest:
    """
    Attributes:
        start_date (datetime.date):
        end_date (datetime.date):
        offset (Union[Unset, int]):
        limit (Union[Unset, int]):
        status (Union[Unset, AccountStatusRequestStatus]):
    """

    start_date: datetime.date
    end_date: datetime.date
    offset: Union[Unset, int] = UNSET
    limit: Union[Unset, int] = UNSET
    status: Union[Unset, AccountStatusRequestStatus] = UNSET
    additional_properties: Dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> Dict[str, Any]:
        start_date = self.start_date.isoformat()

        end_date = self.end_date.isoformat()

        offset = self.offset

        limit = self.limit

        status: Union[Unset, str] = UNSET
        if not isinstance(self.status, Unset):
            status = self.status.value

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

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        d = src_dict.copy()
        start_date = isoparse(d.pop("startDate")).date()

        end_date = isoparse(d.pop("endDate")).date()

        offset = d.pop("offset", UNSET)

        limit = d.pop("limit", UNSET)

        _status = d.pop("status", UNSET)
        status: Union[Unset, AccountStatusRequestStatus]
        if isinstance(_status, Unset):
            status = UNSET
        else:
            status = AccountStatusRequestStatus(_status)

        account_status_request = cls(
            start_date=start_date,
            end_date=end_date,
            offset=offset,
            limit=limit,
            status=status,
        )

        account_status_request.additional_properties = d
        return account_status_request

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
