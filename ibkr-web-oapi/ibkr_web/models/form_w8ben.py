from typing import TYPE_CHECKING, Any, Dict, List, Type, TypeVar, Union

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..models.form_w8ben_explanation import FormW8BENExplanation
from ..models.form_w8ben_signature_type import FormW8BENSignatureType
from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.local_tax_form import LocalTaxForm


T = TypeVar("T", bound="FormW8BEN")


@_attrs_define
class FormW8BEN:
    """
    Attributes:
        local_tax_forms (Union[Unset, List['LocalTaxForm']]):
        name (Union[Unset, str]):
        tin (Union[Unset, str]):
        foreign_tax_id (Union[Unset, str]):
        tin_or_explanation_required (Union[Unset, bool]):
        explanation (Union[Unset, FormW8BENExplanation]):
        reference_number (Union[Unset, int]):
        part_29a_country (Union[Unset, str]):
        cert (Union[Unset, bool]):
        signature_type (Union[Unset, FormW8BENSignatureType]):
        blank_form (Union[Unset, bool]):
        tax_form_file (Union[Unset, str]):
        proprietary_form_number (Union[Unset, int]):
        electronic_format (Union[Unset, bool]):
        submit_date (Union[Unset, str]):
    """

    local_tax_forms: Union[Unset, List["LocalTaxForm"]] = UNSET
    name: Union[Unset, str] = UNSET
    tin: Union[Unset, str] = UNSET
    foreign_tax_id: Union[Unset, str] = UNSET
    tin_or_explanation_required: Union[Unset, bool] = UNSET
    explanation: Union[Unset, FormW8BENExplanation] = UNSET
    reference_number: Union[Unset, int] = UNSET
    part_29a_country: Union[Unset, str] = UNSET
    cert: Union[Unset, bool] = UNSET
    signature_type: Union[Unset, FormW8BENSignatureType] = UNSET
    blank_form: Union[Unset, bool] = UNSET
    tax_form_file: Union[Unset, str] = UNSET
    proprietary_form_number: Union[Unset, int] = UNSET
    electronic_format: Union[Unset, bool] = UNSET
    submit_date: Union[Unset, str] = UNSET
    additional_properties: Dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> Dict[str, Any]:
        local_tax_forms: Union[Unset, List[Dict[str, Any]]] = UNSET
        if not isinstance(self.local_tax_forms, Unset):
            local_tax_forms = []
            for local_tax_forms_item_data in self.local_tax_forms:
                local_tax_forms_item = local_tax_forms_item_data.to_dict()
                local_tax_forms.append(local_tax_forms_item)

        name = self.name

        tin = self.tin

        foreign_tax_id = self.foreign_tax_id

        tin_or_explanation_required = self.tin_or_explanation_required

        explanation: Union[Unset, str] = UNSET
        if not isinstance(self.explanation, Unset):
            explanation = self.explanation.value

        reference_number = self.reference_number

        part_29a_country = self.part_29a_country

        cert = self.cert

        signature_type: Union[Unset, str] = UNSET
        if not isinstance(self.signature_type, Unset):
            signature_type = self.signature_type.value

        blank_form = self.blank_form

        tax_form_file = self.tax_form_file

        proprietary_form_number = self.proprietary_form_number

        electronic_format = self.electronic_format

        submit_date = self.submit_date

        field_dict: Dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if local_tax_forms is not UNSET:
            field_dict["localTaxForms"] = local_tax_forms
        if name is not UNSET:
            field_dict["name"] = name
        if tin is not UNSET:
            field_dict["tin"] = tin
        if foreign_tax_id is not UNSET:
            field_dict["foreignTaxId"] = foreign_tax_id
        if tin_or_explanation_required is not UNSET:
            field_dict["tinOrExplanationRequired"] = tin_or_explanation_required
        if explanation is not UNSET:
            field_dict["explanation"] = explanation
        if reference_number is not UNSET:
            field_dict["referenceNumber"] = reference_number
        if part_29a_country is not UNSET:
            field_dict["part29ACountry"] = part_29a_country
        if cert is not UNSET:
            field_dict["cert"] = cert
        if signature_type is not UNSET:
            field_dict["signatureType"] = signature_type
        if blank_form is not UNSET:
            field_dict["blankForm"] = blank_form
        if tax_form_file is not UNSET:
            field_dict["taxFormFile"] = tax_form_file
        if proprietary_form_number is not UNSET:
            field_dict["proprietaryFormNumber"] = proprietary_form_number
        if electronic_format is not UNSET:
            field_dict["electronicFormat"] = electronic_format
        if submit_date is not UNSET:
            field_dict["submitDate"] = submit_date

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        from ..models.local_tax_form import LocalTaxForm

        d = src_dict.copy()
        local_tax_forms = []
        _local_tax_forms = d.pop("localTaxForms", UNSET)
        for local_tax_forms_item_data in _local_tax_forms or []:
            local_tax_forms_item = LocalTaxForm.from_dict(local_tax_forms_item_data)

            local_tax_forms.append(local_tax_forms_item)

        name = d.pop("name", UNSET)

        tin = d.pop("tin", UNSET)

        foreign_tax_id = d.pop("foreignTaxId", UNSET)

        tin_or_explanation_required = d.pop("tinOrExplanationRequired", UNSET)

        _explanation = d.pop("explanation", UNSET)
        explanation: Union[Unset, FormW8BENExplanation]
        if isinstance(_explanation, Unset):
            explanation = UNSET
        else:
            explanation = FormW8BENExplanation(_explanation)

        reference_number = d.pop("referenceNumber", UNSET)

        part_29a_country = d.pop("part29ACountry", UNSET)

        cert = d.pop("cert", UNSET)

        _signature_type = d.pop("signatureType", UNSET)
        signature_type: Union[Unset, FormW8BENSignatureType]
        if isinstance(_signature_type, Unset):
            signature_type = UNSET
        else:
            signature_type = FormW8BENSignatureType(_signature_type)

        blank_form = d.pop("blankForm", UNSET)

        tax_form_file = d.pop("taxFormFile", UNSET)

        proprietary_form_number = d.pop("proprietaryFormNumber", UNSET)

        electronic_format = d.pop("electronicFormat", UNSET)

        submit_date = d.pop("submitDate", UNSET)

        form_w8ben = cls(
            local_tax_forms=local_tax_forms,
            name=name,
            tin=tin,
            foreign_tax_id=foreign_tax_id,
            tin_or_explanation_required=tin_or_explanation_required,
            explanation=explanation,
            reference_number=reference_number,
            part_29a_country=part_29a_country,
            cert=cert,
            signature_type=signature_type,
            blank_form=blank_form,
            tax_form_file=tax_form_file,
            proprietary_form_number=proprietary_form_number,
            electronic_format=electronic_format,
            submit_date=submit_date,
        )

        form_w8ben.additional_properties = d
        return form_w8ben

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
