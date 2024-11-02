from typing import TYPE_CHECKING, Any, Dict, List, Type, TypeVar, Union

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..models.update_tax_form_input_language import UpdateTaxFormInputLanguage
from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.document import Document
    from ..models.form_w8ben import FormW8BEN
    from ..models.form_w8bene import FormW8BENE
    from ..models.form_w9 import FormW9
    from ..models.local_tax_form import LocalTaxForm


T = TypeVar("T", bound="UpdateTaxForm")


@_attrs_define
class UpdateTaxForm:
    """
    Attributes:
        local_tax_forms (Union[Unset, List['LocalTaxForm']]):
        w_8_ben (Union[Unset, FormW8BEN]):
        w_8_ben_e (Union[Unset, FormW8BENE]):
        w9 (Union[Unset, FormW9]):
        translation (Union[Unset, bool]):
        input_language (Union[Unset, UpdateTaxFormInputLanguage]):
        reference_account_id (Union[Unset, str]):
        documents (Union[Unset, List['Document']]):
        entity_id (Union[Unset, str]):
        external_id (Union[Unset, str]):
    """

    local_tax_forms: Union[Unset, List["LocalTaxForm"]] = UNSET
    w_8_ben: Union[Unset, "FormW8BEN"] = UNSET
    w_8_ben_e: Union[Unset, "FormW8BENE"] = UNSET
    w9: Union[Unset, "FormW9"] = UNSET
    translation: Union[Unset, bool] = UNSET
    input_language: Union[Unset, UpdateTaxFormInputLanguage] = UNSET
    reference_account_id: Union[Unset, str] = UNSET
    documents: Union[Unset, List["Document"]] = UNSET
    entity_id: Union[Unset, str] = UNSET
    external_id: Union[Unset, str] = UNSET
    additional_properties: Dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> Dict[str, Any]:
        local_tax_forms: Union[Unset, List[Dict[str, Any]]] = UNSET
        if not isinstance(self.local_tax_forms, Unset):
            local_tax_forms = []
            for local_tax_forms_item_data in self.local_tax_forms:
                local_tax_forms_item = local_tax_forms_item_data.to_dict()
                local_tax_forms.append(local_tax_forms_item)

        w_8_ben: Union[Unset, Dict[str, Any]] = UNSET
        if not isinstance(self.w_8_ben, Unset):
            w_8_ben = self.w_8_ben.to_dict()

        w_8_ben_e: Union[Unset, Dict[str, Any]] = UNSET
        if not isinstance(self.w_8_ben_e, Unset):
            w_8_ben_e = self.w_8_ben_e.to_dict()

        w9: Union[Unset, Dict[str, Any]] = UNSET
        if not isinstance(self.w9, Unset):
            w9 = self.w9.to_dict()

        translation = self.translation

        input_language: Union[Unset, str] = UNSET
        if not isinstance(self.input_language, Unset):
            input_language = self.input_language.value

        reference_account_id = self.reference_account_id

        documents: Union[Unset, List[Dict[str, Any]]] = UNSET
        if not isinstance(self.documents, Unset):
            documents = []
            for documents_item_data in self.documents:
                documents_item = documents_item_data.to_dict()
                documents.append(documents_item)

        entity_id = self.entity_id

        external_id = self.external_id

        field_dict: Dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if local_tax_forms is not UNSET:
            field_dict["localTaxForms"] = local_tax_forms
        if w_8_ben is not UNSET:
            field_dict["w8Ben"] = w_8_ben
        if w_8_ben_e is not UNSET:
            field_dict["w8BenE"] = w_8_ben_e
        if w9 is not UNSET:
            field_dict["w9"] = w9
        if translation is not UNSET:
            field_dict["translation"] = translation
        if input_language is not UNSET:
            field_dict["inputLanguage"] = input_language
        if reference_account_id is not UNSET:
            field_dict["referenceAccountId"] = reference_account_id
        if documents is not UNSET:
            field_dict["documents"] = documents
        if entity_id is not UNSET:
            field_dict["entityId"] = entity_id
        if external_id is not UNSET:
            field_dict["externalId"] = external_id

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        from ..models.document import Document
        from ..models.form_w8ben import FormW8BEN
        from ..models.form_w8bene import FormW8BENE
        from ..models.form_w9 import FormW9
        from ..models.local_tax_form import LocalTaxForm

        d = src_dict.copy()
        local_tax_forms = []
        _local_tax_forms = d.pop("localTaxForms", UNSET)
        for local_tax_forms_item_data in _local_tax_forms or []:
            local_tax_forms_item = LocalTaxForm.from_dict(local_tax_forms_item_data)

            local_tax_forms.append(local_tax_forms_item)

        _w_8_ben = d.pop("w8Ben", UNSET)
        w_8_ben: Union[Unset, FormW8BEN]
        if isinstance(_w_8_ben, Unset):
            w_8_ben = UNSET
        else:
            w_8_ben = FormW8BEN.from_dict(_w_8_ben)

        _w_8_ben_e = d.pop("w8BenE", UNSET)
        w_8_ben_e: Union[Unset, FormW8BENE]
        if isinstance(_w_8_ben_e, Unset):
            w_8_ben_e = UNSET
        else:
            w_8_ben_e = FormW8BENE.from_dict(_w_8_ben_e)

        _w9 = d.pop("w9", UNSET)
        w9: Union[Unset, FormW9]
        if isinstance(_w9, Unset):
            w9 = UNSET
        else:
            w9 = FormW9.from_dict(_w9)

        translation = d.pop("translation", UNSET)

        _input_language = d.pop("inputLanguage", UNSET)
        input_language: Union[Unset, UpdateTaxFormInputLanguage]
        if isinstance(_input_language, Unset):
            input_language = UNSET
        else:
            input_language = UpdateTaxFormInputLanguage(_input_language)

        reference_account_id = d.pop("referenceAccountId", UNSET)

        documents = []
        _documents = d.pop("documents", UNSET)
        for documents_item_data in _documents or []:
            documents_item = Document.from_dict(documents_item_data)

            documents.append(documents_item)

        entity_id = d.pop("entityId", UNSET)

        external_id = d.pop("externalId", UNSET)

        update_tax_form = cls(
            local_tax_forms=local_tax_forms,
            w_8_ben=w_8_ben,
            w_8_ben_e=w_8_ben_e,
            w9=w9,
            translation=translation,
            input_language=input_language,
            reference_account_id=reference_account_id,
            documents=documents,
            entity_id=entity_id,
            external_id=external_id,
        )

        update_tax_form.additional_properties = d
        return update_tax_form

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
