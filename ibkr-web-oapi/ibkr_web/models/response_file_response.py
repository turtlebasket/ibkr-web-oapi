from typing import TYPE_CHECKING, Any, Dict, List, Type, TypeVar, Union

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.error_response import ErrorResponse
    from ..models.response_file_response_data import ResponseFileResponseData


T = TypeVar("T", bound="ResponseFileResponse")


@_attrs_define
class ResponseFileResponse:
    """
    Attributes:
        error (Union[Unset, ErrorResponse]):
        has_error (Union[Unset, bool]):
        error_description (Union[Unset, str]):
        is_processed (Union[Unset, bool]):
        name (Union[Unset, str]):
        data (Union[Unset, ResponseFileResponseData]):
    """

    error: Union[Unset, "ErrorResponse"] = UNSET
    has_error: Union[Unset, bool] = UNSET
    error_description: Union[Unset, str] = UNSET
    is_processed: Union[Unset, bool] = UNSET
    name: Union[Unset, str] = UNSET
    data: Union[Unset, "ResponseFileResponseData"] = UNSET
    additional_properties: Dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> Dict[str, Any]:
        error: Union[Unset, Dict[str, Any]] = UNSET
        if not isinstance(self.error, Unset):
            error = self.error.to_dict()

        has_error = self.has_error

        error_description = self.error_description

        is_processed = self.is_processed

        name = self.name

        data: Union[Unset, Dict[str, Any]] = UNSET
        if not isinstance(self.data, Unset):
            data = self.data.to_dict()

        field_dict: Dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if error is not UNSET:
            field_dict["error"] = error
        if has_error is not UNSET:
            field_dict["hasError"] = has_error
        if error_description is not UNSET:
            field_dict["errorDescription"] = error_description
        if is_processed is not UNSET:
            field_dict["isProcessed"] = is_processed
        if name is not UNSET:
            field_dict["name"] = name
        if data is not UNSET:
            field_dict["data"] = data

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        from ..models.error_response import ErrorResponse
        from ..models.response_file_response_data import ResponseFileResponseData

        d = src_dict.copy()
        _error = d.pop("error", UNSET)
        error: Union[Unset, ErrorResponse]
        if isinstance(_error, Unset):
            error = UNSET
        else:
            error = ErrorResponse.from_dict(_error)

        has_error = d.pop("hasError", UNSET)

        error_description = d.pop("errorDescription", UNSET)

        is_processed = d.pop("isProcessed", UNSET)

        name = d.pop("name", UNSET)

        _data = d.pop("data", UNSET)
        data: Union[Unset, ResponseFileResponseData]
        if isinstance(_data, Unset):
            data = UNSET
        else:
            data = ResponseFileResponseData.from_dict(_data)

        response_file_response = cls(
            error=error,
            has_error=has_error,
            error_description=error_description,
            is_processed=is_processed,
            name=name,
            data=data,
        )

        response_file_response.additional_properties = d
        return response_file_response

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
