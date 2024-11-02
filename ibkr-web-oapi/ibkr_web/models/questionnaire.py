from typing import TYPE_CHECKING, Any, Dict, List, Type, TypeVar, Union

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.answer import Answer


T = TypeVar("T", bound="Questionnaire")


@_attrs_define
class Questionnaire:
    """
    Attributes:
        answers (Union[Unset, List['Answer']]):
        form_number (Union[Unset, int]):
    """

    answers: Union[Unset, List["Answer"]] = UNSET
    form_number: Union[Unset, int] = UNSET
    additional_properties: Dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> Dict[str, Any]:
        answers: Union[Unset, List[Dict[str, Any]]] = UNSET
        if not isinstance(self.answers, Unset):
            answers = []
            for answers_item_data in self.answers:
                answers_item = answers_item_data.to_dict()
                answers.append(answers_item)

        form_number = self.form_number

        field_dict: Dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if answers is not UNSET:
            field_dict["answers"] = answers
        if form_number is not UNSET:
            field_dict["formNumber"] = form_number

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        from ..models.answer import Answer

        d = src_dict.copy()
        answers = []
        _answers = d.pop("answers", UNSET)
        for answers_item_data in _answers or []:
            answers_item = Answer.from_dict(answers_item_data)

            answers.append(answers_item)

        form_number = d.pop("formNumber", UNSET)

        questionnaire = cls(
            answers=answers,
            form_number=form_number,
        )

        questionnaire.additional_properties = d
        return questionnaire

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
