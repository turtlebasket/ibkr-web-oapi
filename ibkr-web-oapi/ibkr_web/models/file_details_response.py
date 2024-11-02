from typing import Any, Dict, List, Type, TypeVar, Union

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

T = TypeVar("T", bound="FileDetailsResponse")


@_attrs_define
class FileDetailsResponse:
    """
    Attributes:
        account_id (Union[Unset, str]):
        request_file_name (Union[Unset, str]):
        response_file_name (Union[Unset, str]):
    """

    account_id: Union[Unset, str] = UNSET
    request_file_name: Union[Unset, str] = UNSET
    response_file_name: Union[Unset, str] = UNSET
    additional_properties: Dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> Dict[str, Any]:
        account_id = self.account_id

        request_file_name = self.request_file_name

        response_file_name = self.response_file_name

        field_dict: Dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if account_id is not UNSET:
            field_dict["accountId"] = account_id
        if request_file_name is not UNSET:
            field_dict["requestFileName"] = request_file_name
        if response_file_name is not UNSET:
            field_dict["responseFileName"] = response_file_name

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        d = src_dict.copy()
        account_id = d.pop("accountId", UNSET)

        request_file_name = d.pop("requestFileName", UNSET)

        response_file_name = d.pop("responseFileName", UNSET)

        file_details_response = cls(
            account_id=account_id,
            request_file_name=request_file_name,
            response_file_name=response_file_name,
        )

        file_details_response.additional_properties = d
        return file_details_response

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
