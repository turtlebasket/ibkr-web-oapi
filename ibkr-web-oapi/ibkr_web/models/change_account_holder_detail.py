from typing import TYPE_CHECKING, Any, Dict, List, Type, TypeVar, Union

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..models.change_account_holder_detail_input_language import ChangeAccountHolderDetailInputLanguage
from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.associated_individual import AssociatedIndividual
    from ..models.document_submission import DocumentSubmission


T = TypeVar("T", bound="ChangeAccountHolderDetail")


@_attrs_define
class ChangeAccountHolderDetail:
    """
    Attributes:
        new_account_holder_details (Union[Unset, List['AssociatedIndividual']]):
        documents (Union[Unset, DocumentSubmission]):
        reference_account_id (Union[Unset, str]):
        reference_user_name (Union[Unset, str]):
        input_language (Union[Unset, ChangeAccountHolderDetailInputLanguage]):
        translation (Union[Unset, bool]):
    """

    new_account_holder_details: Union[Unset, List["AssociatedIndividual"]] = UNSET
    documents: Union[Unset, "DocumentSubmission"] = UNSET
    reference_account_id: Union[Unset, str] = UNSET
    reference_user_name: Union[Unset, str] = UNSET
    input_language: Union[Unset, ChangeAccountHolderDetailInputLanguage] = UNSET
    translation: Union[Unset, bool] = UNSET
    additional_properties: Dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> Dict[str, Any]:
        new_account_holder_details: Union[Unset, List[Dict[str, Any]]] = UNSET
        if not isinstance(self.new_account_holder_details, Unset):
            new_account_holder_details = []
            for new_account_holder_details_item_data in self.new_account_holder_details:
                new_account_holder_details_item = new_account_holder_details_item_data.to_dict()
                new_account_holder_details.append(new_account_holder_details_item)

        documents: Union[Unset, Dict[str, Any]] = UNSET
        if not isinstance(self.documents, Unset):
            documents = self.documents.to_dict()

        reference_account_id = self.reference_account_id

        reference_user_name = self.reference_user_name

        input_language: Union[Unset, str] = UNSET
        if not isinstance(self.input_language, Unset):
            input_language = self.input_language.value

        translation = self.translation

        field_dict: Dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if new_account_holder_details is not UNSET:
            field_dict["newAccountHolderDetails"] = new_account_holder_details
        if documents is not UNSET:
            field_dict["documents"] = documents
        if reference_account_id is not UNSET:
            field_dict["referenceAccountId"] = reference_account_id
        if reference_user_name is not UNSET:
            field_dict["referenceUserName"] = reference_user_name
        if input_language is not UNSET:
            field_dict["inputLanguage"] = input_language
        if translation is not UNSET:
            field_dict["translation"] = translation

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        from ..models.associated_individual import AssociatedIndividual
        from ..models.document_submission import DocumentSubmission

        d = src_dict.copy()
        new_account_holder_details = []
        _new_account_holder_details = d.pop("newAccountHolderDetails", UNSET)
        for new_account_holder_details_item_data in _new_account_holder_details or []:
            new_account_holder_details_item = AssociatedIndividual.from_dict(new_account_holder_details_item_data)

            new_account_holder_details.append(new_account_holder_details_item)

        _documents = d.pop("documents", UNSET)
        documents: Union[Unset, DocumentSubmission]
        if isinstance(_documents, Unset):
            documents = UNSET
        else:
            documents = DocumentSubmission.from_dict(_documents)

        reference_account_id = d.pop("referenceAccountId", UNSET)

        reference_user_name = d.pop("referenceUserName", UNSET)

        _input_language = d.pop("inputLanguage", UNSET)
        input_language: Union[Unset, ChangeAccountHolderDetailInputLanguage]
        if isinstance(_input_language, Unset):
            input_language = UNSET
        else:
            input_language = ChangeAccountHolderDetailInputLanguage(_input_language)

        translation = d.pop("translation", UNSET)

        change_account_holder_detail = cls(
            new_account_holder_details=new_account_holder_details,
            documents=documents,
            reference_account_id=reference_account_id,
            reference_user_name=reference_user_name,
            input_language=input_language,
            translation=translation,
        )

        change_account_holder_detail.additional_properties = d
        return change_account_holder_detail

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
