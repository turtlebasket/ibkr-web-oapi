import datetime
from typing import TYPE_CHECKING, Any, Dict, List, Type, TypeVar, Union

from attrs import define as _attrs_define
from attrs import field as _attrs_field
from dateutil.parser import isoparse

from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.error_response import ErrorResponse


T = TypeVar("T", bound="Au10TixDetailResponse")


@_attrs_define
class Au10TixDetailResponse:
    """
    Attributes:
        start_date (Union[Unset, datetime.datetime]):
        expiry_date (Union[Unset, datetime.datetime]):
        error (Union[Unset, ErrorResponse]):
        has_error (Union[Unset, bool]):
        error_description (Union[Unset, str]):
        url (Union[Unset, str]):
        external_id (Union[Unset, str]):
        entity_id (Union[Unset, int]):
        state (Union[Unset, str]):
    """

    start_date: Union[Unset, datetime.datetime] = UNSET
    expiry_date: Union[Unset, datetime.datetime] = UNSET
    error: Union[Unset, "ErrorResponse"] = UNSET
    has_error: Union[Unset, bool] = UNSET
    error_description: Union[Unset, str] = UNSET
    url: Union[Unset, str] = UNSET
    external_id: Union[Unset, str] = UNSET
    entity_id: Union[Unset, int] = UNSET
    state: Union[Unset, str] = UNSET
    additional_properties: Dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> Dict[str, Any]:
        start_date: Union[Unset, str] = UNSET
        if not isinstance(self.start_date, Unset):
            start_date = self.start_date.isoformat()

        expiry_date: Union[Unset, str] = UNSET
        if not isinstance(self.expiry_date, Unset):
            expiry_date = self.expiry_date.isoformat()

        error: Union[Unset, Dict[str, Any]] = UNSET
        if not isinstance(self.error, Unset):
            error = self.error.to_dict()

        has_error = self.has_error

        error_description = self.error_description

        url = self.url

        external_id = self.external_id

        entity_id = self.entity_id

        state = self.state

        field_dict: Dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if start_date is not UNSET:
            field_dict["startDate"] = start_date
        if expiry_date is not UNSET:
            field_dict["expiryDate"] = expiry_date
        if error is not UNSET:
            field_dict["error"] = error
        if has_error is not UNSET:
            field_dict["hasError"] = has_error
        if error_description is not UNSET:
            field_dict["errorDescription"] = error_description
        if url is not UNSET:
            field_dict["url"] = url
        if external_id is not UNSET:
            field_dict["externalId"] = external_id
        if entity_id is not UNSET:
            field_dict["entityId"] = entity_id
        if state is not UNSET:
            field_dict["state"] = state

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        from ..models.error_response import ErrorResponse

        d = src_dict.copy()
        _start_date = d.pop("startDate", UNSET)
        start_date: Union[Unset, datetime.datetime]
        if isinstance(_start_date, Unset):
            start_date = UNSET
        else:
            start_date = isoparse(_start_date)

        _expiry_date = d.pop("expiryDate", UNSET)
        expiry_date: Union[Unset, datetime.datetime]
        if isinstance(_expiry_date, Unset):
            expiry_date = UNSET
        else:
            expiry_date = isoparse(_expiry_date)

        _error = d.pop("error", UNSET)
        error: Union[Unset, ErrorResponse]
        if isinstance(_error, Unset):
            error = UNSET
        else:
            error = ErrorResponse.from_dict(_error)

        has_error = d.pop("hasError", UNSET)

        error_description = d.pop("errorDescription", UNSET)

        url = d.pop("url", UNSET)

        external_id = d.pop("externalId", UNSET)

        entity_id = d.pop("entityId", UNSET)

        state = d.pop("state", UNSET)

        au_10_tix_detail_response = cls(
            start_date=start_date,
            expiry_date=expiry_date,
            error=error,
            has_error=has_error,
            error_description=error_description,
            url=url,
            external_id=external_id,
            entity_id=entity_id,
            state=state,
        )

        au_10_tix_detail_response.additional_properties = d
        return au_10_tix_detail_response

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
