from typing import TYPE_CHECKING, Any, Dict, List, Type, TypeVar, Union, cast

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.account_data_capabilities import AccountDataCapabilities
    from ..models.account_data_fee_template import AccountDataFeeTemplate
    from ..models.account_data_mailing import AccountDataMailing
    from ..models.account_data_registered_address import AccountDataRegisteredAddress
    from ..models.account_data_stock_yield_program import AccountDataStockYieldProgram
    from ..models.account_data_tax_ids_item import AccountDataTaxIdsItem
    from ..models.account_data_tax_treaty_details_item import AccountDataTaxTreatyDetailsItem


T = TypeVar("T", bound="AccountData")


@_attrs_define
class AccountData:
    """
    Attributes:
        account_id (Union[Unset, str]):
        master_account_id (Union[Unset, str]):
        main_account (Union[Unset, str]):
        source_account_id (Union[Unset, str]):
        primary_user (Union[Unset, str]):
        clearing_status (Union[Unset, str]):
        clearing_status_description (Union[Unset, str]):
        state_code (Union[Unset, str]):
        base_currency (Union[Unset, str]):
        date_begun (Union[Unset, str]):
        date_approved (Union[Unset, str]):
        date_opened (Union[Unset, str]):
        date_funded (Union[Unset, str]):
        date_closed (Union[Unset, str]):
        date_linked (Union[Unset, str]):
        date_delinked (Union[Unset, str]):
        account_title (Union[Unset, str]):
        official_title (Union[Unset, str]):
        account_alias (Union[Unset, str]):
        email_address (Union[Unset, str]):
        margin (Union[Unset, str]):
        applicant_type (Union[Unset, str]):
        sub_type (Union[Unset, str]):
        stock_yield_program (Union[Unset, AccountDataStockYieldProgram]):
        fee_template (Union[Unset, AccountDataFeeTemplate]):
        capabilities (Union[Unset, AccountDataCapabilities]):
        limited_option_trading (Union[Unset, str]):
        investment_objectives (Union[Unset, List[str]]):
        external_id (Union[Unset, str]):
        mifid_category (Union[Unset, str]):
        mifir_status (Union[Unset, str]):
        equity (Union[Unset, float]):
        household (Union[Unset, str]):
        property_profile (Union[Unset, str]):
        process_type (Union[Unset, str]):
        risk_score (Union[Unset, int]):
        trust_type (Union[Unset, str]):
        org_type (Union[Unset, str]):
        business_description (Union[Unset, str]):
        us_tax_purpose_type (Union[Unset, str]):
        trade_intention_type (Union[Unset, str]):
        registered_address (Union[Unset, AccountDataRegisteredAddress]):
        mailing (Union[Unset, AccountDataMailing]):
        country_of_corporation (Union[Unset, str]):
        tax_ids (Union[Unset, List['AccountDataTaxIdsItem']]):
        tax_treaty_details (Union[Unset, List['AccountDataTaxTreatyDetailsItem']]):
    """

    account_id: Union[Unset, str] = UNSET
    master_account_id: Union[Unset, str] = UNSET
    main_account: Union[Unset, str] = UNSET
    source_account_id: Union[Unset, str] = UNSET
    primary_user: Union[Unset, str] = UNSET
    clearing_status: Union[Unset, str] = UNSET
    clearing_status_description: Union[Unset, str] = UNSET
    state_code: Union[Unset, str] = UNSET
    base_currency: Union[Unset, str] = UNSET
    date_begun: Union[Unset, str] = UNSET
    date_approved: Union[Unset, str] = UNSET
    date_opened: Union[Unset, str] = UNSET
    date_funded: Union[Unset, str] = UNSET
    date_closed: Union[Unset, str] = UNSET
    date_linked: Union[Unset, str] = UNSET
    date_delinked: Union[Unset, str] = UNSET
    account_title: Union[Unset, str] = UNSET
    official_title: Union[Unset, str] = UNSET
    account_alias: Union[Unset, str] = UNSET
    email_address: Union[Unset, str] = UNSET
    margin: Union[Unset, str] = UNSET
    applicant_type: Union[Unset, str] = UNSET
    sub_type: Union[Unset, str] = UNSET
    stock_yield_program: Union[Unset, "AccountDataStockYieldProgram"] = UNSET
    fee_template: Union[Unset, "AccountDataFeeTemplate"] = UNSET
    capabilities: Union[Unset, "AccountDataCapabilities"] = UNSET
    limited_option_trading: Union[Unset, str] = UNSET
    investment_objectives: Union[Unset, List[str]] = UNSET
    external_id: Union[Unset, str] = UNSET
    mifid_category: Union[Unset, str] = UNSET
    mifir_status: Union[Unset, str] = UNSET
    equity: Union[Unset, float] = UNSET
    household: Union[Unset, str] = UNSET
    property_profile: Union[Unset, str] = UNSET
    process_type: Union[Unset, str] = UNSET
    risk_score: Union[Unset, int] = UNSET
    trust_type: Union[Unset, str] = UNSET
    org_type: Union[Unset, str] = UNSET
    business_description: Union[Unset, str] = UNSET
    us_tax_purpose_type: Union[Unset, str] = UNSET
    trade_intention_type: Union[Unset, str] = UNSET
    registered_address: Union[Unset, "AccountDataRegisteredAddress"] = UNSET
    mailing: Union[Unset, "AccountDataMailing"] = UNSET
    country_of_corporation: Union[Unset, str] = UNSET
    tax_ids: Union[Unset, List["AccountDataTaxIdsItem"]] = UNSET
    tax_treaty_details: Union[Unset, List["AccountDataTaxTreatyDetailsItem"]] = UNSET
    additional_properties: Dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> Dict[str, Any]:
        account_id = self.account_id

        master_account_id = self.master_account_id

        main_account = self.main_account

        source_account_id = self.source_account_id

        primary_user = self.primary_user

        clearing_status = self.clearing_status

        clearing_status_description = self.clearing_status_description

        state_code = self.state_code

        base_currency = self.base_currency

        date_begun = self.date_begun

        date_approved = self.date_approved

        date_opened = self.date_opened

        date_funded = self.date_funded

        date_closed = self.date_closed

        date_linked = self.date_linked

        date_delinked = self.date_delinked

        account_title = self.account_title

        official_title = self.official_title

        account_alias = self.account_alias

        email_address = self.email_address

        margin = self.margin

        applicant_type = self.applicant_type

        sub_type = self.sub_type

        stock_yield_program: Union[Unset, Dict[str, Any]] = UNSET
        if not isinstance(self.stock_yield_program, Unset):
            stock_yield_program = self.stock_yield_program.to_dict()

        fee_template: Union[Unset, Dict[str, Any]] = UNSET
        if not isinstance(self.fee_template, Unset):
            fee_template = self.fee_template.to_dict()

        capabilities: Union[Unset, Dict[str, Any]] = UNSET
        if not isinstance(self.capabilities, Unset):
            capabilities = self.capabilities.to_dict()

        limited_option_trading = self.limited_option_trading

        investment_objectives: Union[Unset, List[str]] = UNSET
        if not isinstance(self.investment_objectives, Unset):
            investment_objectives = self.investment_objectives

        external_id = self.external_id

        mifid_category = self.mifid_category

        mifir_status = self.mifir_status

        equity = self.equity

        household = self.household

        property_profile = self.property_profile

        process_type = self.process_type

        risk_score = self.risk_score

        trust_type = self.trust_type

        org_type = self.org_type

        business_description = self.business_description

        us_tax_purpose_type = self.us_tax_purpose_type

        trade_intention_type = self.trade_intention_type

        registered_address: Union[Unset, Dict[str, Any]] = UNSET
        if not isinstance(self.registered_address, Unset):
            registered_address = self.registered_address.to_dict()

        mailing: Union[Unset, Dict[str, Any]] = UNSET
        if not isinstance(self.mailing, Unset):
            mailing = self.mailing.to_dict()

        country_of_corporation = self.country_of_corporation

        tax_ids: Union[Unset, List[Dict[str, Any]]] = UNSET
        if not isinstance(self.tax_ids, Unset):
            tax_ids = []
            for tax_ids_item_data in self.tax_ids:
                tax_ids_item = tax_ids_item_data.to_dict()
                tax_ids.append(tax_ids_item)

        tax_treaty_details: Union[Unset, List[Dict[str, Any]]] = UNSET
        if not isinstance(self.tax_treaty_details, Unset):
            tax_treaty_details = []
            for tax_treaty_details_item_data in self.tax_treaty_details:
                tax_treaty_details_item = tax_treaty_details_item_data.to_dict()
                tax_treaty_details.append(tax_treaty_details_item)

        field_dict: Dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if account_id is not UNSET:
            field_dict["accountId"] = account_id
        if master_account_id is not UNSET:
            field_dict["masterAccountId"] = master_account_id
        if main_account is not UNSET:
            field_dict["mainAccount"] = main_account
        if source_account_id is not UNSET:
            field_dict["sourceAccountId"] = source_account_id
        if primary_user is not UNSET:
            field_dict["primaryUser"] = primary_user
        if clearing_status is not UNSET:
            field_dict["clearingStatus"] = clearing_status
        if clearing_status_description is not UNSET:
            field_dict["clearingStatusDescription"] = clearing_status_description
        if state_code is not UNSET:
            field_dict["stateCode"] = state_code
        if base_currency is not UNSET:
            field_dict["baseCurrency"] = base_currency
        if date_begun is not UNSET:
            field_dict["dateBegun"] = date_begun
        if date_approved is not UNSET:
            field_dict["dateApproved"] = date_approved
        if date_opened is not UNSET:
            field_dict["dateOpened"] = date_opened
        if date_funded is not UNSET:
            field_dict["dateFunded"] = date_funded
        if date_closed is not UNSET:
            field_dict["dateClosed"] = date_closed
        if date_linked is not UNSET:
            field_dict["dateLinked"] = date_linked
        if date_delinked is not UNSET:
            field_dict["dateDelinked"] = date_delinked
        if account_title is not UNSET:
            field_dict["accountTitle"] = account_title
        if official_title is not UNSET:
            field_dict["officialTitle"] = official_title
        if account_alias is not UNSET:
            field_dict["accountAlias"] = account_alias
        if email_address is not UNSET:
            field_dict["emailAddress"] = email_address
        if margin is not UNSET:
            field_dict["margin"] = margin
        if applicant_type is not UNSET:
            field_dict["applicantType"] = applicant_type
        if sub_type is not UNSET:
            field_dict["subType"] = sub_type
        if stock_yield_program is not UNSET:
            field_dict["stockYieldProgram"] = stock_yield_program
        if fee_template is not UNSET:
            field_dict["feeTemplate"] = fee_template
        if capabilities is not UNSET:
            field_dict["capabilities"] = capabilities
        if limited_option_trading is not UNSET:
            field_dict["limitedOptionTrading"] = limited_option_trading
        if investment_objectives is not UNSET:
            field_dict["investmentObjectives"] = investment_objectives
        if external_id is not UNSET:
            field_dict["externalId"] = external_id
        if mifid_category is not UNSET:
            field_dict["mifidCategory"] = mifid_category
        if mifir_status is not UNSET:
            field_dict["mifirStatus"] = mifir_status
        if equity is not UNSET:
            field_dict["equity"] = equity
        if household is not UNSET:
            field_dict["household"] = household
        if property_profile is not UNSET:
            field_dict["propertyProfile"] = property_profile
        if process_type is not UNSET:
            field_dict["processType"] = process_type
        if risk_score is not UNSET:
            field_dict["riskScore"] = risk_score
        if trust_type is not UNSET:
            field_dict["trustType"] = trust_type
        if org_type is not UNSET:
            field_dict["orgType"] = org_type
        if business_description is not UNSET:
            field_dict["businessDescription"] = business_description
        if us_tax_purpose_type is not UNSET:
            field_dict["usTaxPurposeType"] = us_tax_purpose_type
        if trade_intention_type is not UNSET:
            field_dict["tradeIntentionType"] = trade_intention_type
        if registered_address is not UNSET:
            field_dict["registeredAddress"] = registered_address
        if mailing is not UNSET:
            field_dict["mailing"] = mailing
        if country_of_corporation is not UNSET:
            field_dict["countryOfCorporation"] = country_of_corporation
        if tax_ids is not UNSET:
            field_dict["taxIds"] = tax_ids
        if tax_treaty_details is not UNSET:
            field_dict["taxTreatyDetails"] = tax_treaty_details

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        from ..models.account_data_capabilities import AccountDataCapabilities
        from ..models.account_data_fee_template import AccountDataFeeTemplate
        from ..models.account_data_mailing import AccountDataMailing
        from ..models.account_data_registered_address import AccountDataRegisteredAddress
        from ..models.account_data_stock_yield_program import AccountDataStockYieldProgram
        from ..models.account_data_tax_ids_item import AccountDataTaxIdsItem
        from ..models.account_data_tax_treaty_details_item import AccountDataTaxTreatyDetailsItem

        d = src_dict.copy()
        account_id = d.pop("accountId", UNSET)

        master_account_id = d.pop("masterAccountId", UNSET)

        main_account = d.pop("mainAccount", UNSET)

        source_account_id = d.pop("sourceAccountId", UNSET)

        primary_user = d.pop("primaryUser", UNSET)

        clearing_status = d.pop("clearingStatus", UNSET)

        clearing_status_description = d.pop("clearingStatusDescription", UNSET)

        state_code = d.pop("stateCode", UNSET)

        base_currency = d.pop("baseCurrency", UNSET)

        date_begun = d.pop("dateBegun", UNSET)

        date_approved = d.pop("dateApproved", UNSET)

        date_opened = d.pop("dateOpened", UNSET)

        date_funded = d.pop("dateFunded", UNSET)

        date_closed = d.pop("dateClosed", UNSET)

        date_linked = d.pop("dateLinked", UNSET)

        date_delinked = d.pop("dateDelinked", UNSET)

        account_title = d.pop("accountTitle", UNSET)

        official_title = d.pop("officialTitle", UNSET)

        account_alias = d.pop("accountAlias", UNSET)

        email_address = d.pop("emailAddress", UNSET)

        margin = d.pop("margin", UNSET)

        applicant_type = d.pop("applicantType", UNSET)

        sub_type = d.pop("subType", UNSET)

        _stock_yield_program = d.pop("stockYieldProgram", UNSET)
        stock_yield_program: Union[Unset, AccountDataStockYieldProgram]
        if isinstance(_stock_yield_program, Unset):
            stock_yield_program = UNSET
        else:
            stock_yield_program = AccountDataStockYieldProgram.from_dict(_stock_yield_program)

        _fee_template = d.pop("feeTemplate", UNSET)
        fee_template: Union[Unset, AccountDataFeeTemplate]
        if isinstance(_fee_template, Unset):
            fee_template = UNSET
        else:
            fee_template = AccountDataFeeTemplate.from_dict(_fee_template)

        _capabilities = d.pop("capabilities", UNSET)
        capabilities: Union[Unset, AccountDataCapabilities]
        if isinstance(_capabilities, Unset):
            capabilities = UNSET
        else:
            capabilities = AccountDataCapabilities.from_dict(_capabilities)

        limited_option_trading = d.pop("limitedOptionTrading", UNSET)

        investment_objectives = cast(List[str], d.pop("investmentObjectives", UNSET))

        external_id = d.pop("externalId", UNSET)

        mifid_category = d.pop("mifidCategory", UNSET)

        mifir_status = d.pop("mifirStatus", UNSET)

        equity = d.pop("equity", UNSET)

        household = d.pop("household", UNSET)

        property_profile = d.pop("propertyProfile", UNSET)

        process_type = d.pop("processType", UNSET)

        risk_score = d.pop("riskScore", UNSET)

        trust_type = d.pop("trustType", UNSET)

        org_type = d.pop("orgType", UNSET)

        business_description = d.pop("businessDescription", UNSET)

        us_tax_purpose_type = d.pop("usTaxPurposeType", UNSET)

        trade_intention_type = d.pop("tradeIntentionType", UNSET)

        _registered_address = d.pop("registeredAddress", UNSET)
        registered_address: Union[Unset, AccountDataRegisteredAddress]
        if isinstance(_registered_address, Unset):
            registered_address = UNSET
        else:
            registered_address = AccountDataRegisteredAddress.from_dict(_registered_address)

        _mailing = d.pop("mailing", UNSET)
        mailing: Union[Unset, AccountDataMailing]
        if isinstance(_mailing, Unset):
            mailing = UNSET
        else:
            mailing = AccountDataMailing.from_dict(_mailing)

        country_of_corporation = d.pop("countryOfCorporation", UNSET)

        tax_ids = []
        _tax_ids = d.pop("taxIds", UNSET)
        for tax_ids_item_data in _tax_ids or []:
            tax_ids_item = AccountDataTaxIdsItem.from_dict(tax_ids_item_data)

            tax_ids.append(tax_ids_item)

        tax_treaty_details = []
        _tax_treaty_details = d.pop("taxTreatyDetails", UNSET)
        for tax_treaty_details_item_data in _tax_treaty_details or []:
            tax_treaty_details_item = AccountDataTaxTreatyDetailsItem.from_dict(tax_treaty_details_item_data)

            tax_treaty_details.append(tax_treaty_details_item)

        account_data = cls(
            account_id=account_id,
            master_account_id=master_account_id,
            main_account=main_account,
            source_account_id=source_account_id,
            primary_user=primary_user,
            clearing_status=clearing_status,
            clearing_status_description=clearing_status_description,
            state_code=state_code,
            base_currency=base_currency,
            date_begun=date_begun,
            date_approved=date_approved,
            date_opened=date_opened,
            date_funded=date_funded,
            date_closed=date_closed,
            date_linked=date_linked,
            date_delinked=date_delinked,
            account_title=account_title,
            official_title=official_title,
            account_alias=account_alias,
            email_address=email_address,
            margin=margin,
            applicant_type=applicant_type,
            sub_type=sub_type,
            stock_yield_program=stock_yield_program,
            fee_template=fee_template,
            capabilities=capabilities,
            limited_option_trading=limited_option_trading,
            investment_objectives=investment_objectives,
            external_id=external_id,
            mifid_category=mifid_category,
            mifir_status=mifir_status,
            equity=equity,
            household=household,
            property_profile=property_profile,
            process_type=process_type,
            risk_score=risk_score,
            trust_type=trust_type,
            org_type=org_type,
            business_description=business_description,
            us_tax_purpose_type=us_tax_purpose_type,
            trade_intention_type=trade_intention_type,
            registered_address=registered_address,
            mailing=mailing,
            country_of_corporation=country_of_corporation,
            tax_ids=tax_ids,
            tax_treaty_details=tax_treaty_details,
        )

        account_data.additional_properties = d
        return account_data

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
