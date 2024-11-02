from typing import TYPE_CHECKING, Any, Dict, List, Type, TypeVar, Union, cast

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.error_response import ErrorResponse


T = TypeVar("T", bound="UserNameAvailableResponse")


@_attrs_define
class UserNameAvailableResponse:
    """
    Attributes:
        error (Union[Unset, ErrorResponse]):
        has_error (Union[Unset, bool]):
        error_description (Union[Unset, str]):
        is_valid (Union[Unset, bool]):
        is_available (Union[Unset, bool]):
        suggested_user_name (Union[Unset, List[str]]):
    """

    error: Union[Unset, "ErrorResponse"] = UNSET
    has_error: Union[Unset, bool] = UNSET
    error_description: Union[Unset, str] = UNSET
    is_valid: Union[Unset, bool] = UNSET
    is_available: Union[Unset, bool] = UNSET
    suggested_user_name: Union[Unset, List[str]] = UNSET
    additional_properties: Dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> Dict[str, Any]:
        error: Union[Unset, Dict[str, Any]] = UNSET
        if not isinstance(self.error, Unset):
            error = self.error.to_dict()

        has_error = self.has_error

        error_description = self.error_description

        is_valid = self.is_valid

        is_available = self.is_available

        suggested_user_name: Union[Unset, List[str]] = UNSET
        if not isinstance(self.suggested_user_name, Unset):
            suggested_user_name = self.suggested_user_name

        field_dict: Dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if error is not UNSET:
            field_dict["error"] = error
        if has_error is not UNSET:
            field_dict["hasError"] = has_error
        if error_description is not UNSET:
            field_dict["errorDescription"] = error_description
        if is_valid is not UNSET:
            field_dict["isValid"] = is_valid
        if is_available is not UNSET:
            field_dict["isAvailable"] = is_available
        if suggested_user_name is not UNSET:
            field_dict["suggestedUserName"] = suggested_user_name

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        from ..models.error_response import ErrorResponse

        d = src_dict.copy()
        _error = d.pop("error", UNSET)
        error: Union[Unset, ErrorResponse]
        if isinstance(_error, Unset):
            error = UNSET
        else:
            error = ErrorResponse.from_dict(_error)

        has_error = d.pop("hasError", UNSET)

        error_description = d.pop("errorDescription", UNSET)

        is_valid = d.pop("isValid", UNSET)

        is_available = d.pop("isAvailable", UNSET)

        suggested_user_name = cast(List[str], d.pop("suggestedUserName", UNSET))

        user_name_available_response = cls(
            error=error,
            has_error=has_error,
            error_description=error_description,
            is_valid=is_valid,
            is_available=is_available,
            suggested_user_name=suggested_user_name,
        )

        user_name_available_response.additional_properties = d
        return user_name_available_response

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
