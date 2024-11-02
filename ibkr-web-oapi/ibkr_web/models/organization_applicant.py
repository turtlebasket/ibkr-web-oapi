from typing import TYPE_CHECKING, Any, Dict, List, Type, TypeVar, Union

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..models.organization_applicant_type import OrganizationApplicantType
from ..models.organization_applicant_type_of_trading import OrganizationApplicantTypeOfTrading
from ..models.organization_applicant_us_tax_purpose_type import OrganizationApplicantUsTaxPurposeType
from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.account_support_type import AccountSupportType
    from ..models.accredited_investor_information import AccreditedInvestorInformation
    from ..models.associated_entities import AssociatedEntities
    from ..models.financial_information import FinancialInformation
    from ..models.form_w8bene import FormW8BENE
    from ..models.form_w8imy import FormW8IMY
    from ..models.managing_owner import ManagingOwner
    from ..models.organization_identification import OrganizationIdentification
    from ..models.regulated_membership import RegulatedMembership
    from ..models.regulatory_information import RegulatoryInformation
    from ..models.tax_residency import TaxResidency
    from ..models.withholding_statement_type import WithholdingStatementType


T = TypeVar("T", bound="OrganizationApplicant")


@_attrs_define
class OrganizationApplicant:
    """
    Attributes:
        identifications (Union[Unset, List['OrganizationIdentification']]):
        account_support (Union[Unset, AccountSupportType]):
        financial_information (Union[Unset, List['FinancialInformation']]):
        accredited_investor_information (Union[Unset, AccreditedInvestorInformation]):
        regulatory_information (Union[Unset, List['RegulatoryInformation']]):
        managing_owner (Union[Unset, ManagingOwner]):
        associated_entities (Union[Unset, AssociatedEntities]):
        regulated_memberships (Union[Unset, List['RegulatedMembership']]):
        tax_residencies (Union[Unset, List['TaxResidency']]):
        w_8_ben_e (Union[Unset, FormW8BENE]):
        w_8imy (Union[Unset, FormW8IMY]):
        withholding_statement (Union[Unset, WithholdingStatementType]):
        type_of_trading (Union[Unset, OrganizationApplicantTypeOfTrading]):
        type (Union[Unset, OrganizationApplicantType]):
        org_us_subsidiary (Union[Unset, bool]):
        qualified_intermediary (Union[Unset, bool]):
        assumed_primary_reporting (Union[Unset, bool]):
        accepted_primary_withholding (Union[Unset, bool]):
        us_tax_purpose_type (Union[Unset, OrganizationApplicantUsTaxPurposeType]):
    """

    identifications: Union[Unset, List["OrganizationIdentification"]] = UNSET
    account_support: Union[Unset, "AccountSupportType"] = UNSET
    financial_information: Union[Unset, List["FinancialInformation"]] = UNSET
    accredited_investor_information: Union[Unset, "AccreditedInvestorInformation"] = UNSET
    regulatory_information: Union[Unset, List["RegulatoryInformation"]] = UNSET
    managing_owner: Union[Unset, "ManagingOwner"] = UNSET
    associated_entities: Union[Unset, "AssociatedEntities"] = UNSET
    regulated_memberships: Union[Unset, List["RegulatedMembership"]] = UNSET
    tax_residencies: Union[Unset, List["TaxResidency"]] = UNSET
    w_8_ben_e: Union[Unset, "FormW8BENE"] = UNSET
    w_8imy: Union[Unset, "FormW8IMY"] = UNSET
    withholding_statement: Union[Unset, "WithholdingStatementType"] = UNSET
    type_of_trading: Union[Unset, OrganizationApplicantTypeOfTrading] = UNSET
    type: Union[Unset, OrganizationApplicantType] = UNSET
    org_us_subsidiary: Union[Unset, bool] = UNSET
    qualified_intermediary: Union[Unset, bool] = UNSET
    assumed_primary_reporting: Union[Unset, bool] = UNSET
    accepted_primary_withholding: Union[Unset, bool] = UNSET
    us_tax_purpose_type: Union[Unset, OrganizationApplicantUsTaxPurposeType] = UNSET
    additional_properties: Dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> Dict[str, Any]:
        identifications: Union[Unset, List[Dict[str, Any]]] = UNSET
        if not isinstance(self.identifications, Unset):
            identifications = []
            for identifications_item_data in self.identifications:
                identifications_item = identifications_item_data.to_dict()
                identifications.append(identifications_item)

        account_support: Union[Unset, Dict[str, Any]] = UNSET
        if not isinstance(self.account_support, Unset):
            account_support = self.account_support.to_dict()

        financial_information: Union[Unset, List[Dict[str, Any]]] = UNSET
        if not isinstance(self.financial_information, Unset):
            financial_information = []
            for financial_information_item_data in self.financial_information:
                financial_information_item = financial_information_item_data.to_dict()
                financial_information.append(financial_information_item)

        accredited_investor_information: Union[Unset, Dict[str, Any]] = UNSET
        if not isinstance(self.accredited_investor_information, Unset):
            accredited_investor_information = self.accredited_investor_information.to_dict()

        regulatory_information: Union[Unset, List[Dict[str, Any]]] = UNSET
        if not isinstance(self.regulatory_information, Unset):
            regulatory_information = []
            for regulatory_information_item_data in self.regulatory_information:
                regulatory_information_item = regulatory_information_item_data.to_dict()
                regulatory_information.append(regulatory_information_item)

        managing_owner: Union[Unset, Dict[str, Any]] = UNSET
        if not isinstance(self.managing_owner, Unset):
            managing_owner = self.managing_owner.to_dict()

        associated_entities: Union[Unset, Dict[str, Any]] = UNSET
        if not isinstance(self.associated_entities, Unset):
            associated_entities = self.associated_entities.to_dict()

        regulated_memberships: Union[Unset, List[Dict[str, Any]]] = UNSET
        if not isinstance(self.regulated_memberships, Unset):
            regulated_memberships = []
            for regulated_memberships_item_data in self.regulated_memberships:
                regulated_memberships_item = regulated_memberships_item_data.to_dict()
                regulated_memberships.append(regulated_memberships_item)

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

        type_of_trading: Union[Unset, str] = UNSET
        if not isinstance(self.type_of_trading, Unset):
            type_of_trading = self.type_of_trading.value

        type: Union[Unset, str] = UNSET
        if not isinstance(self.type, Unset):
            type = self.type.value

        org_us_subsidiary = self.org_us_subsidiary

        qualified_intermediary = self.qualified_intermediary

        assumed_primary_reporting = self.assumed_primary_reporting

        accepted_primary_withholding = self.accepted_primary_withholding

        us_tax_purpose_type: Union[Unset, str] = UNSET
        if not isinstance(self.us_tax_purpose_type, Unset):
            us_tax_purpose_type = self.us_tax_purpose_type.value

        field_dict: Dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if identifications is not UNSET:
            field_dict["identifications"] = identifications
        if account_support is not UNSET:
            field_dict["accountSupport"] = account_support
        if financial_information is not UNSET:
            field_dict["financialInformation"] = financial_information
        if accredited_investor_information is not UNSET:
            field_dict["accreditedInvestorInformation"] = accredited_investor_information
        if regulatory_information is not UNSET:
            field_dict["regulatoryInformation"] = regulatory_information
        if managing_owner is not UNSET:
            field_dict["managingOwner"] = managing_owner
        if associated_entities is not UNSET:
            field_dict["associatedEntities"] = associated_entities
        if regulated_memberships is not UNSET:
            field_dict["regulatedMemberships"] = regulated_memberships
        if tax_residencies is not UNSET:
            field_dict["taxResidencies"] = tax_residencies
        if w_8_ben_e is not UNSET:
            field_dict["w8BenE"] = w_8_ben_e
        if w_8imy is not UNSET:
            field_dict["w8IMY"] = w_8imy
        if withholding_statement is not UNSET:
            field_dict["withholdingStatement"] = withholding_statement
        if type_of_trading is not UNSET:
            field_dict["typeOfTrading"] = type_of_trading
        if type is not UNSET:
            field_dict["type"] = type
        if org_us_subsidiary is not UNSET:
            field_dict["orgUsSubsidiary"] = org_us_subsidiary
        if qualified_intermediary is not UNSET:
            field_dict["qualifiedIntermediary"] = qualified_intermediary
        if assumed_primary_reporting is not UNSET:
            field_dict["assumedPrimaryReporting"] = assumed_primary_reporting
        if accepted_primary_withholding is not UNSET:
            field_dict["acceptedPrimaryWithholding"] = accepted_primary_withholding
        if us_tax_purpose_type is not UNSET:
            field_dict["usTaxPurposeType"] = us_tax_purpose_type

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        from ..models.account_support_type import AccountSupportType
        from ..models.accredited_investor_information import AccreditedInvestorInformation
        from ..models.associated_entities import AssociatedEntities
        from ..models.financial_information import FinancialInformation
        from ..models.form_w8bene import FormW8BENE
        from ..models.form_w8imy import FormW8IMY
        from ..models.managing_owner import ManagingOwner
        from ..models.organization_identification import OrganizationIdentification
        from ..models.regulated_membership import RegulatedMembership
        from ..models.regulatory_information import RegulatoryInformation
        from ..models.tax_residency import TaxResidency
        from ..models.withholding_statement_type import WithholdingStatementType

        d = src_dict.copy()
        identifications = []
        _identifications = d.pop("identifications", UNSET)
        for identifications_item_data in _identifications or []:
            identifications_item = OrganizationIdentification.from_dict(identifications_item_data)

            identifications.append(identifications_item)

        _account_support = d.pop("accountSupport", UNSET)
        account_support: Union[Unset, AccountSupportType]
        if isinstance(_account_support, Unset):
            account_support = UNSET
        else:
            account_support = AccountSupportType.from_dict(_account_support)

        financial_information = []
        _financial_information = d.pop("financialInformation", UNSET)
        for financial_information_item_data in _financial_information or []:
            financial_information_item = FinancialInformation.from_dict(financial_information_item_data)

            financial_information.append(financial_information_item)

        _accredited_investor_information = d.pop("accreditedInvestorInformation", UNSET)
        accredited_investor_information: Union[Unset, AccreditedInvestorInformation]
        if isinstance(_accredited_investor_information, Unset):
            accredited_investor_information = UNSET
        else:
            accredited_investor_information = AccreditedInvestorInformation.from_dict(_accredited_investor_information)

        regulatory_information = []
        _regulatory_information = d.pop("regulatoryInformation", UNSET)
        for regulatory_information_item_data in _regulatory_information or []:
            regulatory_information_item = RegulatoryInformation.from_dict(regulatory_information_item_data)

            regulatory_information.append(regulatory_information_item)

        _managing_owner = d.pop("managingOwner", UNSET)
        managing_owner: Union[Unset, ManagingOwner]
        if isinstance(_managing_owner, Unset):
            managing_owner = UNSET
        else:
            managing_owner = ManagingOwner.from_dict(_managing_owner)

        _associated_entities = d.pop("associatedEntities", UNSET)
        associated_entities: Union[Unset, AssociatedEntities]
        if isinstance(_associated_entities, Unset):
            associated_entities = UNSET
        else:
            associated_entities = AssociatedEntities.from_dict(_associated_entities)

        regulated_memberships = []
        _regulated_memberships = d.pop("regulatedMemberships", UNSET)
        for regulated_memberships_item_data in _regulated_memberships or []:
            regulated_memberships_item = RegulatedMembership.from_dict(regulated_memberships_item_data)

            regulated_memberships.append(regulated_memberships_item)

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

        _type_of_trading = d.pop("typeOfTrading", UNSET)
        type_of_trading: Union[Unset, OrganizationApplicantTypeOfTrading]
        if isinstance(_type_of_trading, Unset):
            type_of_trading = UNSET
        else:
            type_of_trading = OrganizationApplicantTypeOfTrading(_type_of_trading)

        _type = d.pop("type", UNSET)
        type: Union[Unset, OrganizationApplicantType]
        if isinstance(_type, Unset):
            type = UNSET
        else:
            type = OrganizationApplicantType(_type)

        org_us_subsidiary = d.pop("orgUsSubsidiary", UNSET)

        qualified_intermediary = d.pop("qualifiedIntermediary", UNSET)

        assumed_primary_reporting = d.pop("assumedPrimaryReporting", UNSET)

        accepted_primary_withholding = d.pop("acceptedPrimaryWithholding", UNSET)

        _us_tax_purpose_type = d.pop("usTaxPurposeType", UNSET)
        us_tax_purpose_type: Union[Unset, OrganizationApplicantUsTaxPurposeType]
        if isinstance(_us_tax_purpose_type, Unset):
            us_tax_purpose_type = UNSET
        else:
            us_tax_purpose_type = OrganizationApplicantUsTaxPurposeType(_us_tax_purpose_type)

        organization_applicant = cls(
            identifications=identifications,
            account_support=account_support,
            financial_information=financial_information,
            accredited_investor_information=accredited_investor_information,
            regulatory_information=regulatory_information,
            managing_owner=managing_owner,
            associated_entities=associated_entities,
            regulated_memberships=regulated_memberships,
            tax_residencies=tax_residencies,
            w_8_ben_e=w_8_ben_e,
            w_8imy=w_8imy,
            withholding_statement=withholding_statement,
            type_of_trading=type_of_trading,
            type=type,
            org_us_subsidiary=org_us_subsidiary,
            qualified_intermediary=qualified_intermediary,
            assumed_primary_reporting=assumed_primary_reporting,
            accepted_primary_withholding=accepted_primary_withholding,
            us_tax_purpose_type=us_tax_purpose_type,
        )

        organization_applicant.additional_properties = d
        return organization_applicant

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
