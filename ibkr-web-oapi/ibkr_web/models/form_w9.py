from typing import TYPE_CHECKING, Any, Dict, List, Type, TypeVar, Union

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..models.form_w9_customer_type import FormW9CustomerType
from ..models.form_w9_signature_type import FormW9SignatureType
from ..models.form_w9_tin_type import FormW9TinType
from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.local_tax_form import LocalTaxForm


T = TypeVar("T", bound="FormW9")


@_attrs_define
class FormW9:
    """
    Attributes:
        local_tax_forms (Union[Unset, List['LocalTaxForm']]):
        name (Union[Unset, str]):
        business_name (Union[Unset, str]):
        customer_type (Union[Unset, FormW9CustomerType]):
        tax_classification (Union[Unset, str]):
        other_customer_type (Union[Unset, str]):
        tin (Union[Unset, str]):
        tin_type (Union[Unset, FormW9TinType]):
        cert1 (Union[Unset, bool]):
        cert2 (Union[Unset, bool]):
        cert3 (Union[Unset, bool]):
        cert4 (Union[Unset, bool]):
        signature_type (Union[Unset, FormW9SignatureType]):
        blank_form (Union[Unset, bool]):
        tax_form_file (Union[Unset, str]):
        proprietary_form_number (Union[Unset, int]):
    """

    local_tax_forms: Union[Unset, List["LocalTaxForm"]] = UNSET
    name: Union[Unset, str] = UNSET
    business_name: Union[Unset, str] = UNSET
    customer_type: Union[Unset, FormW9CustomerType] = UNSET
    tax_classification: Union[Unset, str] = UNSET
    other_customer_type: Union[Unset, str] = UNSET
    tin: Union[Unset, str] = UNSET
    tin_type: Union[Unset, FormW9TinType] = UNSET
    cert1: Union[Unset, bool] = UNSET
    cert2: Union[Unset, bool] = UNSET
    cert3: Union[Unset, bool] = UNSET
    cert4: Union[Unset, bool] = UNSET
    signature_type: Union[Unset, FormW9SignatureType] = UNSET
    blank_form: Union[Unset, bool] = UNSET
    tax_form_file: Union[Unset, str] = UNSET
    proprietary_form_number: Union[Unset, int] = UNSET
    additional_properties: Dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> Dict[str, Any]:
        local_tax_forms: Union[Unset, List[Dict[str, Any]]] = UNSET
        if not isinstance(self.local_tax_forms, Unset):
            local_tax_forms = []
            for local_tax_forms_item_data in self.local_tax_forms:
                local_tax_forms_item = local_tax_forms_item_data.to_dict()
                local_tax_forms.append(local_tax_forms_item)

        name = self.name

        business_name = self.business_name

        customer_type: Union[Unset, str] = UNSET
        if not isinstance(self.customer_type, Unset):
            customer_type = self.customer_type.value

        tax_classification = self.tax_classification

        other_customer_type = self.other_customer_type

        tin = self.tin

        tin_type: Union[Unset, str] = UNSET
        if not isinstance(self.tin_type, Unset):
            tin_type = self.tin_type.value

        cert1 = self.cert1

        cert2 = self.cert2

        cert3 = self.cert3

        cert4 = self.cert4

        signature_type: Union[Unset, str] = UNSET
        if not isinstance(self.signature_type, Unset):
            signature_type = self.signature_type.value

        blank_form = self.blank_form

        tax_form_file = self.tax_form_file

        proprietary_form_number = self.proprietary_form_number

        field_dict: Dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if local_tax_forms is not UNSET:
            field_dict["localTaxForms"] = local_tax_forms
        if name is not UNSET:
            field_dict["name"] = name
        if business_name is not UNSET:
            field_dict["businessName"] = business_name
        if customer_type is not UNSET:
            field_dict["customerType"] = customer_type
        if tax_classification is not UNSET:
            field_dict["taxClassification"] = tax_classification
        if other_customer_type is not UNSET:
            field_dict["otherCustomerType"] = other_customer_type
        if tin is not UNSET:
            field_dict["tin"] = tin
        if tin_type is not UNSET:
            field_dict["tinType"] = tin_type
        if cert1 is not UNSET:
            field_dict["cert1"] = cert1
        if cert2 is not UNSET:
            field_dict["cert2"] = cert2
        if cert3 is not UNSET:
            field_dict["cert3"] = cert3
        if cert4 is not UNSET:
            field_dict["cert4"] = cert4
        if signature_type is not UNSET:
            field_dict["signatureType"] = signature_type
        if blank_form is not UNSET:
            field_dict["blankForm"] = blank_form
        if tax_form_file is not UNSET:
            field_dict["taxFormFile"] = tax_form_file
        if proprietary_form_number is not UNSET:
            field_dict["proprietaryFormNumber"] = proprietary_form_number

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

        business_name = d.pop("businessName", UNSET)

        _customer_type = d.pop("customerType", UNSET)
        customer_type: Union[Unset, FormW9CustomerType]
        if isinstance(_customer_type, Unset):
            customer_type = UNSET
        else:
            customer_type = FormW9CustomerType(_customer_type)

        tax_classification = d.pop("taxClassification", UNSET)

        other_customer_type = d.pop("otherCustomerType", UNSET)

        tin = d.pop("tin", UNSET)

        _tin_type = d.pop("tinType", UNSET)
        tin_type: Union[Unset, FormW9TinType]
        if isinstance(_tin_type, Unset):
            tin_type = UNSET
        else:
            tin_type = FormW9TinType(_tin_type)

        cert1 = d.pop("cert1", UNSET)

        cert2 = d.pop("cert2", UNSET)

        cert3 = d.pop("cert3", UNSET)

        cert4 = d.pop("cert4", UNSET)

        _signature_type = d.pop("signatureType", UNSET)
        signature_type: Union[Unset, FormW9SignatureType]
        if isinstance(_signature_type, Unset):
            signature_type = UNSET
        else:
            signature_type = FormW9SignatureType(_signature_type)

        blank_form = d.pop("blankForm", UNSET)

        tax_form_file = d.pop("taxFormFile", UNSET)

        proprietary_form_number = d.pop("proprietaryFormNumber", UNSET)

        form_w9 = cls(
            local_tax_forms=local_tax_forms,
            name=name,
            business_name=business_name,
            customer_type=customer_type,
            tax_classification=tax_classification,
            other_customer_type=other_customer_type,
            tin=tin,
            tin_type=tin_type,
            cert1=cert1,
            cert2=cert2,
            cert3=cert3,
            cert4=cert4,
            signature_type=signature_type,
            blank_form=blank_form,
            tax_form_file=tax_form_file,
            proprietary_form_number=proprietary_form_number,
        )

        form_w9.additional_properties = d
        return form_w9

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
