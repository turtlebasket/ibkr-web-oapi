from typing import Any, Dict, List, Type, TypeVar, Union

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

T = TypeVar("T", bound="RequestInfoResponse")


@_attrs_define
class RequestInfoResponse:
    """
    Attributes:
        request_id (Union[Unset, int]):
        executed_at (Union[Unset, str]):
    """

    request_id: Union[Unset, int] = UNSET
    executed_at: Union[Unset, str] = UNSET
    additional_properties: Dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> Dict[str, Any]:
        request_id = self.request_id

        executed_at = self.executed_at

        field_dict: Dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if request_id is not UNSET:
            field_dict["requestId"] = request_id
        if executed_at is not UNSET:
            field_dict["executedAt"] = executed_at

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        d = src_dict.copy()
        request_id = d.pop("requestId", UNSET)

        executed_at = d.pop("executedAt", UNSET)

        request_info_response = cls(
            request_id=request_id,
            executed_at=executed_at,
        )

        request_info_response.additional_properties = d
        return request_info_response

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
