from typing import TYPE_CHECKING, Any, Dict, List, Type, TypeVar, Union

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.questionnaire import Questionnaire


T = TypeVar("T", bound="Questionnaires")


@_attrs_define
class Questionnaires:
    """
    Attributes:
        questionnaire (Union[Unset, List['Questionnaire']]):
        reference_account_id (Union[Unset, str]):
    """

    questionnaire: Union[Unset, List["Questionnaire"]] = UNSET
    reference_account_id: Union[Unset, str] = UNSET
    additional_properties: Dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> Dict[str, Any]:
        questionnaire: Union[Unset, List[Dict[str, Any]]] = UNSET
        if not isinstance(self.questionnaire, Unset):
            questionnaire = []
            for questionnaire_item_data in self.questionnaire:
                questionnaire_item = questionnaire_item_data.to_dict()
                questionnaire.append(questionnaire_item)

        reference_account_id = self.reference_account_id

        field_dict: Dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if questionnaire is not UNSET:
            field_dict["questionnaire"] = questionnaire
        if reference_account_id is not UNSET:
            field_dict["referenceAccountId"] = reference_account_id

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        from ..models.questionnaire import Questionnaire

        d = src_dict.copy()
        questionnaire = []
        _questionnaire = d.pop("questionnaire", UNSET)
        for questionnaire_item_data in _questionnaire or []:
            questionnaire_item = Questionnaire.from_dict(questionnaire_item_data)

            questionnaire.append(questionnaire_item)

        reference_account_id = d.pop("referenceAccountId", UNSET)

        questionnaires = cls(
            questionnaire=questionnaire,
            reference_account_id=reference_account_id,
        )

        questionnaires.additional_properties = d
        return questionnaires

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
