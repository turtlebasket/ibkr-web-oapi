from typing import TYPE_CHECKING, Any, Dict, List, Type, TypeVar, Union

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..models.customer_type import CustomerType
from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.individual_applicant import IndividualApplicant
    from ..models.joint_applicant import JointApplicant
    from ..models.organization_applicant import OrganizationApplicant
    from ..models.trust_applicant import TrustApplicant


T = TypeVar("T", bound="Customer")


@_attrs_define
class Customer:
    """
    Attributes:
        organization (Union[Unset, OrganizationApplicant]):
        account_holder (Union[Unset, IndividualApplicant]):
        joint_holders (Union[Unset, JointApplicant]):
        trust (Union[Unset, TrustApplicant]):
        id (Union[Unset, str]):
        external_id (Union[Unset, str]):
        transfer_us_micro_cap_stock (Union[Unset, bool]):
        type (Union[Unset, CustomerType]):
        prefix (Union[Unset, str]):
        user_name (Union[Unset, str]):
        user_name_alias (Union[Unset, str]):
        user_name_source (Union[Unset, str]):
        email (Union[Unset, str]):
        md_status_non_pro (Union[Unset, bool]):
        preferred_primary_language (Union[Unset, str]):
        preferred_secondary_language (Union[Unset, str]):
        legal_residence_country (Union[Unset, str]):
        tax_treaty_country (Union[Unset, str]):
        meet_aml_standard (Union[Unset, str]):
        meets_aml_standard (Union[Unset, str]):
        direct_trading_access (Union[Unset, bool]):
        origin_country (Union[Unset, str]):
        termination_age (Union[Unset, int]):
        governing_state (Union[Unset, str]):
        opt_for_debit_card (Union[Unset, bool]):
        robo_fa_client (Union[Unset, bool]):
        independent_account (Union[Unset, bool]):
        paper_account (Union[Unset, bool]):
    """

    organization: Union[Unset, "OrganizationApplicant"] = UNSET
    account_holder: Union[Unset, "IndividualApplicant"] = UNSET
    joint_holders: Union[Unset, "JointApplicant"] = UNSET
    trust: Union[Unset, "TrustApplicant"] = UNSET
    id: Union[Unset, str] = UNSET
    external_id: Union[Unset, str] = UNSET
    transfer_us_micro_cap_stock: Union[Unset, bool] = UNSET
    type: Union[Unset, CustomerType] = UNSET
    prefix: Union[Unset, str] = UNSET
    user_name: Union[Unset, str] = UNSET
    user_name_alias: Union[Unset, str] = UNSET
    user_name_source: Union[Unset, str] = UNSET
    email: Union[Unset, str] = UNSET
    md_status_non_pro: Union[Unset, bool] = UNSET
    preferred_primary_language: Union[Unset, str] = UNSET
    preferred_secondary_language: Union[Unset, str] = UNSET
    legal_residence_country: Union[Unset, str] = UNSET
    tax_treaty_country: Union[Unset, str] = UNSET
    meet_aml_standard: Union[Unset, str] = UNSET
    meets_aml_standard: Union[Unset, str] = UNSET
    direct_trading_access: Union[Unset, bool] = UNSET
    origin_country: Union[Unset, str] = UNSET
    termination_age: Union[Unset, int] = UNSET
    governing_state: Union[Unset, str] = UNSET
    opt_for_debit_card: Union[Unset, bool] = UNSET
    robo_fa_client: Union[Unset, bool] = UNSET
    independent_account: Union[Unset, bool] = UNSET
    paper_account: Union[Unset, bool] = UNSET
    additional_properties: Dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> Dict[str, Any]:
        organization: Union[Unset, Dict[str, Any]] = UNSET
        if not isinstance(self.organization, Unset):
            organization = self.organization.to_dict()

        account_holder: Union[Unset, Dict[str, Any]] = UNSET
        if not isinstance(self.account_holder, Unset):
            account_holder = self.account_holder.to_dict()

        joint_holders: Union[Unset, Dict[str, Any]] = UNSET
        if not isinstance(self.joint_holders, Unset):
            joint_holders = self.joint_holders.to_dict()

        trust: Union[Unset, Dict[str, Any]] = UNSET
        if not isinstance(self.trust, Unset):
            trust = self.trust.to_dict()

        id = self.id

        external_id = self.external_id

        transfer_us_micro_cap_stock = self.transfer_us_micro_cap_stock

        type: Union[Unset, str] = UNSET
        if not isinstance(self.type, Unset):
            type = self.type.value

        prefix = self.prefix

        user_name = self.user_name

        user_name_alias = self.user_name_alias

        user_name_source = self.user_name_source

        email = self.email

        md_status_non_pro = self.md_status_non_pro

        preferred_primary_language = self.preferred_primary_language

        preferred_secondary_language = self.preferred_secondary_language

        legal_residence_country = self.legal_residence_country

        tax_treaty_country = self.tax_treaty_country

        meet_aml_standard = self.meet_aml_standard

        meets_aml_standard = self.meets_aml_standard

        direct_trading_access = self.direct_trading_access

        origin_country = self.origin_country

        termination_age = self.termination_age

        governing_state = self.governing_state

        opt_for_debit_card = self.opt_for_debit_card

        robo_fa_client = self.robo_fa_client

        independent_account = self.independent_account

        paper_account = self.paper_account

        field_dict: Dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if organization is not UNSET:
            field_dict["organization"] = organization
        if account_holder is not UNSET:
            field_dict["accountHolder"] = account_holder
        if joint_holders is not UNSET:
            field_dict["jointHolders"] = joint_holders
        if trust is not UNSET:
            field_dict["trust"] = trust
        if id is not UNSET:
            field_dict["id"] = id
        if external_id is not UNSET:
            field_dict["externalId"] = external_id
        if transfer_us_micro_cap_stock is not UNSET:
            field_dict["transferUsMicroCapStock"] = transfer_us_micro_cap_stock
        if type is not UNSET:
            field_dict["type"] = type
        if prefix is not UNSET:
            field_dict["prefix"] = prefix
        if user_name is not UNSET:
            field_dict["userName"] = user_name
        if user_name_alias is not UNSET:
            field_dict["userNameAlias"] = user_name_alias
        if user_name_source is not UNSET:
            field_dict["userNameSource"] = user_name_source
        if email is not UNSET:
            field_dict["email"] = email
        if md_status_non_pro is not UNSET:
            field_dict["mdStatusNonPro"] = md_status_non_pro
        if preferred_primary_language is not UNSET:
            field_dict["preferredPrimaryLanguage"] = preferred_primary_language
        if preferred_secondary_language is not UNSET:
            field_dict["preferredSecondaryLanguage"] = preferred_secondary_language
        if legal_residence_country is not UNSET:
            field_dict["legalResidenceCountry"] = legal_residence_country
        if tax_treaty_country is not UNSET:
            field_dict["taxTreatyCountry"] = tax_treaty_country
        if meet_aml_standard is not UNSET:
            field_dict["meetAmlStandard"] = meet_aml_standard
        if meets_aml_standard is not UNSET:
            field_dict["meetsAmlStandard"] = meets_aml_standard
        if direct_trading_access is not UNSET:
            field_dict["directTradingAccess"] = direct_trading_access
        if origin_country is not UNSET:
            field_dict["originCountry"] = origin_country
        if termination_age is not UNSET:
            field_dict["terminationAge"] = termination_age
        if governing_state is not UNSET:
            field_dict["governingState"] = governing_state
        if opt_for_debit_card is not UNSET:
            field_dict["optForDebitCard"] = opt_for_debit_card
        if robo_fa_client is not UNSET:
            field_dict["roboFaClient"] = robo_fa_client
        if independent_account is not UNSET:
            field_dict["independentAccount"] = independent_account
        if paper_account is not UNSET:
            field_dict["paperAccount"] = paper_account

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        from ..models.individual_applicant import IndividualApplicant
        from ..models.joint_applicant import JointApplicant
        from ..models.organization_applicant import OrganizationApplicant
        from ..models.trust_applicant import TrustApplicant

        d = src_dict.copy()
        _organization = d.pop("organization", UNSET)
        organization: Union[Unset, OrganizationApplicant]
        if isinstance(_organization, Unset):
            organization = UNSET
        else:
            organization = OrganizationApplicant.from_dict(_organization)

        _account_holder = d.pop("accountHolder", UNSET)
        account_holder: Union[Unset, IndividualApplicant]
        if isinstance(_account_holder, Unset):
            account_holder = UNSET
        else:
            account_holder = IndividualApplicant.from_dict(_account_holder)

        _joint_holders = d.pop("jointHolders", UNSET)
        joint_holders: Union[Unset, JointApplicant]
        if isinstance(_joint_holders, Unset):
            joint_holders = UNSET
        else:
            joint_holders = JointApplicant.from_dict(_joint_holders)

        _trust = d.pop("trust", UNSET)
        trust: Union[Unset, TrustApplicant]
        if isinstance(_trust, Unset):
            trust = UNSET
        else:
            trust = TrustApplicant.from_dict(_trust)

        id = d.pop("id", UNSET)

        external_id = d.pop("externalId", UNSET)

        transfer_us_micro_cap_stock = d.pop("transferUsMicroCapStock", UNSET)

        _type = d.pop("type", UNSET)
        type: Union[Unset, CustomerType]
        if isinstance(_type, Unset):
            type = UNSET
        else:
            type = CustomerType(_type)

        prefix = d.pop("prefix", UNSET)

        user_name = d.pop("userName", UNSET)

        user_name_alias = d.pop("userNameAlias", UNSET)

        user_name_source = d.pop("userNameSource", UNSET)

        email = d.pop("email", UNSET)

        md_status_non_pro = d.pop("mdStatusNonPro", UNSET)

        preferred_primary_language = d.pop("preferredPrimaryLanguage", UNSET)

        preferred_secondary_language = d.pop("preferredSecondaryLanguage", UNSET)

        legal_residence_country = d.pop("legalResidenceCountry", UNSET)

        tax_treaty_country = d.pop("taxTreatyCountry", UNSET)

        meet_aml_standard = d.pop("meetAmlStandard", UNSET)

        meets_aml_standard = d.pop("meetsAmlStandard", UNSET)

        direct_trading_access = d.pop("directTradingAccess", UNSET)

        origin_country = d.pop("originCountry", UNSET)

        termination_age = d.pop("terminationAge", UNSET)

        governing_state = d.pop("governingState", UNSET)

        opt_for_debit_card = d.pop("optForDebitCard", UNSET)

        robo_fa_client = d.pop("roboFaClient", UNSET)

        independent_account = d.pop("independentAccount", UNSET)

        paper_account = d.pop("paperAccount", UNSET)

        customer = cls(
            organization=organization,
            account_holder=account_holder,
            joint_holders=joint_holders,
            trust=trust,
            id=id,
            external_id=external_id,
            transfer_us_micro_cap_stock=transfer_us_micro_cap_stock,
            type=type,
            prefix=prefix,
            user_name=user_name,
            user_name_alias=user_name_alias,
            user_name_source=user_name_source,
            email=email,
            md_status_non_pro=md_status_non_pro,
            preferred_primary_language=preferred_primary_language,
            preferred_secondary_language=preferred_secondary_language,
            legal_residence_country=legal_residence_country,
            tax_treaty_country=tax_treaty_country,
            meet_aml_standard=meet_aml_standard,
            meets_aml_standard=meets_aml_standard,
            direct_trading_access=direct_trading_access,
            origin_country=origin_country,
            termination_age=termination_age,
            governing_state=governing_state,
            opt_for_debit_card=opt_for_debit_card,
            robo_fa_client=robo_fa_client,
            independent_account=independent_account,
            paper_account=paper_account,
        )

        customer.additional_properties = d
        return customer

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
