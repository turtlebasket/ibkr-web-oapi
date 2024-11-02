from typing import TYPE_CHECKING, Any, Dict, List, Type, TypeVar, Union

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..models.update_w8ben_input_language import UpdateW8BENInputLanguage
from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.document import Document
    from ..models.tax_payer_details import TaxPayerDetails


T = TypeVar("T", bound="UpdateW8BEN")


@_attrs_define
class UpdateW8BEN:
    """
    Attributes:
        tax_payer_details (Union[Unset, TaxPayerDetails]):
        documents (Union[Unset, List['Document']]):
        input_language (Union[Unset, UpdateW8BENInputLanguage]):
        translation (Union[Unset, bool]):
        reference_account_id (Union[Unset, str]):
    """

    tax_payer_details: Union[Unset, "TaxPayerDetails"] = UNSET
    documents: Union[Unset, List["Document"]] = UNSET
    input_language: Union[Unset, UpdateW8BENInputLanguage] = UNSET
    translation: Union[Unset, bool] = UNSET
    reference_account_id: Union[Unset, str] = UNSET
    additional_properties: Dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> Dict[str, Any]:
        tax_payer_details: Union[Unset, Dict[str, Any]] = UNSET
        if not isinstance(self.tax_payer_details, Unset):
            tax_payer_details = self.tax_payer_details.to_dict()

        documents: Union[Unset, List[Dict[str, Any]]] = UNSET
        if not isinstance(self.documents, Unset):
            documents = []
            for documents_item_data in self.documents:
                documents_item = documents_item_data.to_dict()
                documents.append(documents_item)

        input_language: Union[Unset, str] = UNSET
        if not isinstance(self.input_language, Unset):
            input_language = self.input_language.value

        translation = self.translation

        reference_account_id = self.reference_account_id

        field_dict: Dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if tax_payer_details is not UNSET:
            field_dict["taxPayerDetails"] = tax_payer_details
        if documents is not UNSET:
            field_dict["documents"] = documents
        if input_language is not UNSET:
            field_dict["inputLanguage"] = input_language
        if translation is not UNSET:
            field_dict["translation"] = translation
        if reference_account_id is not UNSET:
            field_dict["referenceAccountId"] = reference_account_id

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        from ..models.document import Document
        from ..models.tax_payer_details import TaxPayerDetails

        d = src_dict.copy()
        _tax_payer_details = d.pop("taxPayerDetails", UNSET)
        tax_payer_details: Union[Unset, TaxPayerDetails]
        if isinstance(_tax_payer_details, Unset):
            tax_payer_details = UNSET
        else:
            tax_payer_details = TaxPayerDetails.from_dict(_tax_payer_details)

        documents = []
        _documents = d.pop("documents", UNSET)
        for documents_item_data in _documents or []:
            documents_item = Document.from_dict(documents_item_data)

            documents.append(documents_item)

        _input_language = d.pop("inputLanguage", UNSET)
        input_language: Union[Unset, UpdateW8BENInputLanguage]
        if isinstance(_input_language, Unset):
            input_language = UNSET
        else:
            input_language = UpdateW8BENInputLanguage(_input_language)

        translation = d.pop("translation", UNSET)

        reference_account_id = d.pop("referenceAccountId", UNSET)

        update_w8ben = cls(
            tax_payer_details=tax_payer_details,
            documents=documents,
            input_language=input_language,
            translation=translation,
            reference_account_id=reference_account_id,
        )

        update_w8ben.additional_properties = d
        return update_w8ben

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
