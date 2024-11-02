from typing import TYPE_CHECKING, Any, Dict, List, Type, TypeVar, Union

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.answer_detail import AnswerDetail


T = TypeVar("T", bound="Answer")


@_attrs_define
class Answer:
    """
    Attributes:
        answer_details (Union[Unset, List['AnswerDetail']]):
        detail (Union[Unset, str]):
        id (Union[Unset, int]):
    """

    answer_details: Union[Unset, List["AnswerDetail"]] = UNSET
    detail: Union[Unset, str] = UNSET
    id: Union[Unset, int] = UNSET
    additional_properties: Dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> Dict[str, Any]:
        answer_details: Union[Unset, List[Dict[str, Any]]] = UNSET
        if not isinstance(self.answer_details, Unset):
            answer_details = []
            for answer_details_item_data in self.answer_details:
                answer_details_item = answer_details_item_data.to_dict()
                answer_details.append(answer_details_item)

        detail = self.detail

        id = self.id

        field_dict: Dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if answer_details is not UNSET:
            field_dict["answerDetails"] = answer_details
        if detail is not UNSET:
            field_dict["detail"] = detail
        if id is not UNSET:
            field_dict["id"] = id

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        from ..models.answer_detail import AnswerDetail

        d = src_dict.copy()
        answer_details = []
        _answer_details = d.pop("answerDetails", UNSET)
        for answer_details_item_data in _answer_details or []:
            answer_details_item = AnswerDetail.from_dict(answer_details_item_data)

            answer_details.append(answer_details_item)

        detail = d.pop("detail", UNSET)

        id = d.pop("id", UNSET)

        answer = cls(
            answer_details=answer_details,
            detail=detail,
            id=id,
        )

        answer.additional_properties = d
        return answer

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
