from typing import Any, Dict, List, Type, TypeVar, Union

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

T = TypeVar("T", bound="AmRequestStatusResponse")


@_attrs_define
class AmRequestStatusResponse:
    """
    Attributes:
        request_id (Union[Unset, str]):
        request_type (Union[Unset, str]):
        status (Union[Unset, str]):
        message (Union[Unset, str]):
        acct_id (Union[Unset, str]):
    """

    request_id: Union[Unset, str] = UNSET
    request_type: Union[Unset, str] = UNSET
    status: Union[Unset, str] = UNSET
    message: Union[Unset, str] = UNSET
    acct_id: Union[Unset, str] = UNSET
    additional_properties: Dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> Dict[str, Any]:
        request_id = self.request_id

        request_type = self.request_type

        status = self.status

        message = self.message

        acct_id = self.acct_id

        field_dict: Dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if request_id is not UNSET:
            field_dict["requestId"] = request_id
        if request_type is not UNSET:
            field_dict["requestType"] = request_type
        if status is not UNSET:
            field_dict["status"] = status
        if message is not UNSET:
            field_dict["message"] = message
        if acct_id is not UNSET:
            field_dict["acctId"] = acct_id

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        d = src_dict.copy()
        request_id = d.pop("requestId", UNSET)

        request_type = d.pop("requestType", UNSET)

        status = d.pop("status", UNSET)

        message = d.pop("message", UNSET)

        acct_id = d.pop("acctId", UNSET)

        am_request_status_response = cls(
            request_id=request_id,
            request_type=request_type,
            status=status,
            message=message,
            acct_id=acct_id,
        )

        am_request_status_response.additional_properties = d
        return am_request_status_response

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
