from typing import Any, Dict, List, Type, TypeVar, Union, cast

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..models.form_w8bene_box_11_status import FormW8BENEBox11Status
from ..models.form_w8bene_entity_type import FormW8BENEEntityType
from ..models.form_w8bene_explanation import FormW8BENEExplanation
from ..models.form_w8bene_fatca_status import FormW8BENEFatcaStatus
from ..models.form_w8bene_part_314b import FormW8BENEPart314B
from ..models.form_w8bene_part_1226_desc_3 import FormW8BENEPart1226Desc3
from ..models.form_w8bene_signature_type import FormW8BENESignatureType
from ..types import UNSET, Unset

T = TypeVar("T", bound="FormW8BENE")


@_attrs_define
class FormW8BENE:
    """
    Attributes:
        substantial_us_owner_external_ids (Union[Unset, List[str]]):
        name (Union[Unset, str]):
        country_of_organization (Union[Unset, str]):
        disregarded_entity_name (Union[Unset, str]):
        entity_type (Union[Unset, FormW8BENEEntityType]):
        fatca_status (Union[Unset, FormW8BENEFatcaStatus]):
        us_tin (Union[Unset, str]):
        giin (Union[Unset, str]):
        foreign_tin (Union[Unset, str]):
        tin_or_explanation_required (Union[Unset, bool]):
        explanation (Union[Unset, FormW8BENEExplanation]):
        reference_number (Union[Unset, int]):
        submit_date (Union[Unset, str]):
        box_11_status (Union[Unset, FormW8BENEBox11Status]):
        part_314a (Union[Unset, bool]):
        part_314a_country (Union[Unset, str]):
        part_314b (Union[Unset, FormW8BENEPart314B]):
        part_314c (Union[Unset, bool]):
        part416 (Union[Unset, str]):
        part_417i (Union[Unset, bool]):
        part_417_ii (Union[Unset, bool]):
        part518 (Union[Unset, bool]):
        part619 (Union[Unset, bool]):
        part720 (Union[Unset, str]):
        part721 (Union[Unset, bool]):
        part822 (Union[Unset, bool]):
        part923 (Union[Unset, bool]):
        part_1024a (Union[Unset, bool]):
        part_1024b (Union[Unset, bool]):
        part_1024c (Union[Unset, bool]):
        part_1024d (Union[Unset, bool]):
        part_1125a (Union[Unset, bool]):
        part_1125b (Union[Unset, bool]):
        part_1125c (Union[Unset, bool]):
        part1226 (Union[Unset, bool]):
        part_1226_desc_1 (Union[Unset, str]):
        part_1226_desc_2 (Union[Unset, str]):
        part_1226_desc_3 (Union[Unset, FormW8BENEPart1226Desc3]):
        part_1226_desc_4 (Union[Unset, str]):
        part1327 (Union[Unset, bool]):
        part_1428a (Union[Unset, bool]):
        part_1428b (Union[Unset, bool]):
        part_1529a (Union[Unset, bool]):
        part_1529b (Union[Unset, bool]):
        part_1529c (Union[Unset, bool]):
        part_1529d (Union[Unset, bool]):
        part_1529e (Union[Unset, bool]):
        part_1529f (Union[Unset, bool]):
        part1630 (Union[Unset, bool]):
        part1731 (Union[Unset, bool]):
        part1832 (Union[Unset, bool]):
        part1933 (Union[Unset, bool]):
        part2034 (Union[Unset, bool]):
        part2135 (Union[Unset, bool]):
        part_2135_date (Union[Unset, str]):
        part2236 (Union[Unset, bool]):
        part_2337a (Union[Unset, bool]):
        part_2337a_desc (Union[Unset, str]):
        part_2337b (Union[Unset, bool]):
        part_2337b_desc_1 (Union[Unset, str]):
        part_2337b_desc_2 (Union[Unset, str]):
        part2438 (Union[Unset, bool]):
        part2539 (Union[Unset, bool]):
        part_2640a (Union[Unset, bool]):
        part_2640b (Union[Unset, bool]):
        part_2640c (Union[Unset, bool]):
        part2741 (Union[Unset, bool]):
        part2842 (Union[Unset, str]):
        part2843 (Union[Unset, bool]):
        cert (Union[Unset, bool]):
        signature_type (Union[Unset, FormW8BENESignatureType]):
        blank_form (Union[Unset, bool]):
        tax_form_file (Union[Unset, str]):
        proprietary_form_number (Union[Unset, int]):
        electronic_format (Union[Unset, bool]):
    """

    substantial_us_owner_external_ids: Union[Unset, List[str]] = UNSET
    name: Union[Unset, str] = UNSET
    country_of_organization: Union[Unset, str] = UNSET
    disregarded_entity_name: Union[Unset, str] = UNSET
    entity_type: Union[Unset, FormW8BENEEntityType] = UNSET
    fatca_status: Union[Unset, FormW8BENEFatcaStatus] = UNSET
    us_tin: Union[Unset, str] = UNSET
    giin: Union[Unset, str] = UNSET
    foreign_tin: Union[Unset, str] = UNSET
    tin_or_explanation_required: Union[Unset, bool] = UNSET
    explanation: Union[Unset, FormW8BENEExplanation] = UNSET
    reference_number: Union[Unset, int] = UNSET
    submit_date: Union[Unset, str] = UNSET
    box_11_status: Union[Unset, FormW8BENEBox11Status] = UNSET
    part_314a: Union[Unset, bool] = UNSET
    part_314a_country: Union[Unset, str] = UNSET
    part_314b: Union[Unset, FormW8BENEPart314B] = UNSET
    part_314c: Union[Unset, bool] = UNSET
    part416: Union[Unset, str] = UNSET
    part_417i: Union[Unset, bool] = UNSET
    part_417_ii: Union[Unset, bool] = UNSET
    part518: Union[Unset, bool] = UNSET
    part619: Union[Unset, bool] = UNSET
    part720: Union[Unset, str] = UNSET
    part721: Union[Unset, bool] = UNSET
    part822: Union[Unset, bool] = UNSET
    part923: Union[Unset, bool] = UNSET
    part_1024a: Union[Unset, bool] = UNSET
    part_1024b: Union[Unset, bool] = UNSET
    part_1024c: Union[Unset, bool] = UNSET
    part_1024d: Union[Unset, bool] = UNSET
    part_1125a: Union[Unset, bool] = UNSET
    part_1125b: Union[Unset, bool] = UNSET
    part_1125c: Union[Unset, bool] = UNSET
    part1226: Union[Unset, bool] = UNSET
    part_1226_desc_1: Union[Unset, str] = UNSET
    part_1226_desc_2: Union[Unset, str] = UNSET
    part_1226_desc_3: Union[Unset, FormW8BENEPart1226Desc3] = UNSET
    part_1226_desc_4: Union[Unset, str] = UNSET
    part1327: Union[Unset, bool] = UNSET
    part_1428a: Union[Unset, bool] = UNSET
    part_1428b: Union[Unset, bool] = UNSET
    part_1529a: Union[Unset, bool] = UNSET
    part_1529b: Union[Unset, bool] = UNSET
    part_1529c: Union[Unset, bool] = UNSET
    part_1529d: Union[Unset, bool] = UNSET
    part_1529e: Union[Unset, bool] = UNSET
    part_1529f: Union[Unset, bool] = UNSET
    part1630: Union[Unset, bool] = UNSET
    part1731: Union[Unset, bool] = UNSET
    part1832: Union[Unset, bool] = UNSET
    part1933: Union[Unset, bool] = UNSET
    part2034: Union[Unset, bool] = UNSET
    part2135: Union[Unset, bool] = UNSET
    part_2135_date: Union[Unset, str] = UNSET
    part2236: Union[Unset, bool] = UNSET
    part_2337a: Union[Unset, bool] = UNSET
    part_2337a_desc: Union[Unset, str] = UNSET
    part_2337b: Union[Unset, bool] = UNSET
    part_2337b_desc_1: Union[Unset, str] = UNSET
    part_2337b_desc_2: Union[Unset, str] = UNSET
    part2438: Union[Unset, bool] = UNSET
    part2539: Union[Unset, bool] = UNSET
    part_2640a: Union[Unset, bool] = UNSET
    part_2640b: Union[Unset, bool] = UNSET
    part_2640c: Union[Unset, bool] = UNSET
    part2741: Union[Unset, bool] = UNSET
    part2842: Union[Unset, str] = UNSET
    part2843: Union[Unset, bool] = UNSET
    cert: Union[Unset, bool] = UNSET
    signature_type: Union[Unset, FormW8BENESignatureType] = UNSET
    blank_form: Union[Unset, bool] = UNSET
    tax_form_file: Union[Unset, str] = UNSET
    proprietary_form_number: Union[Unset, int] = UNSET
    electronic_format: Union[Unset, bool] = UNSET
    additional_properties: Dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> Dict[str, Any]:
        substantial_us_owner_external_ids: Union[Unset, List[str]] = UNSET
        if not isinstance(self.substantial_us_owner_external_ids, Unset):
            substantial_us_owner_external_ids = self.substantial_us_owner_external_ids

        name = self.name

        country_of_organization = self.country_of_organization

        disregarded_entity_name = self.disregarded_entity_name

        entity_type: Union[Unset, str] = UNSET
        if not isinstance(self.entity_type, Unset):
            entity_type = self.entity_type.value

        fatca_status: Union[Unset, str] = UNSET
        if not isinstance(self.fatca_status, Unset):
            fatca_status = self.fatca_status.value

        us_tin = self.us_tin

        giin = self.giin

        foreign_tin = self.foreign_tin

        tin_or_explanation_required = self.tin_or_explanation_required

        explanation: Union[Unset, str] = UNSET
        if not isinstance(self.explanation, Unset):
            explanation = self.explanation.value

        reference_number = self.reference_number

        submit_date = self.submit_date

        box_11_status: Union[Unset, str] = UNSET
        if not isinstance(self.box_11_status, Unset):
            box_11_status = self.box_11_status.value

        part_314a = self.part_314a

        part_314a_country = self.part_314a_country

        part_314b: Union[Unset, str] = UNSET
        if not isinstance(self.part_314b, Unset):
            part_314b = self.part_314b.value

        part_314c = self.part_314c

        part416 = self.part416

        part_417i = self.part_417i

        part_417_ii = self.part_417_ii

        part518 = self.part518

        part619 = self.part619

        part720 = self.part720

        part721 = self.part721

        part822 = self.part822

        part923 = self.part923

        part_1024a = self.part_1024a

        part_1024b = self.part_1024b

        part_1024c = self.part_1024c

        part_1024d = self.part_1024d

        part_1125a = self.part_1125a

        part_1125b = self.part_1125b

        part_1125c = self.part_1125c

        part1226 = self.part1226

        part_1226_desc_1 = self.part_1226_desc_1

        part_1226_desc_2 = self.part_1226_desc_2

        part_1226_desc_3: Union[Unset, str] = UNSET
        if not isinstance(self.part_1226_desc_3, Unset):
            part_1226_desc_3 = self.part_1226_desc_3.value

        part_1226_desc_4 = self.part_1226_desc_4

        part1327 = self.part1327

        part_1428a = self.part_1428a

        part_1428b = self.part_1428b

        part_1529a = self.part_1529a

        part_1529b = self.part_1529b

        part_1529c = self.part_1529c

        part_1529d = self.part_1529d

        part_1529e = self.part_1529e

        part_1529f = self.part_1529f

        part1630 = self.part1630

        part1731 = self.part1731

        part1832 = self.part1832

        part1933 = self.part1933

        part2034 = self.part2034

        part2135 = self.part2135

        part_2135_date = self.part_2135_date

        part2236 = self.part2236

        part_2337a = self.part_2337a

        part_2337a_desc = self.part_2337a_desc

        part_2337b = self.part_2337b

        part_2337b_desc_1 = self.part_2337b_desc_1

        part_2337b_desc_2 = self.part_2337b_desc_2

        part2438 = self.part2438

        part2539 = self.part2539

        part_2640a = self.part_2640a

        part_2640b = self.part_2640b

        part_2640c = self.part_2640c

        part2741 = self.part2741

        part2842 = self.part2842

        part2843 = self.part2843

        cert = self.cert

        signature_type: Union[Unset, str] = UNSET
        if not isinstance(self.signature_type, Unset):
            signature_type = self.signature_type.value

        blank_form = self.blank_form

        tax_form_file = self.tax_form_file

        proprietary_form_number = self.proprietary_form_number

        electronic_format = self.electronic_format

        field_dict: Dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if substantial_us_owner_external_ids is not UNSET:
            field_dict["substantialUsOwnerExternalIds"] = substantial_us_owner_external_ids
        if name is not UNSET:
            field_dict["name"] = name
        if country_of_organization is not UNSET:
            field_dict["countryOfOrganization"] = country_of_organization
        if disregarded_entity_name is not UNSET:
            field_dict["disregardedEntityName"] = disregarded_entity_name
        if entity_type is not UNSET:
            field_dict["entityType"] = entity_type
        if fatca_status is not UNSET:
            field_dict["fatcaStatus"] = fatca_status
        if us_tin is not UNSET:
            field_dict["usTin"] = us_tin
        if giin is not UNSET:
            field_dict["giin"] = giin
        if foreign_tin is not UNSET:
            field_dict["foreignTin"] = foreign_tin
        if tin_or_explanation_required is not UNSET:
            field_dict["tinOrExplanationRequired"] = tin_or_explanation_required
        if explanation is not UNSET:
            field_dict["explanation"] = explanation
        if reference_number is not UNSET:
            field_dict["referenceNumber"] = reference_number
        if submit_date is not UNSET:
            field_dict["submitDate"] = submit_date
        if box_11_status is not UNSET:
            field_dict["box11Status"] = box_11_status
        if part_314a is not UNSET:
            field_dict["part314A"] = part_314a
        if part_314a_country is not UNSET:
            field_dict["part314ACountry"] = part_314a_country
        if part_314b is not UNSET:
            field_dict["part314B"] = part_314b
        if part_314c is not UNSET:
            field_dict["part314C"] = part_314c
        if part416 is not UNSET:
            field_dict["part416"] = part416
        if part_417i is not UNSET:
            field_dict["part417I"] = part_417i
        if part_417_ii is not UNSET:
            field_dict["part417Ii"] = part_417_ii
        if part518 is not UNSET:
            field_dict["part518"] = part518
        if part619 is not UNSET:
            field_dict["part619"] = part619
        if part720 is not UNSET:
            field_dict["part720"] = part720
        if part721 is not UNSET:
            field_dict["part721"] = part721
        if part822 is not UNSET:
            field_dict["part822"] = part822
        if part923 is not UNSET:
            field_dict["part923"] = part923
        if part_1024a is not UNSET:
            field_dict["part1024A"] = part_1024a
        if part_1024b is not UNSET:
            field_dict["part1024B"] = part_1024b
        if part_1024c is not UNSET:
            field_dict["part1024C"] = part_1024c
        if part_1024d is not UNSET:
            field_dict["part1024D"] = part_1024d
        if part_1125a is not UNSET:
            field_dict["part1125A"] = part_1125a
        if part_1125b is not UNSET:
            field_dict["part1125B"] = part_1125b
        if part_1125c is not UNSET:
            field_dict["part1125C"] = part_1125c
        if part1226 is not UNSET:
            field_dict["part1226"] = part1226
        if part_1226_desc_1 is not UNSET:
            field_dict["part1226Desc1"] = part_1226_desc_1
        if part_1226_desc_2 is not UNSET:
            field_dict["part1226Desc2"] = part_1226_desc_2
        if part_1226_desc_3 is not UNSET:
            field_dict["part1226Desc3"] = part_1226_desc_3
        if part_1226_desc_4 is not UNSET:
            field_dict["part1226Desc4"] = part_1226_desc_4
        if part1327 is not UNSET:
            field_dict["part1327"] = part1327
        if part_1428a is not UNSET:
            field_dict["part1428A"] = part_1428a
        if part_1428b is not UNSET:
            field_dict["part1428B"] = part_1428b
        if part_1529a is not UNSET:
            field_dict["part1529A"] = part_1529a
        if part_1529b is not UNSET:
            field_dict["part1529B"] = part_1529b
        if part_1529c is not UNSET:
            field_dict["part1529C"] = part_1529c
        if part_1529d is not UNSET:
            field_dict["part1529D"] = part_1529d
        if part_1529e is not UNSET:
            field_dict["part1529E"] = part_1529e
        if part_1529f is not UNSET:
            field_dict["part1529F"] = part_1529f
        if part1630 is not UNSET:
            field_dict["part1630"] = part1630
        if part1731 is not UNSET:
            field_dict["part1731"] = part1731
        if part1832 is not UNSET:
            field_dict["part1832"] = part1832
        if part1933 is not UNSET:
            field_dict["part1933"] = part1933
        if part2034 is not UNSET:
            field_dict["part2034"] = part2034
        if part2135 is not UNSET:
            field_dict["part2135"] = part2135
        if part_2135_date is not UNSET:
            field_dict["part2135Date"] = part_2135_date
        if part2236 is not UNSET:
            field_dict["part2236"] = part2236
        if part_2337a is not UNSET:
            field_dict["part2337A"] = part_2337a
        if part_2337a_desc is not UNSET:
            field_dict["part2337ADesc"] = part_2337a_desc
        if part_2337b is not UNSET:
            field_dict["part2337B"] = part_2337b
        if part_2337b_desc_1 is not UNSET:
            field_dict["part2337BDesc1"] = part_2337b_desc_1
        if part_2337b_desc_2 is not UNSET:
            field_dict["part2337BDesc2"] = part_2337b_desc_2
        if part2438 is not UNSET:
            field_dict["part2438"] = part2438
        if part2539 is not UNSET:
            field_dict["part2539"] = part2539
        if part_2640a is not UNSET:
            field_dict["part2640A"] = part_2640a
        if part_2640b is not UNSET:
            field_dict["part2640B"] = part_2640b
        if part_2640c is not UNSET:
            field_dict["part2640C"] = part_2640c
        if part2741 is not UNSET:
            field_dict["part2741"] = part2741
        if part2842 is not UNSET:
            field_dict["part2842"] = part2842
        if part2843 is not UNSET:
            field_dict["part2843"] = part2843
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

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        d = src_dict.copy()
        substantial_us_owner_external_ids = cast(List[str], d.pop("substantialUsOwnerExternalIds", UNSET))

        name = d.pop("name", UNSET)

        country_of_organization = d.pop("countryOfOrganization", UNSET)

        disregarded_entity_name = d.pop("disregardedEntityName", UNSET)

        _entity_type = d.pop("entityType", UNSET)
        entity_type: Union[Unset, FormW8BENEEntityType]
        if isinstance(_entity_type, Unset):
            entity_type = UNSET
        else:
            entity_type = FormW8BENEEntityType(_entity_type)

        _fatca_status = d.pop("fatcaStatus", UNSET)
        fatca_status: Union[Unset, FormW8BENEFatcaStatus]
        if isinstance(_fatca_status, Unset):
            fatca_status = UNSET
        else:
            fatca_status = FormW8BENEFatcaStatus(_fatca_status)

        us_tin = d.pop("usTin", UNSET)

        giin = d.pop("giin", UNSET)

        foreign_tin = d.pop("foreignTin", UNSET)

        tin_or_explanation_required = d.pop("tinOrExplanationRequired", UNSET)

        _explanation = d.pop("explanation", UNSET)
        explanation: Union[Unset, FormW8BENEExplanation]
        if isinstance(_explanation, Unset):
            explanation = UNSET
        else:
            explanation = FormW8BENEExplanation(_explanation)

        reference_number = d.pop("referenceNumber", UNSET)

        submit_date = d.pop("submitDate", UNSET)

        _box_11_status = d.pop("box11Status", UNSET)
        box_11_status: Union[Unset, FormW8BENEBox11Status]
        if isinstance(_box_11_status, Unset):
            box_11_status = UNSET
        else:
            box_11_status = FormW8BENEBox11Status(_box_11_status)

        part_314a = d.pop("part314A", UNSET)

        part_314a_country = d.pop("part314ACountry", UNSET)

        _part_314b = d.pop("part314B", UNSET)
        part_314b: Union[Unset, FormW8BENEPart314B]
        if isinstance(_part_314b, Unset):
            part_314b = UNSET
        else:
            part_314b = FormW8BENEPart314B(_part_314b)

        part_314c = d.pop("part314C", UNSET)

        part416 = d.pop("part416", UNSET)

        part_417i = d.pop("part417I", UNSET)

        part_417_ii = d.pop("part417Ii", UNSET)

        part518 = d.pop("part518", UNSET)

        part619 = d.pop("part619", UNSET)

        part720 = d.pop("part720", UNSET)

        part721 = d.pop("part721", UNSET)

        part822 = d.pop("part822", UNSET)

        part923 = d.pop("part923", UNSET)

        part_1024a = d.pop("part1024A", UNSET)

        part_1024b = d.pop("part1024B", UNSET)

        part_1024c = d.pop("part1024C", UNSET)

        part_1024d = d.pop("part1024D", UNSET)

        part_1125a = d.pop("part1125A", UNSET)

        part_1125b = d.pop("part1125B", UNSET)

        part_1125c = d.pop("part1125C", UNSET)

        part1226 = d.pop("part1226", UNSET)

        part_1226_desc_1 = d.pop("part1226Desc1", UNSET)

        part_1226_desc_2 = d.pop("part1226Desc2", UNSET)

        _part_1226_desc_3 = d.pop("part1226Desc3", UNSET)
        part_1226_desc_3: Union[Unset, FormW8BENEPart1226Desc3]
        if isinstance(_part_1226_desc_3, Unset):
            part_1226_desc_3 = UNSET
        else:
            part_1226_desc_3 = FormW8BENEPart1226Desc3(_part_1226_desc_3)

        part_1226_desc_4 = d.pop("part1226Desc4", UNSET)

        part1327 = d.pop("part1327", UNSET)

        part_1428a = d.pop("part1428A", UNSET)

        part_1428b = d.pop("part1428B", UNSET)

        part_1529a = d.pop("part1529A", UNSET)

        part_1529b = d.pop("part1529B", UNSET)

        part_1529c = d.pop("part1529C", UNSET)

        part_1529d = d.pop("part1529D", UNSET)

        part_1529e = d.pop("part1529E", UNSET)

        part_1529f = d.pop("part1529F", UNSET)

        part1630 = d.pop("part1630", UNSET)

        part1731 = d.pop("part1731", UNSET)

        part1832 = d.pop("part1832", UNSET)

        part1933 = d.pop("part1933", UNSET)

        part2034 = d.pop("part2034", UNSET)

        part2135 = d.pop("part2135", UNSET)

        part_2135_date = d.pop("part2135Date", UNSET)

        part2236 = d.pop("part2236", UNSET)

        part_2337a = d.pop("part2337A", UNSET)

        part_2337a_desc = d.pop("part2337ADesc", UNSET)

        part_2337b = d.pop("part2337B", UNSET)

        part_2337b_desc_1 = d.pop("part2337BDesc1", UNSET)

        part_2337b_desc_2 = d.pop("part2337BDesc2", UNSET)

        part2438 = d.pop("part2438", UNSET)

        part2539 = d.pop("part2539", UNSET)

        part_2640a = d.pop("part2640A", UNSET)

        part_2640b = d.pop("part2640B", UNSET)

        part_2640c = d.pop("part2640C", UNSET)

        part2741 = d.pop("part2741", UNSET)

        part2842 = d.pop("part2842", UNSET)

        part2843 = d.pop("part2843", UNSET)

        cert = d.pop("cert", UNSET)

        _signature_type = d.pop("signatureType", UNSET)
        signature_type: Union[Unset, FormW8BENESignatureType]
        if isinstance(_signature_type, Unset):
            signature_type = UNSET
        else:
            signature_type = FormW8BENESignatureType(_signature_type)

        blank_form = d.pop("blankForm", UNSET)

        tax_form_file = d.pop("taxFormFile", UNSET)

        proprietary_form_number = d.pop("proprietaryFormNumber", UNSET)

        electronic_format = d.pop("electronicFormat", UNSET)

        form_w8bene = cls(
            substantial_us_owner_external_ids=substantial_us_owner_external_ids,
            name=name,
            country_of_organization=country_of_organization,
            disregarded_entity_name=disregarded_entity_name,
            entity_type=entity_type,
            fatca_status=fatca_status,
            us_tin=us_tin,
            giin=giin,
            foreign_tin=foreign_tin,
            tin_or_explanation_required=tin_or_explanation_required,
            explanation=explanation,
            reference_number=reference_number,
            submit_date=submit_date,
            box_11_status=box_11_status,
            part_314a=part_314a,
            part_314a_country=part_314a_country,
            part_314b=part_314b,
            part_314c=part_314c,
            part416=part416,
            part_417i=part_417i,
            part_417_ii=part_417_ii,
            part518=part518,
            part619=part619,
            part720=part720,
            part721=part721,
            part822=part822,
            part923=part923,
            part_1024a=part_1024a,
            part_1024b=part_1024b,
            part_1024c=part_1024c,
            part_1024d=part_1024d,
            part_1125a=part_1125a,
            part_1125b=part_1125b,
            part_1125c=part_1125c,
            part1226=part1226,
            part_1226_desc_1=part_1226_desc_1,
            part_1226_desc_2=part_1226_desc_2,
            part_1226_desc_3=part_1226_desc_3,
            part_1226_desc_4=part_1226_desc_4,
            part1327=part1327,
            part_1428a=part_1428a,
            part_1428b=part_1428b,
            part_1529a=part_1529a,
            part_1529b=part_1529b,
            part_1529c=part_1529c,
            part_1529d=part_1529d,
            part_1529e=part_1529e,
            part_1529f=part_1529f,
            part1630=part1630,
            part1731=part1731,
            part1832=part1832,
            part1933=part1933,
            part2034=part2034,
            part2135=part2135,
            part_2135_date=part_2135_date,
            part2236=part2236,
            part_2337a=part_2337a,
            part_2337a_desc=part_2337a_desc,
            part_2337b=part_2337b,
            part_2337b_desc_1=part_2337b_desc_1,
            part_2337b_desc_2=part_2337b_desc_2,
            part2438=part2438,
            part2539=part2539,
            part_2640a=part_2640a,
            part_2640b=part_2640b,
            part_2640c=part_2640c,
            part2741=part2741,
            part2842=part2842,
            part2843=part2843,
            cert=cert,
            signature_type=signature_type,
            blank_form=blank_form,
            tax_form_file=tax_form_file,
            proprietary_form_number=proprietary_form_number,
            electronic_format=electronic_format,
        )

        form_w8bene.additional_properties = d
        return form_w8bene

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
