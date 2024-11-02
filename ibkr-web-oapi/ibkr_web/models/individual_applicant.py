from typing import TYPE_CHECKING, Any, Dict, List, Type, TypeVar, Union

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.accredited_investor_information import AccreditedInvestorInformation
    from ..models.associated_individual import AssociatedIndividual
    from ..models.financial_information import FinancialInformation
    from ..models.individual_tax_information import IndividualTaxInformation
    from ..models.regulated_membership import RegulatedMembership
    from ..models.regulatory_information import RegulatoryInformation
    from ..models.withholding_statement_type import WithholdingStatementType


T = TypeVar("T", bound="IndividualApplicant")


@_attrs_define
class IndividualApplicant:
    """
    Attributes:
        account_holder_details (Union[Unset, List['AssociatedIndividual']]):
        financial_information (Union[Unset, List['FinancialInformation']]):
        regulatory_information (Union[Unset, List['RegulatoryInformation']]):
        regulated_memberships (Union[Unset, List['RegulatedMembership']]):
        accredited_investor_information (Union[Unset, AccreditedInvestorInformation]):
        tax_information (Union[Unset, IndividualTaxInformation]):
        withholding_statement (Union[Unset, WithholdingStatementType]):
    """

    account_holder_details: Union[Unset, List["AssociatedIndividual"]] = UNSET
    financial_information: Union[Unset, List["FinancialInformation"]] = UNSET
    regulatory_information: Union[Unset, List["RegulatoryInformation"]] = UNSET
    regulated_memberships: Union[Unset, List["RegulatedMembership"]] = UNSET
    accredited_investor_information: Union[Unset, "AccreditedInvestorInformation"] = UNSET
    tax_information: Union[Unset, "IndividualTaxInformation"] = UNSET
    withholding_statement: Union[Unset, "WithholdingStatementType"] = UNSET
    additional_properties: Dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> Dict[str, Any]:
        account_holder_details: Union[Unset, List[Dict[str, Any]]] = UNSET
        if not isinstance(self.account_holder_details, Unset):
            account_holder_details = []
            for account_holder_details_item_data in self.account_holder_details:
                account_holder_details_item = account_holder_details_item_data.to_dict()
                account_holder_details.append(account_holder_details_item)

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

        tax_information: Union[Unset, Dict[str, Any]] = UNSET
        if not isinstance(self.tax_information, Unset):
            tax_information = self.tax_information.to_dict()

        withholding_statement: Union[Unset, Dict[str, Any]] = UNSET
        if not isinstance(self.withholding_statement, Unset):
            withholding_statement = self.withholding_statement.to_dict()

        field_dict: Dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if account_holder_details is not UNSET:
            field_dict["accountHolderDetails"] = account_holder_details
        if financial_information is not UNSET:
            field_dict["financialInformation"] = financial_information
        if regulatory_information is not UNSET:
            field_dict["regulatoryInformation"] = regulatory_information
        if regulated_memberships is not UNSET:
            field_dict["regulatedMemberships"] = regulated_memberships
        if accredited_investor_information is not UNSET:
            field_dict["accreditedInvestorInformation"] = accredited_investor_information
        if tax_information is not UNSET:
            field_dict["taxInformation"] = tax_information
        if withholding_statement is not UNSET:
            field_dict["withholdingStatement"] = withholding_statement

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        from ..models.accredited_investor_information import AccreditedInvestorInformation
        from ..models.associated_individual import AssociatedIndividual
        from ..models.financial_information import FinancialInformation
        from ..models.individual_tax_information import IndividualTaxInformation
        from ..models.regulated_membership import RegulatedMembership
        from ..models.regulatory_information import RegulatoryInformation
        from ..models.withholding_statement_type import WithholdingStatementType

        d = src_dict.copy()
        account_holder_details = []
        _account_holder_details = d.pop("accountHolderDetails", UNSET)
        for account_holder_details_item_data in _account_holder_details or []:
            account_holder_details_item = AssociatedIndividual.from_dict(account_holder_details_item_data)

            account_holder_details.append(account_holder_details_item)

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

        _tax_information = d.pop("taxInformation", UNSET)
        tax_information: Union[Unset, IndividualTaxInformation]
        if isinstance(_tax_information, Unset):
            tax_information = UNSET
        else:
            tax_information = IndividualTaxInformation.from_dict(_tax_information)

        _withholding_statement = d.pop("withholdingStatement", UNSET)
        withholding_statement: Union[Unset, WithholdingStatementType]
        if isinstance(_withholding_statement, Unset):
            withholding_statement = UNSET
        else:
            withholding_statement = WithholdingStatementType.from_dict(_withholding_statement)

        individual_applicant = cls(
            account_holder_details=account_holder_details,
            financial_information=financial_information,
            regulatory_information=regulatory_information,
            regulated_memberships=regulated_memberships,
            accredited_investor_information=accredited_investor_information,
            tax_information=tax_information,
            withholding_statement=withholding_statement,
        )

        individual_applicant.additional_properties = d
        return individual_applicant

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
