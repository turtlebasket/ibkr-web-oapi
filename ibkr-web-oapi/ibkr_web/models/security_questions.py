from typing import TYPE_CHECKING, Any, Dict, List, Type, TypeVar, Union

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..models.security_questions_input_language import SecurityQuestionsInputLanguage
from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.details import Details


T = TypeVar("T", bound="SecurityQuestions")


@_attrs_define
class SecurityQuestions:
    """
    Attributes:
        details (Union[Unset, List['Details']]):
        reference_user_name (Union[Unset, str]):
        input_language (Union[Unset, SecurityQuestionsInputLanguage]):
    """

    details: Union[Unset, List["Details"]] = UNSET
    reference_user_name: Union[Unset, str] = UNSET
    input_language: Union[Unset, SecurityQuestionsInputLanguage] = UNSET
    additional_properties: Dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> Dict[str, Any]:
        details: Union[Unset, List[Dict[str, Any]]] = UNSET
        if not isinstance(self.details, Unset):
            details = []
            for details_item_data in self.details:
                details_item = details_item_data.to_dict()
                details.append(details_item)

        reference_user_name = self.reference_user_name

        input_language: Union[Unset, str] = UNSET
        if not isinstance(self.input_language, Unset):
            input_language = self.input_language.value

        field_dict: Dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if details is not UNSET:
            field_dict["details"] = details
        if reference_user_name is not UNSET:
            field_dict["referenceUserName"] = reference_user_name
        if input_language is not UNSET:
            field_dict["inputLanguage"] = input_language

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        from ..models.details import Details

        d = src_dict.copy()
        details = []
        _details = d.pop("details", UNSET)
        for details_item_data in _details or []:
            details_item = Details.from_dict(details_item_data)

            details.append(details_item)

        reference_user_name = d.pop("referenceUserName", UNSET)

        _input_language = d.pop("inputLanguage", UNSET)
        input_language: Union[Unset, SecurityQuestionsInputLanguage]
        if isinstance(_input_language, Unset):
            input_language = UNSET
        else:
            input_language = SecurityQuestionsInputLanguage(_input_language)

        security_questions = cls(
            details=details,
            reference_user_name=reference_user_name,
            input_language=input_language,
        )

        security_questions.additional_properties = d
        return security_questions

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
