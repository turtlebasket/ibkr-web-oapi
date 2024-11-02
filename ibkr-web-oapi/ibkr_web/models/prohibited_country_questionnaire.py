from typing import TYPE_CHECKING, Any, Dict, List, Type, TypeVar, Union

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.prohibited_questionnaire_detail import ProhibitedQuestionnaireDetail


T = TypeVar("T", bound="ProhibitedCountryQuestionnaire")


@_attrs_define
class ProhibitedCountryQuestionnaire:
    """
    Attributes:
        prohibited_questionnaire_details (Union[Unset, List['ProhibitedQuestionnaireDetail']]):
        reference_account_id (Union[Unset, str]):
        external_id (Union[Unset, str]):
        entity_id (Union[Unset, str]):
    """

    prohibited_questionnaire_details: Union[Unset, List["ProhibitedQuestionnaireDetail"]] = UNSET
    reference_account_id: Union[Unset, str] = UNSET
    external_id: Union[Unset, str] = UNSET
    entity_id: Union[Unset, str] = UNSET
    additional_properties: Dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> Dict[str, Any]:
        prohibited_questionnaire_details: Union[Unset, List[Dict[str, Any]]] = UNSET
        if not isinstance(self.prohibited_questionnaire_details, Unset):
            prohibited_questionnaire_details = []
            for prohibited_questionnaire_details_item_data in self.prohibited_questionnaire_details:
                prohibited_questionnaire_details_item = prohibited_questionnaire_details_item_data.to_dict()
                prohibited_questionnaire_details.append(prohibited_questionnaire_details_item)

        reference_account_id = self.reference_account_id

        external_id = self.external_id

        entity_id = self.entity_id

        field_dict: Dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if prohibited_questionnaire_details is not UNSET:
            field_dict["prohibitedQuestionnaireDetails"] = prohibited_questionnaire_details
        if reference_account_id is not UNSET:
            field_dict["referenceAccountId"] = reference_account_id
        if external_id is not UNSET:
            field_dict["externalId"] = external_id
        if entity_id is not UNSET:
            field_dict["entityId"] = entity_id

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        from ..models.prohibited_questionnaire_detail import ProhibitedQuestionnaireDetail

        d = src_dict.copy()
        prohibited_questionnaire_details = []
        _prohibited_questionnaire_details = d.pop("prohibitedQuestionnaireDetails", UNSET)
        for prohibited_questionnaire_details_item_data in _prohibited_questionnaire_details or []:
            prohibited_questionnaire_details_item = ProhibitedQuestionnaireDetail.from_dict(
                prohibited_questionnaire_details_item_data
            )

            prohibited_questionnaire_details.append(prohibited_questionnaire_details_item)

        reference_account_id = d.pop("referenceAccountId", UNSET)

        external_id = d.pop("externalId", UNSET)

        entity_id = d.pop("entityId", UNSET)

        prohibited_country_questionnaire = cls(
            prohibited_questionnaire_details=prohibited_questionnaire_details,
            reference_account_id=reference_account_id,
            external_id=external_id,
            entity_id=entity_id,
        )

        prohibited_country_questionnaire.additional_properties = d
        return prohibited_country_questionnaire

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
