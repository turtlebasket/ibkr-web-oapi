from typing import TYPE_CHECKING, Any, Dict, List, Type, TypeVar, Union

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.request_detail import RequestDetail


T = TypeVar("T", bound="RequestDetailsResponse")


@_attrs_define
class RequestDetailsResponse:
    """
    Attributes:
        request_details (Union[Unset, List['RequestDetail']]):
        offset (Union[Unset, int]):
        limit (Union[Unset, int]):
        total (Union[Unset, int]):
    """

    request_details: Union[Unset, List["RequestDetail"]] = UNSET
    offset: Union[Unset, int] = UNSET
    limit: Union[Unset, int] = UNSET
    total: Union[Unset, int] = UNSET
    additional_properties: Dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> Dict[str, Any]:
        request_details: Union[Unset, List[Dict[str, Any]]] = UNSET
        if not isinstance(self.request_details, Unset):
            request_details = []
            for request_details_item_data in self.request_details:
                request_details_item = request_details_item_data.to_dict()
                request_details.append(request_details_item)

        offset = self.offset

        limit = self.limit

        total = self.total

        field_dict: Dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if request_details is not UNSET:
            field_dict["requestDetails"] = request_details
        if offset is not UNSET:
            field_dict["offset"] = offset
        if limit is not UNSET:
            field_dict["limit"] = limit
        if total is not UNSET:
            field_dict["total"] = total

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        from ..models.request_detail import RequestDetail

        d = src_dict.copy()
        request_details = []
        _request_details = d.pop("requestDetails", UNSET)
        for request_details_item_data in _request_details or []:
            request_details_item = RequestDetail.from_dict(request_details_item_data)

            request_details.append(request_details_item)

        offset = d.pop("offset", UNSET)

        limit = d.pop("limit", UNSET)

        total = d.pop("total", UNSET)

        request_details_response = cls(
            request_details=request_details,
            offset=offset,
            limit=limit,
            total=total,
        )

        request_details_response.additional_properties = d
        return request_details_response

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
