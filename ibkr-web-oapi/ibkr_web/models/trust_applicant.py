from typing import TYPE_CHECKING, Any, Dict, List, Type, TypeVar, Union

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..models.trust_applicant_trust_type import TrustApplicantTrustType
from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.accredited_investor_information import AccreditedInvestorInformation
    from ..models.association_type_entities import AssociationTypeEntities
    from ..models.financial_information import FinancialInformation
    from ..models.form_w8bene import FormW8BENE
    from ..models.form_w8imy import FormW8IMY
    from ..models.regulated_membership import RegulatedMembership
    from ..models.regulatory_information import RegulatoryInformation
    from ..models.tax_residency import TaxResidency
    from ..models.trust_identification import TrustIdentification
    from ..models.trustees_type import TrusteesType
    from ..models.withholding_statement_type import WithholdingStatementType


T = TypeVar("T", bound="TrustApplicant")


@_attrs_define
class TrustApplicant:
    """
    Attributes:
        identification (Union[Unset, List['TrustIdentification']]):
        financial_information (Union[Unset, List['FinancialInformation']]):
        regulatory_information (Union[Unset, List['RegulatoryInformation']]):
        regulated_memberships (Union[Unset, List['RegulatedMembership']]):
        accredited_investor_information (Union[Unset, AccreditedInvestorInformation]):
        trustees (Union[Unset, TrusteesType]):
        beneficiaries (Union[Unset, AssociationTypeEntities]):
        grantors (Union[Unset, AssociationTypeEntities]):
        tax_residencies (Union[Unset, List['TaxResidency']]):
        w_8_ben_e (Union[Unset, FormW8BENE]):
        w_8imy (Union[Unset, FormW8IMY]):
        withholding_statement (Union[Unset, WithholdingStatementType]):
        third_party_management (Union[Unset, bool]):
        trust_type (Union[Unset, TrustApplicantTrustType]):
    """

    identification: Union[Unset, List["TrustIdentification"]] = UNSET
    financial_information: Union[Unset, List["FinancialInformation"]] = UNSET
    regulatory_information: Union[Unset, List["RegulatoryInformation"]] = UNSET
    regulated_memberships: Union[Unset, List["RegulatedMembership"]] = UNSET
    accredited_investor_information: Union[Unset, "AccreditedInvestorInformation"] = UNSET
    trustees: Union[Unset, "TrusteesType"] = UNSET
    beneficiaries: Union[Unset, "AssociationTypeEntities"] = UNSET
    grantors: Union[Unset, "AssociationTypeEntities"] = UNSET
    tax_residencies: Union[Unset, List["TaxResidency"]] = UNSET
    w_8_ben_e: Union[Unset, "FormW8BENE"] = UNSET
    w_8imy: Union[Unset, "FormW8IMY"] = UNSET
    withholding_statement: Union[Unset, "WithholdingStatementType"] = UNSET
    third_party_management: Union[Unset, bool] = UNSET
    trust_type: Union[Unset, TrustApplicantTrustType] = UNSET
    additional_properties: Dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> Dict[str, Any]:
        identification: Union[Unset, List[Dict[str, Any]]] = UNSET
        if not isinstance(self.identification, Unset):
            identification = []
            for identification_item_data in self.identification:
                identification_item = identification_item_data.to_dict()
                identification.append(identification_item)

        financial_information: Union[Unset, List[Dict[str, Any]]] = UNSET
        if not isinstance(self.financial_information, Unset):
            financial_information = []
            for financial_information_item_data in self.financial_information:
                financial_information_item = financial_information_item_data.to_dict()
                financial_information.append(financial_information_item)

        regulatory_information: Union[Unset, List[Dict[str, Any]]] = UNSET
        if not isinstance(self.regulatory_information, Unset):
            regulatory_information = []
            for regulatory_information_item_data in self.regulatory_information:
                regulatory_information_item = regulatory_information_item_data.to_dict()
                regulatory_information.append(regulatory_information_item)

        regulated_memberships: Union[Unset, List[Dict[str, Any]]] = UNSET
        if not isinstance(self.regulated_memberships, Unset):
            regulated_memberships = []
            for regulated_memberships_item_data in self.regulated_memberships:
                regulated_memberships_item = regulated_memberships_item_data.to_dict()
                regulated_memberships.append(regulated_memberships_item)

        accredited_investor_information: Union[Unset, Dict[str, Any]] = UNSET
        if not isinstance(self.accredited_investor_information, Unset):
            accredited_investor_information = self.accredited_investor_information.to_dict()

        trustees: Union[Unset, Dict[str, Any]] = UNSET
        if not isinstance(self.trustees, Unset):
            trustees = self.trustees.to_dict()

        beneficiaries: Union[Unset, Dict[str, Any]] = UNSET
        if not isinstance(self.beneficiaries, Unset):
            beneficiaries = self.beneficiaries.to_dict()

        grantors: Union[Unset, Dict[str, Any]] = UNSET
        if not isinstance(self.grantors, Unset):
            grantors = self.grantors.to_dict()

        tax_residencies: Union[Unset, List[Dict[str, Any]]] = UNSET
        if not isinstance(self.tax_residencies, Unset):
            tax_residencies = []
            for tax_residencies_item_data in self.tax_residencies:
                tax_residencies_item = tax_residencies_item_data.to_dict()
                tax_residencies.append(tax_residencies_item)

        w_8_ben_e: Union[Unset, Dict[str, Any]] = UNSET
        if not isinstance(self.w_8_ben_e, Unset):
            w_8_ben_e = self.w_8_ben_e.to_dict()

        w_8imy: Union[Unset, Dict[str, Any]] = UNSET
        if not isinstance(self.w_8imy, Unset):
            w_8imy = self.w_8imy.to_dict()

        withholding_statement: Union[Unset, Dict[str, Any]] = UNSET
        if not isinstance(self.withholding_statement, Unset):
            withholding_statement = self.withholding_statement.to_dict()

        third_party_management = self.third_party_management

        trust_type: Union[Unset, str] = UNSET
        if not isinstance(self.trust_type, Unset):
            trust_type = self.trust_type.value

        field_dict: Dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if identification is not UNSET:
            field_dict["identification"] = identification
        if financial_information is not UNSET:
            field_dict["financialInformation"] = financial_information
        if regulatory_information is not UNSET:
            field_dict["regulatoryInformation"] = regulatory_information
        if regulated_memberships is not UNSET:
            field_dict["regulatedMemberships"] = regulated_memberships
        if accredited_investor_information is not UNSET:
            field_dict["accreditedInvestorInformation"] = accredited_investor_information
        if trustees is not UNSET:
            field_dict["trustees"] = trustees
        if beneficiaries is not UNSET:
            field_dict["beneficiaries"] = beneficiaries
        if grantors is not UNSET:
            field_dict["grantors"] = grantors
        if tax_residencies is not UNSET:
            field_dict["taxResidencies"] = tax_residencies
        if w_8_ben_e is not UNSET:
            field_dict["w8BenE"] = w_8_ben_e
        if w_8imy is not UNSET:
            field_dict["w8IMY"] = w_8imy
        if withholding_statement is not UNSET:
            field_dict["withholdingStatement"] = withholding_statement
        if third_party_management is not UNSET:
            field_dict["thirdPartyManagement"] = third_party_management
        if trust_type is not UNSET:
            field_dict["trustType"] = trust_type

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        from ..models.accredited_investor_information import AccreditedInvestorInformation
        from ..models.association_type_entities import AssociationTypeEntities
        from ..models.financial_information import FinancialInformation
        from ..models.form_w8bene import FormW8BENE
        from ..models.form_w8imy import FormW8IMY
        from ..models.regulated_membership import RegulatedMembership
        from ..models.regulatory_information import RegulatoryInformation
        from ..models.tax_residency import TaxResidency
        from ..models.trust_identification import TrustIdentification
        from ..models.trustees_type import TrusteesType
        from ..models.withholding_statement_type import WithholdingStatementType

        d = src_dict.copy()
        identification = []
        _identification = d.pop("identification", UNSET)
        for identification_item_data in _identification or []:
            identification_item = TrustIdentification.from_dict(identification_item_data)

            identification.append(identification_item)

        financial_information = []
        _financial_information = d.pop("financialInformation", UNSET)
        for financial_information_item_data in _financial_information or []:
            financial_information_item = FinancialInformation.from_dict(financial_information_item_data)

            financial_information.append(financial_information_item)

        regulatory_information = []
        _regulatory_information = d.pop("regulatoryInformation", UNSET)
        for regulatory_information_item_data in _regulatory_information or []:
            regulatory_information_item = RegulatoryInformation.from_dict(regulatory_information_item_data)

            regulatory_information.append(regulatory_information_item)

        regulated_memberships = []
        _regulated_memberships = d.pop("regulatedMemberships", UNSET)
        for regulated_memberships_item_data in _regulated_memberships or []:
            regulated_memberships_item = RegulatedMembership.from_dict(regulated_memberships_item_data)

            regulated_memberships.append(regulated_memberships_item)

        _accredited_investor_information = d.pop("accreditedInvestorInformation", UNSET)
        accredited_investor_information: Union[Unset, AccreditedInvestorInformation]
        if isinstance(_accredited_investor_information, Unset):
            accredited_investor_information = UNSET
        else:
            accredited_investor_information = AccreditedInvestorInformation.from_dict(_accredited_investor_information)

        _trustees = d.pop("trustees", UNSET)
        trustees: Union[Unset, TrusteesType]
        if isinstance(_trustees, Unset):
            trustees = UNSET
        else:
            trustees = TrusteesType.from_dict(_trustees)

        _beneficiaries = d.pop("beneficiaries", UNSET)
        beneficiaries: Union[Unset, AssociationTypeEntities]
        if isinstance(_beneficiaries, Unset):
            beneficiaries = UNSET
        else:
            beneficiaries = AssociationTypeEntities.from_dict(_beneficiaries)

        _grantors = d.pop("grantors", UNSET)
        grantors: Union[Unset, AssociationTypeEntities]
        if isinstance(_grantors, Unset):
            grantors = UNSET
        else:
            grantors = AssociationTypeEntities.from_dict(_grantors)

        tax_residencies = []
        _tax_residencies = d.pop("taxResidencies", UNSET)
        for tax_residencies_item_data in _tax_residencies or []:
            tax_residencies_item = TaxResidency.from_dict(tax_residencies_item_data)

            tax_residencies.append(tax_residencies_item)

        _w_8_ben_e = d.pop("w8BenE", UNSET)
        w_8_ben_e: Union[Unset, FormW8BENE]
        if isinstance(_w_8_ben_e, Unset):
            w_8_ben_e = UNSET
        else:
            w_8_ben_e = FormW8BENE.from_dict(_w_8_ben_e)

        _w_8imy = d.pop("w8IMY", UNSET)
        w_8imy: Union[Unset, FormW8IMY]
        if isinstance(_w_8imy, Unset):
            w_8imy = UNSET
        else:
            w_8imy = FormW8IMY.from_dict(_w_8imy)

        _withholding_statement = d.pop("withholdingStatement", UNSET)
        withholding_statement: Union[Unset, WithholdingStatementType]
        if isinstance(_withholding_statement, Unset):
            withholding_statement = UNSET
        else:
            withholding_statement = WithholdingStatementType.from_dict(_withholding_statement)

        third_party_management = d.pop("thirdPartyManagement", UNSET)

        _trust_type = d.pop("trustType", UNSET)
        trust_type: Union[Unset, TrustApplicantTrustType]
        if isinstance(_trust_type, Unset):
            trust_type = UNSET
        else:
            trust_type = TrustApplicantTrustType(_trust_type)

        trust_applicant = cls(
            identification=identification,
            financial_information=financial_information,
            regulatory_information=regulatory_information,
            regulated_memberships=regulated_memberships,
            accredited_investor_information=accredited_investor_information,
            trustees=trustees,
            beneficiaries=beneficiaries,
            grantors=grantors,
            tax_residencies=tax_residencies,
            w_8_ben_e=w_8_ben_e,
            w_8imy=w_8imy,
            withholding_statement=withholding_statement,
            third_party_management=third_party_management,
            trust_type=trust_type,
        )

        trust_applicant.additional_properties = d
        return trust_applicant

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
