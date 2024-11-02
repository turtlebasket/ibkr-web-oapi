from typing import Any, Dict, List, Type, TypeVar, Union

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..models.prohibited_questionnaire_detail_code import ProhibitedQuestionnaireDetailCode
from ..types import UNSET, Unset

T = TypeVar("T", bound="ProhibitedQuestionnaireDetail")


@_attrs_define
class ProhibitedQuestionnaireDetail:
    """
    Attributes:
        code (Union[Unset, ProhibitedQuestionnaireDetailCode]):
        status (Union[Unset, bool]):
        details (Union[Unset, str]):
    """

    code: Union[Unset, ProhibitedQuestionnaireDetailCode] = UNSET
    status: Union[Unset, bool] = UNSET
    details: Union[Unset, str] = UNSET
    additional_properties: Dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> Dict[str, Any]:
        code: Union[Unset, str] = UNSET
        if not isinstance(self.code, Unset):
            code = self.code.value

        status = self.status

        details = self.details

        field_dict: Dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if code is not UNSET:
            field_dict["code"] = code
        if status is not UNSET:
            field_dict["status"] = status
        if details is not UNSET:
            field_dict["details"] = details

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        d = src_dict.copy()
        _code = d.pop("code", UNSET)
        code: Union[Unset, ProhibitedQuestionnaireDetailCode]
        if isinstance(_code, Unset):
            code = UNSET
        else:
            code = ProhibitedQuestionnaireDetailCode(_code)

        status = d.pop("status", UNSET)

        details = d.pop("details", UNSET)

        prohibited_questionnaire_detail = cls(
            code=code,
            status=status,
            details=details,
        )

        prohibited_questionnaire_detail.additional_properties = d
        return prohibited_questionnaire_detail

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
