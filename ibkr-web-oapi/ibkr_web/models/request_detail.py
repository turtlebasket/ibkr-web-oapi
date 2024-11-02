from typing import Any, Dict, List, Type, TypeVar, Union

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

T = TypeVar("T", bound="RequestDetail")


@_attrs_define
class RequestDetail:
    """
    Attributes:
        request_id (Union[Unset, int]):
        date_submitted (Union[Unset, str]):
        status (Union[Unset, str]):
        account_id (Union[Unset, str]):
        request_type (Union[Unset, str]):
    """

    request_id: Union[Unset, int] = UNSET
    date_submitted: Union[Unset, str] = UNSET
    status: Union[Unset, str] = UNSET
    account_id: Union[Unset, str] = UNSET
    request_type: Union[Unset, str] = UNSET
    additional_properties: Dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> Dict[str, Any]:
        request_id = self.request_id

        date_submitted = self.date_submitted

        status = self.status

        account_id = self.account_id

        request_type = self.request_type

        field_dict: Dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if request_id is not UNSET:
            field_dict["requestId"] = request_id
        if date_submitted is not UNSET:
            field_dict["dateSubmitted"] = date_submitted
        if status is not UNSET:
            field_dict["status"] = status
        if account_id is not UNSET:
            field_dict["accountID"] = account_id
        if request_type is not UNSET:
            field_dict["requestType"] = request_type

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        d = src_dict.copy()
        request_id = d.pop("requestId", UNSET)

        date_submitted = d.pop("dateSubmitted", UNSET)

        status = d.pop("status", UNSET)

        account_id = d.pop("accountID", UNSET)

        request_type = d.pop("requestType", UNSET)

        request_detail = cls(
            request_id=request_id,
            date_submitted=date_submitted,
            status=status,
            account_id=account_id,
            request_type=request_type,
        )

        request_detail.additional_properties = d
        return request_detail

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
