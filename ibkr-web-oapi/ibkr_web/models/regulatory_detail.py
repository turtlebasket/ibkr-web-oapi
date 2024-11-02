from typing import Any, Dict, List, Type, TypeVar, Union

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..models.regulatory_detail_code import RegulatoryDetailCode
from ..types import UNSET, Unset

T = TypeVar("T", bound="RegulatoryDetail")


@_attrs_define
class RegulatoryDetail:
    """
    Attributes:
        code (Union[Unset, RegulatoryDetailCode]):
        status (Union[Unset, bool]):
        details (Union[Unset, str]):
        detail (Union[Unset, str]):
        external_individual_id (Union[Unset, str]):
    """

    code: Union[Unset, RegulatoryDetailCode] = UNSET
    status: Union[Unset, bool] = UNSET
    details: Union[Unset, str] = UNSET
    detail: Union[Unset, str] = UNSET
    external_individual_id: Union[Unset, str] = UNSET
    additional_properties: Dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> Dict[str, Any]:
        code: Union[Unset, str] = UNSET
        if not isinstance(self.code, Unset):
            code = self.code.value

        status = self.status

        details = self.details

        detail = self.detail

        external_individual_id = self.external_individual_id

        field_dict: Dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if code is not UNSET:
            field_dict["code"] = code
        if status is not UNSET:
            field_dict["status"] = status
        if details is not UNSET:
            field_dict["details"] = details
        if detail is not UNSET:
            field_dict["detail"] = detail
        if external_individual_id is not UNSET:
            field_dict["externalIndividualId"] = external_individual_id

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        d = src_dict.copy()
        _code = d.pop("code", UNSET)
        code: Union[Unset, RegulatoryDetailCode]
        if isinstance(_code, Unset):
            code = UNSET
        else:
            code = RegulatoryDetailCode(_code)

        status = d.pop("status", UNSET)

        details = d.pop("details", UNSET)

        detail = d.pop("detail", UNSET)

        external_individual_id = d.pop("externalIndividualId", UNSET)

        regulatory_detail = cls(
            code=code,
            status=status,
            details=details,
            detail=detail,
            external_individual_id=external_individual_id,
        )

        regulatory_detail.additional_properties = d
        return regulatory_detail

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
