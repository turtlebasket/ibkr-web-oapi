from typing import TYPE_CHECKING, Any, Dict, List, Type, TypeVar, Union

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..models.account_account_type import AccountAccountType
from ..models.account_base_currency import AccountBaseCurrency
from ..models.account_brokerage_service_codes_item import AccountBrokerageServiceCodesItem
from ..models.account_capabilities_item import AccountCapabilitiesItem
from ..models.account_investment_objectives_item import AccountInvestmentObjectivesItem
from ..models.account_ira_type import AccountIraType
from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.account_configuration_type import AccountConfigurationType
    from ..models.account_rep import AccountRep
    from ..models.ach_instruction import ACHInstruction
    from ..models.advisor_wrap_fees_type import AdvisorWrapFeesType
    from ..models.commission_config import CommissionConfig
    from ..models.commission_schedule_type import CommissionScheduleType
    from ..models.custodian_type import CustodianType
    from ..models.deposit_notification import DepositNotification
    from ..models.dvp_instruction import DVPInstruction
    from ..models.exchange_access import ExchangeAccess
    from ..models.ext_positions_transfer_type import ExtPositionsTransferType
    from ..models.interest_markup_type import InterestMarkupType
    from ..models.ira_beneficiaries_type import IRABeneficiariesType
    from ..models.ira_decedent import IRADecedent
    from ..models.recurring_transaction import RecurringTransaction
    from ..models.trading_limits import TradingLimits
    from ..models.trading_permission import TradingPermission


T = TypeVar("T", bound="Account")


