import datetime
from typing import Any, Dict, List, Type, TypeVar, Union

from attrs import define as _attrs_define
from attrs import field as _attrs_field
from dateutil.parser import isoparse

from ..models.task_request_type import TaskRequestType
from ..types import UNSET, Unset

T = TypeVar("T", bound="TaskRequest")


@_attrs_define
class TaskRequest:
    """
    Attributes:
        start_date (datetime.date):
        end_date (datetime.date):
        type (TaskRequestType):
        offset (Union[Unset, int]):
        limit (Union[Unset, int]):
        form_number (Union[Unset, int]):
    """

    start_date: datetime.date
    end_date: datetime.date
    type: TaskRequestType
    offset: Union[Unset, int] = UNSET
    limit: Union[Unset, int] = UNSET
    form_number: Union[Unset, int] = UNSET
    additional_properties: Dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> Dict[str, Any]:
        start_date = self.start_date.isoformat()

        end_date = self.end_date.isoformat()

        type = self.type.value

        offset = self.offset

        limit = self.limit

        form_number = self.form_number

        field_dict: Dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "startDate": start_date,
                "endDate": end_date,
                "type": type,
            }
        )
        if offset is not UNSET:
            field_dict["offset"] = offset
        if limit is not UNSET:
            field_dict["limit"] = limit
        if form_number is not UNSET:
            field_dict["formNumber"] = form_number

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        d = src_dict.copy()
        start_date = isoparse(d.pop("startDate")).date()

        end_date = isoparse(d.pop("endDate")).date()

        type = TaskRequestType(d.pop("type"))

        offset = d.pop("offset", UNSET)

        limit = d.pop("limit", UNSET)

        form_number = d.pop("formNumber", UNSET)

        task_request = cls(
            start_date=start_date,
            end_date=end_date,
            type=type,
            offset=offset,
            limit=limit,
            form_number=form_number,
        )

        task_request.additional_properties = d
        return task_request

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
