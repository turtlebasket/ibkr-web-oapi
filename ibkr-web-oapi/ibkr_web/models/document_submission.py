from typing import TYPE_CHECKING, Any, Dict, List, Type, TypeVar, Union

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..models.document_submission_input_language import DocumentSubmissionInputLanguage
from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.document import Document


T = TypeVar("T", bound="DocumentSubmission")


@_attrs_define
class DocumentSubmission:
    """
    Attributes:
        documents (Union[Unset, List['Document']]):
        reference_account_id (Union[Unset, str]):
        input_language (Union[Unset, DocumentSubmissionInputLanguage]):
        translation (Union[Unset, bool]):
    """

    documents: Union[Unset, List["Document"]] = UNSET
    reference_account_id: Union[Unset, str] = UNSET
    input_language: Union[Unset, DocumentSubmissionInputLanguage] = UNSET
    translation: Union[Unset, bool] = UNSET
    additional_properties: Dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> Dict[str, Any]:
        documents: Union[Unset, List[Dict[str, Any]]] = UNSET
        if not isinstance(self.documents, Unset):
            documents = []
            for documents_item_data in self.documents:
                documents_item = documents_item_data.to_dict()
                documents.append(documents_item)

        reference_account_id = self.reference_account_id

        input_language: Union[Unset, str] = UNSET
        if not isinstance(self.input_language, Unset):
            input_language = self.input_language.value

        translation = self.translation

        field_dict: Dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if documents is not UNSET:
            field_dict["documents"] = documents
        if reference_account_id is not UNSET:
            field_dict["referenceAccountId"] = reference_account_id
        if input_language is not UNSET:
            field_dict["inputLanguage"] = input_language
        if translation is not UNSET:
            field_dict["translation"] = translation

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        from ..models.document import Document

        d = src_dict.copy()
        documents = []
        _documents = d.pop("documents", UNSET)
        for documents_item_data in _documents or []:
            documents_item = Document.from_dict(documents_item_data)

            documents.append(documents_item)

        reference_account_id = d.pop("referenceAccountId", UNSET)

        _input_language = d.pop("inputLanguage", UNSET)
        input_language: Union[Unset, DocumentSubmissionInputLanguage]
        if isinstance(_input_language, Unset):
            input_language = UNSET
        else:
            input_language = DocumentSubmissionInputLanguage(_input_language)

        translation = d.pop("translation", UNSET)

        document_submission = cls(
            documents=documents,
            reference_account_id=reference_account_id,
            input_language=input_language,
            translation=translation,
        )

        document_submission.additional_properties = d
        return document_submission

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