@_attrs_define
class Account:
    """
    Attributes:
        account_configuration (Union[Unset, AccountConfigurationType]):
        investment_objectives (Union[Unset, List[AccountInvestmentObjectivesItem]]):
        brokerage_service_codes (Union[Unset, List[AccountBrokerageServiceCodesItem]]):
        capabilities (Union[Unset, List[AccountCapabilitiesItem]]):
        trading_permissions (Union[Unset, List['TradingPermission']]):
        commission_configs (Union[Unset, List['CommissionConfig']]):
        all_exchange_access (Union[Unset, List['ExchangeAccess']]):
        dvp_instructions (Union[Unset, List['DVPInstruction']]):
        trading_limits (Union[Unset, TradingLimits]):
        advisor_wrap_fees (Union[Unset, AdvisorWrapFeesType]):
        fees_template_name (Union[Unset, str]):
        client_commission_schedule (Union[Unset, CommissionScheduleType]):
        client_interest_markup_schedules (Union[Unset, List['InterestMarkupType']]):
        decendent (Union[Unset, IRADecedent]):
        ira_beneficiaries (Union[Unset, IRABeneficiariesType]):
        ext_positions_transfers (Union[Unset, List['ExtPositionsTransferType']]):
        deposit_notification (Union[Unset, DepositNotification]):
        ach_instructions (Union[Unset, List['ACHInstruction']]):
        recurring_transactions (Union[Unset, List['RecurringTransaction']]):
        custodian (Union[Unset, CustodianType]):
        successor_custodian (Union[Unset, CustodianType]):
        account_rep (Union[Unset, AccountRep]):
        id (Union[Unset, str]):
        external_id (Union[Unset, str]):
        property_profile (Union[Unset, str]):
        base_currency (Union[Unset, AccountBaseCurrency]):
        employee_plan (Union[Unset, str]):
        multi_currency (Union[Unset, bool]):
        migration (Union[Unset, bool]):
        source_account_id (Union[Unset, str]):
        margin (Union[Unset, str]):
        ira (Union[Unset, bool]):
        ira_type (Union[Unset, AccountIraType]):
        ira_official_title (Union[Unset, str]):
        client_active_trading (Union[Unset, bool]):
        duplicate (Union[Unset, bool]):
        number_of_duplicates (Union[Unset, int]):
        stock_yield_program (Union[Unset, bool]):
        alias (Union[Unset, str]):
        account_type (Union[Unset, AccountAccountType]):
        drip (Union[Unset, bool]):
        limited_options (Union[Unset, bool]):
    """

    account_configuration: Union[Unset, "AccountConfigurationType"] = UNSET
    investment_objectives: Union[Unset, List[AccountInvestmentObjectivesItem]] = UNSET
    brokerage_service_codes: Union[Unset, List[AccountBrokerageServiceCodesItem]] = UNSET
    capabilities: Union[Unset, List[AccountCapabilitiesItem]] = UNSET
    trading_permissions: Union[Unset, List["TradingPermission"]] = UNSET
    commission_configs: Union[Unset, List["CommissionConfig"]] = UNSET
    all_exchange_access: Union[Unset, List["ExchangeAccess"]] = UNSET
    dvp_instructions: Union[Unset, List["DVPInstruction"]] = UNSET
    trading_limits: Union[Unset, "TradingLimits"] = UNSET
    advisor_wrap_fees: Union[Unset, "AdvisorWrapFeesType"] = UNSET
    fees_template_name: Union[Unset, str] = UNSET
    client_commission_schedule: Union[Unset, "CommissionScheduleType"] = UNSET
    client_interest_markup_schedules: Union[Unset, List["InterestMarkupType"]] = UNSET
    decendent: Union[Unset, "IRADecedent"] = UNSET
    ira_beneficiaries: Union[Unset, "IRABeneficiariesType"] = UNSET
    ext_positions_transfers: Union[Unset, List["ExtPositionsTransferType"]] = UNSET
    deposit_notification: Union[Unset, "DepositNotification"] = UNSET
    ach_instructions: Union[Unset, List["ACHInstruction"]] = UNSET
    recurring_transactions: Union[Unset, List["RecurringTransaction"]] = UNSET
    custodian: Union[Unset, "CustodianType"] = UNSET
    successor_custodian: Union[Unset, "CustodianType"] = UNSET
    account_rep: Union[Unset, "AccountRep"] = UNSET
    id: Union[Unset, str] = UNSET
    external_id: Union[Unset, str] = UNSET
    property_profile: Union[Unset, str] = UNSET
    base_currency: Union[Unset, AccountBaseCurrency] = UNSET
    employee_plan: Union[Unset, str] = UNSET
    multi_currency: Union[Unset, bool] = UNSET
    migration: Union[Unset, bool] = UNSET
    source_account_id: Union[Unset, str] = UNSET
    margin: Union[Unset, str] = UNSET
    ira: Union[Unset, bool] = UNSET
    ira_type: Union[Unset, AccountIraType] = UNSET
    ira_official_title: Union[Unset, str] = UNSET
    client_active_trading: Union[Unset, bool] = UNSET
    duplicate: Union[Unset, bool] = UNSET
    number_of_duplicates: Union[Unset, int] = UNSET
    stock_yield_program: Union[Unset, bool] = UNSET
    alias: Union[Unset, str] = UNSET
    account_type: Union[Unset, AccountAccountType] = UNSET
    drip: Union[Unset, bool] = UNSET
    limited_options: Union[Unset, bool] = UNSET
    additional_properties: Dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> Dict[str, Any]:
        account_configuration: Union[Unset, Dict[str, Any]] = UNSET
        if not isinstance(self.account_configuration, Unset):
            account_configuration = self.account_configuration.to_dict()

        investment_objectives: Union[Unset, List[str]] = UNSET
        if not isinstance(self.investment_objectives, Unset):
            investment_objectives = []
            for investment_objectives_item_data in self.investment_objectives:
                investment_objectives_item = investment_objectives_item_data.value
                investment_objectives.append(investment_objectives_item)

        brokerage_service_codes: Union[Unset, List[str]] = UNSET
        if not isinstance(self.brokerage_service_codes, Unset):
            brokerage_service_codes = []
            for brokerage_service_codes_item_data in self.brokerage_service_codes:
                brokerage_service_codes_item = brokerage_service_codes_item_data.value
                brokerage_service_codes.append(brokerage_service_codes_item)

        capabilities: Union[Unset, List[str]] = UNSET
        if not isinstance(self.capabilities, Unset):
            capabilities = []
            for capabilities_item_data in self.capabilities:
                capabilities_item = capabilities_item_data.value
                capabilities.append(capabilities_item)

        trading_permissions: Union[Unset, List[Dict[str, Any]]] = UNSET
        if not isinstance(self.trading_permissions, Unset):
            trading_permissions = []
            for trading_permissions_item_data in self.trading_permissions:
                trading_permissions_item = trading_permissions_item_data.to_dict()
                trading_permissions.append(trading_permissions_item)

        commission_configs: Union[Unset, List[Dict[str, Any]]] = UNSET
        if not isinstance(self.commission_configs, Unset):
            commission_configs = []
            for commission_configs_item_data in self.commission_configs:
                commission_configs_item = commission_configs_item_data.to_dict()
                commission_configs.append(commission_configs_item)

        all_exchange_access: Union[Unset, List[Dict[str, Any]]] = UNSET
        if not isinstance(self.all_exchange_access, Unset):
            all_exchange_access = []
            for all_exchange_access_item_data in self.all_exchange_access:
                all_exchange_access_item = all_exchange_access_item_data.to_dict()
                all_exchange_access.append(all_exchange_access_item)

        dvp_instructions: Union[Unset, List[Dict[str, Any]]] = UNSET
        if not isinstance(self.dvp_instructions, Unset):
            dvp_instructions = []
            for dvp_instructions_item_data in self.dvp_instructions:
                dvp_instructions_item = dvp_instructions_item_data.to_dict()
                dvp_instructions.append(dvp_instructions_item)

        trading_limits: Union[Unset, Dict[str, Any]] = UNSET
        if not isinstance(self.trading_limits, Unset):
            trading_limits = self.trading_limits.to_dict()

        advisor_wrap_fees: Union[Unset, Dict[str, Any]] = UNSET
        if not isinstance(self.advisor_wrap_fees, Unset):
            advisor_wrap_fees = self.advisor_wrap_fees.to_dict()

        fees_template_name = self.fees_template_name

        client_commission_schedule: Union[Unset, Dict[str, Any]] = UNSET
        if not isinstance(self.client_commission_schedule, Unset):
            client_commission_schedule = self.client_commission_schedule.to_dict()

        client_interest_markup_schedules: Union[Unset, List[Dict[str, Any]]] = UNSET
        if not isinstance(self.client_interest_markup_schedules, Unset):
            client_interest_markup_schedules = []
            for client_interest_markup_schedules_item_data in self.client_interest_markup_schedules:
                client_interest_markup_schedules_item = client_interest_markup_schedules_item_data.to_dict()
                client_interest_markup_schedules.append(client_interest_markup_schedules_item)

        decendent: Union[Unset, Dict[str, Any]] = UNSET
        if not isinstance(self.decendent, Unset):
            decendent = self.decendent.to_dict()

        ira_beneficiaries: Union[Unset, Dict[str, Any]] = UNSET
        if not isinstance(self.ira_beneficiaries, Unset):
            ira_beneficiaries = self.ira_beneficiaries.to_dict()

        ext_positions_transfers: Union[Unset, List[Dict[str, Any]]] = UNSET
        if not isinstance(self.ext_positions_transfers, Unset):
            ext_positions_transfers = []
            for ext_positions_transfers_item_data in self.ext_positions_transfers:
                ext_positions_transfers_item = ext_positions_transfers_item_data.to_dict()
                ext_positions_transfers.append(ext_positions_transfers_item)

        deposit_notification: Union[Unset, Dict[str, Any]] = UNSET
        if not isinstance(self.deposit_notification, Unset):
            deposit_notification = self.deposit_notification.to_dict()

        ach_instructions: Union[Unset, List[Dict[str, Any]]] = UNSET
        if not isinstance(self.ach_instructions, Unset):
            ach_instructions = []
            for ach_instructions_item_data in self.ach_instructions:
                ach_instructions_item = ach_instructions_item_data.to_dict()
                ach_instructions.append(ach_instructions_item)

        recurring_transactions: Union[Unset, List[Dict[str, Any]]] = UNSET
        if not isinstance(self.recurring_transactions, Unset):
            recurring_transactions = []
            for recurring_transactions_item_data in self.recurring_transactions:
                recurring_transactions_item = recurring_transactions_item_data.to_dict()
                recurring_transactions.append(recurring_transactions_item)

        custodian: Union[Unset, Dict[str, Any]] = UNSET
        if not isinstance(self.custodian, Unset):
            custodian = self.custodian.to_dict()

        successor_custodian: Union[Unset, Dict[str, Any]] = UNSET
        if not isinstance(self.successor_custodian, Unset):
            successor_custodian = self.successor_custodian.to_dict()

        account_rep: Union[Unset, Dict[str, Any]] = UNSET
        if not isinstance(self.account_rep, Unset):
            account_rep = self.account_rep.to_dict()

        id = self.id

        external_id = self.external_id

        property_profile = self.property_profile

        base_currency: Union[Unset, str] = UNSET
        if not isinstance(self.base_currency, Unset):
            base_currency = self.base_currency.value

        employee_plan = self.employee_plan

        multi_currency = self.multi_currency

        migration = self.migration

        source_account_id = self.source_account_id

        margin = self.margin

        ira = self.ira

        ira_type: Union[Unset, str] = UNSET
        if not isinstance(self.ira_type, Unset):
            ira_type = self.ira_type.value

        ira_official_title = self.ira_official_title

        client_active_trading = self.client_active_trading

        duplicate = self.duplicate

        number_of_duplicates = self.number_of_duplicates

        stock_yield_program = self.stock_yield_program

        alias = self.alias

        account_type: Union[Unset, str] = UNSET
        if not isinstance(self.account_type, Unset):
            account_type = self.account_type.value

        drip = self.drip

        limited_options = self.limited_options

        field_dict: Dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if account_configuration is not UNSET:
            field_dict["accountConfiguration"] = account_configuration
        if investment_objectives is not UNSET:
            field_dict["investmentObjectives"] = investment_objectives
        if brokerage_service_codes is not UNSET:
            field_dict["brokerageServiceCodes"] = brokerage_service_codes
        if capabilities is not UNSET:
            field_dict["capabilities"] = capabilities
        if trading_permissions is not UNSET:
            field_dict["tradingPermissions"] = trading_permissions
        if commission_configs is not UNSET:
            field_dict["commissionConfigs"] = commission_configs
        if all_exchange_access is not UNSET:
            field_dict["allExchangeAccess"] = all_exchange_access
        if dvp_instructions is not UNSET:
            field_dict["dvpInstructions"] = dvp_instructions
        if trading_limits is not UNSET:
            field_dict["tradingLimits"] = trading_limits
        if advisor_wrap_fees is not UNSET:
            field_dict["advisorWrapFees"] = advisor_wrap_fees
        if fees_template_name is not UNSET:
            field_dict["feesTemplateName"] = fees_template_name
        if client_commission_schedule is not UNSET:
            field_dict["clientCommissionSchedule"] = client_commission_schedule
        if client_interest_markup_schedules is not UNSET:
            field_dict["clientInterestMarkupSchedules"] = client_interest_markup_schedules
        if decendent is not UNSET:
            field_dict["decendent"] = decendent
        if ira_beneficiaries is not UNSET:
            field_dict["iraBeneficiaries"] = ira_beneficiaries
        if ext_positions_transfers is not UNSET:
            field_dict["extPositionsTransfers"] = ext_positions_transfers
        if deposit_notification is not UNSET:
            field_dict["depositNotification"] = deposit_notification
        if ach_instructions is not UNSET:
            field_dict["achInstructions"] = ach_instructions
        if recurring_transactions is not UNSET:
            field_dict["recurringTransactions"] = recurring_transactions
        if custodian is not UNSET:
            field_dict["custodian"] = custodian
        if successor_custodian is not UNSET:
            field_dict["successorCustodian"] = successor_custodian
        if account_rep is not UNSET:
            field_dict["accountRep"] = account_rep
        if id is not UNSET:
            field_dict["id"] = id
        if external_id is not UNSET:
            field_dict["externalId"] = external_id
        if property_profile is not UNSET:
            field_dict["propertyProfile"] = property_profile
        if base_currency is not UNSET:
            field_dict["baseCurrency"] = base_currency
        if employee_plan is not UNSET:
            field_dict["employeePlan"] = employee_plan
        if multi_currency is not UNSET:
            field_dict["multiCurrency"] = multi_currency
        if migration is not UNSET:
            field_dict["migration"] = migration
        if source_account_id is not UNSET:
            field_dict["sourceAccountId"] = source_account_id
        if margin is not UNSET:
            field_dict["margin"] = margin
        if ira is not UNSET:
            field_dict["ira"] = ira
        if ira_type is not UNSET:
            field_dict["iraType"] = ira_type
        if ira_official_title is not UNSET:
            field_dict["iraOfficialTitle"] = ira_official_title
        if client_active_trading is not UNSET:
            field_dict["clientActiveTrading"] = client_active_trading
        if duplicate is not UNSET:
            field_dict["duplicate"] = duplicate
        if number_of_duplicates is not UNSET:
            field_dict["numberOfDuplicates"] = number_of_duplicates
        if stock_yield_program is not UNSET:
            field_dict["stockYieldProgram"] = stock_yield_program
        if alias is not UNSET:
            field_dict["alias"] = alias
        if account_type is not UNSET:
            field_dict["accountType"] = account_type
        if drip is not UNSET:
            field_dict["drip"] = drip
        if limited_options is not UNSET:
            field_dict["limitedOptions"] = limited_options

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        from ..models.account_configuration_type import AccountConfigurationType
        from ..models.account_rep import AccountRep
        from ..models.ach_instruction import ACHInstruction
        from ..models.advisor_wrap_fees_type import AdvisorWrapFeesType
        from ..models.commission_config import CommissionConfig
        from ..models.commission_schedule_type import CommissionScheduleType
        from ..models.custodian_type import CustodianType
        from ..models.deposit_notification import DepositNotification
        from ..models.dvp_instruction import DVPInstruction
        from ..models.exchange_access import ExchangeAccess
        from ..models.ext_positions_transfer_type import ExtPositionsTransferType
        from ..models.interest_markup_type import InterestMarkupType
        from ..models.ira_beneficiaries_type import IRABeneficiariesType
        from ..models.ira_decedent import IRADecedent
        from ..models.recurring_transaction import RecurringTransaction
        from ..models.trading_limits import TradingLimits
        from ..models.trading_permission import TradingPermission

        d = src_dict.copy()
        _account_configuration = d.pop("accountConfiguration", UNSET)
        account_configuration: Union[Unset, AccountConfigurationType]
        if isinstance(_account_configuration, Unset):
            account_configuration = UNSET
        else:
            account_configuration = AccountConfigurationType.from_dict(_account_configuration)

        investment_objectives = []
        _investment_objectives = d.pop("investmentObjectives", UNSET)
        for investment_objectives_item_data in _investment_objectives or []:
            investment_objectives_item = AccountInvestmentObjectivesItem(investment_objectives_item_data)

            investment_objectives.append(investment_objectives_item)

        brokerage_service_codes = []
        _brokerage_service_codes = d.pop("brokerageServiceCodes", UNSET)
        for brokerage_service_codes_item_data in _brokerage_service_codes or []:
            brokerage_service_codes_item = AccountBrokerageServiceCodesItem(brokerage_service_codes_item_data)

            brokerage_service_codes.append(brokerage_service_codes_item)

        capabilities = []
        _capabilities = d.pop("capabilities", UNSET)
        for capabilities_item_data in _capabilities or []:
            capabilities_item = AccountCapabilitiesItem(capabilities_item_data)

            capabilities.append(capabilities_item)

        trading_permissions = []
        _trading_permissions = d.pop("tradingPermissions", UNSET)
        for trading_permissions_item_data in _trading_permissions or []:
            trading_permissions_item = TradingPermission.from_dict(trading_permissions_item_data)

            trading_permissions.append(trading_permissions_item)

        commission_configs = []
        _commission_configs = d.pop("commissionConfigs", UNSET)
        for commission_configs_item_data in _commission_configs or []:
            commission_configs_item = CommissionConfig.from_dict(commission_configs_item_data)

            commission_configs.append(commission_configs_item)

        all_exchange_access = []
        _all_exchange_access = d.pop("allExchangeAccess", UNSET)
        for all_exchange_access_item_data in _all_exchange_access or []:
            all_exchange_access_item = ExchangeAccess.from_dict(all_exchange_access_item_data)

            all_exchange_access.append(all_exchange_access_item)

        dvp_instructions = []
        _dvp_instructions = d.pop("dvpInstructions", UNSET)
        for dvp_instructions_item_data in _dvp_instructions or []:
            dvp_instructions_item = DVPInstruction.from_dict(dvp_instructions_item_data)

            dvp_instructions.append(dvp_instructions_item)

        _trading_limits = d.pop("tradingLimits", UNSET)
        trading_limits: Union[Unset, TradingLimits]
        if isinstance(_trading_limits, Unset):
            trading_limits = UNSET
        else:
            trading_limits = TradingLimits.from_dict(_trading_limits)

        _advisor_wrap_fees = d.pop("advisorWrapFees", UNSET)
        advisor_wrap_fees: Union[Unset, AdvisorWrapFeesType]
        if isinstance(_advisor_wrap_fees, Unset):
            advisor_wrap_fees = UNSET
        else:
            advisor_wrap_fees = AdvisorWrapFeesType.from_dict(_advisor_wrap_fees)

        fees_template_name = d.pop("feesTemplateName", UNSET)

        _client_commission_schedule = d.pop("clientCommissionSchedule", UNSET)
        client_commission_schedule: Union[Unset, CommissionScheduleType]
        if isinstance(_client_commission_schedule, Unset):
            client_commission_schedule = UNSET
        else:
            client_commission_schedule = CommissionScheduleType.from_dict(_client_commission_schedule)

        client_interest_markup_schedules = []
        _client_interest_markup_schedules = d.pop("clientInterestMarkupSchedules", UNSET)
        for client_interest_markup_schedules_item_data in _client_interest_markup_schedules or []:
            client_interest_markup_schedules_item = InterestMarkupType.from_dict(
                client_interest_markup_schedules_item_data
            )

            client_interest_markup_schedules.append(client_interest_markup_schedules_item)

        _decendent = d.pop("decendent", UNSET)
        decendent: Union[Unset, IRADecedent]
        if isinstance(_decendent, Unset):
            decendent = UNSET
        else:
            decendent = IRADecedent.from_dict(_decendent)

        _ira_beneficiaries = d.pop("iraBeneficiaries", UNSET)
        ira_beneficiaries: Union[Unset, IRABeneficiariesType]
        if isinstance(_ira_beneficiaries, Unset):
            ira_beneficiaries = UNSET
        else:
            ira_beneficiaries = IRABeneficiariesType.from_dict(_ira_beneficiaries)

        ext_positions_transfers = []
        _ext_positions_transfers = d.pop("extPositionsTransfers", UNSET)
        for ext_positions_transfers_item_data in _ext_positions_transfers or []:
            ext_positions_transfers_item = ExtPositionsTransferType.from_dict(ext_positions_transfers_item_data)

            ext_positions_transfers.append(ext_positions_transfers_item)

        _deposit_notification = d.pop("depositNotification", UNSET)
        deposit_notification: Union[Unset, DepositNotification]
        if isinstance(_deposit_notification, Unset):
            deposit_notification = UNSET
        else:
            deposit_notification = DepositNotification.from_dict(_deposit_notification)

        ach_instructions = []
        _ach_instructions = d.pop("achInstructions", UNSET)
        for ach_instructions_item_data in _ach_instructions or []:
            ach_instructions_item = ACHInstruction.from_dict(ach_instructions_item_data)

            ach_instructions.append(ach_instructions_item)

        recurring_transactions = []
        _recurring_transactions = d.pop("recurringTransactions", UNSET)
        for recurring_transactions_item_data in _recurring_transactions or []:
            recurring_transactions_item = RecurringTransaction.from_dict(recurring_transactions_item_data)

            recurring_transactions.append(recurring_transactions_item)

        _custodian = d.pop("custodian", UNSET)
        custodian: Union[Unset, CustodianType]
        if isinstance(_custodian, Unset):
            custodian = UNSET
        else:
            custodian = CustodianType.from_dict(_custodian)

        _successor_custodian = d.pop("successorCustodian", UNSET)
        successor_custodian: Union[Unset, CustodianType]
        if isinstance(_successor_custodian, Unset):
            successor_custodian = UNSET
        else:
            successor_custodian = CustodianType.from_dict(_successor_custodian)

        _account_rep = d.pop("accountRep", UNSET)
        account_rep: Union[Unset, AccountRep]
        if isinstance(_account_rep, Unset):
            account_rep = UNSET
        else:
            account_rep = AccountRep.from_dict(_account_rep)

        id = d.pop("id", UNSET)

        external_id = d.pop("externalId", UNSET)

        property_profile = d.pop("propertyProfile", UNSET)

        _base_currency = d.pop("baseCurrency", UNSET)
        base_currency: Union[Unset, AccountBaseCurrency]
        if isinstance(_base_currency, Unset):
            base_currency = UNSET
        else:
            base_currency = AccountBaseCurrency(_base_currency)

        employee_plan = d.pop("employeePlan", UNSET)

        multi_currency = d.pop("multiCurrency", UNSET)

        migration = d.pop("migration", UNSET)

        source_account_id = d.pop("sourceAccountId", UNSET)

        margin = d.pop("margin", UNSET)

        ira = d.pop("ira", UNSET)

        _ira_type = d.pop("iraType", UNSET)
        ira_type: Union[Unset, AccountIraType]
        if isinstance(_ira_type, Unset):
            ira_type = UNSET
        else:
            ira_type = AccountIraType(_ira_type)

        ira_official_title = d.pop("iraOfficialTitle", UNSET)

        client_active_trading = d.pop("clientActiveTrading", UNSET)

        duplicate = d.pop("duplicate", UNSET)

        number_of_duplicates = d.pop("numberOfDuplicates", UNSET)

        stock_yield_program = d.pop("stockYieldProgram", UNSET)

        alias = d.pop("alias", UNSET)

        _account_type = d.pop("accountType", UNSET)
        account_type: Union[Unset, AccountAccountType]
        if isinstance(_account_type, Unset):
            account_type = UNSET
        else:
            account_type = AccountAccountType(_account_type)

        drip = d.pop("drip", UNSET)

        limited_options = d.pop("limitedOptions", UNSET)

        account = cls(
            account_configuration=account_configuration,
            investment_objectives=investment_objectives,
            brokerage_service_codes=brokerage_service_codes,
            capabilities=capabilities,
            trading_permissions=trading_permissions,
            commission_configs=commission_configs,
            all_exchange_access=all_exchange_access,
            dvp_instructions=dvp_instructions,
            trading_limits=trading_limits,
            advisor_wrap_fees=advisor_wrap_fees,
            fees_template_name=fees_template_name,
            client_commission_schedule=client_commission_schedule,
            client_interest_markup_schedules=client_interest_markup_schedules,
            decendent=decendent,
            ira_beneficiaries=ira_beneficiaries,
            ext_positions_transfers=ext_positions_transfers,
            deposit_notification=deposit_notification,
            ach_instructions=ach_instructions,
            recurring_transactions=recurring_transactions,
            custodian=custodian,
            successor_custodian=successor_custodian,
            account_rep=account_rep,
            id=id,
            external_id=external_id,
            property_profile=property_profile,
            base_currency=base_currency,
            employee_plan=employee_plan,
            multi_currency=multi_currency,
            migration=migration,
            source_account_id=source_account_id,
            margin=margin,
            ira=ira,
            ira_type=ira_type,
            ira_official_title=ira_official_title,
            client_active_trading=client_active_trading,
            duplicate=duplicate,
            number_of_duplicates=number_of_duplicates,
            stock_yield_program=stock_yield_program,
            alias=alias,
            account_type=account_type,
            drip=drip,
            limited_options=limited_options,
        )

        account.additional_properties = d
        return account

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
