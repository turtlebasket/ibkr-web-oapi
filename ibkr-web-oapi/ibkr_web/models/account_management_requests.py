from typing import TYPE_CHECKING, Any, Dict, List, Type, TypeVar, Union

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.abandon_account import AbandonAccount
    from ..models.account_configuration import AccountConfiguration
    from ..models.accredited_investor import AccreditedInvestor
    from ..models.ach_instruction import ACHInstruction
    from ..models.add_additional_account import AddAdditionalAccount
    from ..models.add_clp_capability import AddCLPCapability
    from ..models.add_levfx_capability import AddLEVFXCapability
    from ..models.add_mi_fir_data import AddMiFIRData
    from ..models.add_new_user import AddNewUser
    from ..models.add_trading_permissions import AddTradingPermissions
    from ..models.allocate_van import AllocateVAN
    from ..models.change_account_holder_detail import ChangeAccountHolderDetail
    from ..models.change_base_currency import ChangeBaseCurrency
    from ..models.change_financial_information import ChangeFinancialInformation
    from ..models.change_margin_type import ChangeMarginType
    from ..models.complete_login_message import CompleteLoginMessage
    from ..models.create_user import CreateUser
    from ..models.create_user_for_second_holder import CreateUserForSecondHolder
    from ..models.deposit_notification import DepositNotification
    from ..models.disable_account_in_brokerage import DisableAccountInBrokerage
    from ..models.document_submission import DocumentSubmission
    from ..models.duplicate_account import DuplicateAccount
    from ..models.enable_account_in_brokerage import EnableAccountInBrokerage
    from ..models.enroll_in_drip import EnrollInDRIP
    from ..models.enroll_in_syep import EnrollInSYEP
    from ..models.get_java_script import GetJavaScript
    from ..models.information_change import InformationChange
    from ..models.leave_drip import LeaveDRIP
    from ..models.leave_syep import LeaveSYEP
    from ..models.link_duplicate_account import LinkDuplicateAccount
    from ..models.process_documents import ProcessDocuments
    from ..models.prohibited_country_questionnaire import ProhibitedCountryQuestionnaire
    from ..models.questionnaires import Questionnaires
    from ..models.recurring_transaction import RecurringTransaction
    from ..models.remove_trading_permissions import RemoveTradingPermissions
    from ..models.reopen_account import ReopenAccount
    from ..models.reset_abandoned_account import ResetAbandonedAccount
    from ..models.security_questions import SecurityQuestions
    from ..models.update_account_alias import UpdateAccountAlias
    from ..models.update_account_representatives import UpdateAccountRepresentatives
    from ..models.update_bcan import UpdateBCAN
    from ..models.update_credentials import UpdateCredentials
    from ..models.update_external_id import UpdateExternalId
    from ..models.update_property_profile import UpdatePropertyProfile
    from ..models.update_tax_form import UpdateTaxForm
    from ..models.update_user_access_rights import UpdateUserAccessRights
    from ..models.update_w8ben import UpdateW8BEN
    from ..models.update_withholding_statement import UpdateWithholdingStatement
    from ..models.yodlee_session import YodleeSession


T = TypeVar("T", bound="AccountManagementRequests")


@_attrs_define
class AccountManagementRequests:
    """
    Attributes:
        update_external_id (Union[Unset, UpdateExternalId]):
        update_property_profile (Union[Unset, UpdatePropertyProfile]):
        update_account_alias (Union[Unset, UpdateAccountAlias]):
        change_base_currency (Union[Unset, ChangeBaseCurrency]):
        abandon_account (Union[Unset, AbandonAccount]):
        add_new_user (Union[Unset, AddNewUser]):
        add_lev_fx_capability (Union[Unset, AddLEVFXCapability]):
        add_mi_fir_data (Union[Unset, AddMiFIRData]):
        add_trading_permissions (Union[Unset, AddTradingPermissions]):
        remove_trading_permissions (Union[Unset, RemoveTradingPermissions]):
        change_margin_type (Union[Unset, ChangeMarginType]):
        add_clp_capability (Union[Unset, AddCLPCapability]):
        change_financial_information (Union[Unset, ChangeFinancialInformation]):
        reset_abandoned_account (Union[Unset, ResetAbandonedAccount]):
        update_credentials (Union[Unset, UpdateCredentials]):
        update_account_representatives (Union[Unset, UpdateAccountRepresentatives]):
        complete_login_message (Union[Unset, CompleteLoginMessage]):
        reopen_account (Union[Unset, ReopenAccount]):
        enroll_in_syep (Union[Unset, EnrollInSYEP]):
        leave_syep (Union[Unset, LeaveSYEP]):
        enroll_in_drip (Union[Unset, EnrollInDRIP]):
        leave_drip (Union[Unset, LeaveDRIP]):
        update_w8_ben (Union[Unset, UpdateW8BEN]):
        yodlee_session (Union[Unset, YodleeSession]):
        enable_account_in_brokerage (Union[Unset, EnableAccountInBrokerage]):
        disable_account_in_brokerage (Union[Unset, DisableAccountInBrokerage]):
        link_duplicate_account (Union[Unset, LinkDuplicateAccount]):
        duplicate_account (Union[Unset, DuplicateAccount]):
        ach_instruction (Union[Unset, ACHInstruction]):
        recurring_transaction (Union[Unset, RecurringTransaction]):
        deposit_notification (Union[Unset, DepositNotification]):
        document_submission (Union[Unset, DocumentSubmission]):
        process_documents (Union[Unset, ProcessDocuments]):
        update_bcan (Union[Unset, UpdateBCAN]):
        prohibited_country_questionnaire (Union[Unset, ProhibitedCountryQuestionnaire]):
        update_withholding_statement (Union[Unset, UpdateWithholdingStatement]):
        accredited_investor (Union[Unset, AccreditedInvestor]):
        change_account_holder_detail (Union[Unset, ChangeAccountHolderDetail]):
        get_java_script (Union[Unset, GetJavaScript]):
        update_user_access_rights (Union[Unset, UpdateUserAccessRights]):
        information_change (Union[Unset, InformationChange]):
        add_additional_account (Union[Unset, AddAdditionalAccount]):
        account_configuration (Union[Unset, AccountConfiguration]):
        allocate_van (Union[Unset, AllocateVAN]):
        create_user_for_second_holder (Union[Unset, CreateUserForSecondHolder]):
        create_user (Union[Unset, CreateUser]):
        update_tax_form (Union[Unset, UpdateTaxForm]):
        questionnaires (Union[Unset, Questionnaires]):
        security_questions (Union[Unset, SecurityQuestions]):
    """

    update_external_id: Union[Unset, "UpdateExternalId"] = UNSET
    update_property_profile: Union[Unset, "UpdatePropertyProfile"] = UNSET
    update_account_alias: Union[Unset, "UpdateAccountAlias"] = UNSET
    change_base_currency: Union[Unset, "ChangeBaseCurrency"] = UNSET
    abandon_account: Union[Unset, "AbandonAccount"] = UNSET
    add_new_user: Union[Unset, "AddNewUser"] = UNSET
    add_lev_fx_capability: Union[Unset, "AddLEVFXCapability"] = UNSET
    add_mi_fir_data: Union[Unset, "AddMiFIRData"] = UNSET
    add_trading_permissions: Union[Unset, "AddTradingPermissions"] = UNSET
    remove_trading_permissions: Union[Unset, "RemoveTradingPermissions"] = UNSET
    change_margin_type: Union[Unset, "ChangeMarginType"] = UNSET
    add_clp_capability: Union[Unset, "AddCLPCapability"] = UNSET
    change_financial_information: Union[Unset, "ChangeFinancialInformation"] = UNSET
    reset_abandoned_account: Union[Unset, "ResetAbandonedAccount"] = UNSET
    update_credentials: Union[Unset, "UpdateCredentials"] = UNSET
    update_account_representatives: Union[Unset, "UpdateAccountRepresentatives"] = UNSET
    complete_login_message: Union[Unset, "CompleteLoginMessage"] = UNSET
    reopen_account: Union[Unset, "ReopenAccount"] = UNSET
    enroll_in_syep: Union[Unset, "EnrollInSYEP"] = UNSET
    leave_syep: Union[Unset, "LeaveSYEP"] = UNSET
    enroll_in_drip: Union[Unset, "EnrollInDRIP"] = UNSET
    leave_drip: Union[Unset, "LeaveDRIP"] = UNSET
    update_w8_ben: Union[Unset, "UpdateW8BEN"] = UNSET
    yodlee_session: Union[Unset, "YodleeSession"] = UNSET
    enable_account_in_brokerage: Union[Unset, "EnableAccountInBrokerage"] = UNSET
    disable_account_in_brokerage: Union[Unset, "DisableAccountInBrokerage"] = UNSET
    link_duplicate_account: Union[Unset, "LinkDuplicateAccount"] = UNSET
    duplicate_account: Union[Unset, "DuplicateAccount"] = UNSET
    ach_instruction: Union[Unset, "ACHInstruction"] = UNSET
    recurring_transaction: Union[Unset, "RecurringTransaction"] = UNSET
    deposit_notification: Union[Unset, "DepositNotification"] = UNSET
    document_submission: Union[Unset, "DocumentSubmission"] = UNSET
    process_documents: Union[Unset, "ProcessDocuments"] = UNSET
    update_bcan: Union[Unset, "UpdateBCAN"] = UNSET
    prohibited_country_questionnaire: Union[Unset, "ProhibitedCountryQuestionnaire"] = UNSET
    update_withholding_statement: Union[Unset, "UpdateWithholdingStatement"] = UNSET
    accredited_investor: Union[Unset, "AccreditedInvestor"] = UNSET
    change_account_holder_detail: Union[Unset, "ChangeAccountHolderDetail"] = UNSET
    get_java_script: Union[Unset, "GetJavaScript"] = UNSET
    update_user_access_rights: Union[Unset, "UpdateUserAccessRights"] = UNSET
    information_change: Union[Unset, "InformationChange"] = UNSET
    add_additional_account: Union[Unset, "AddAdditionalAccount"] = UNSET
    account_configuration: Union[Unset, "AccountConfiguration"] = UNSET
    allocate_van: Union[Unset, "AllocateVAN"] = UNSET
    create_user_for_second_holder: Union[Unset, "CreateUserForSecondHolder"] = UNSET
    create_user: Union[Unset, "CreateUser"] = UNSET
    update_tax_form: Union[Unset, "UpdateTaxForm"] = UNSET
    questionnaires: Union[Unset, "Questionnaires"] = UNSET
    security_questions: Union[Unset, "SecurityQuestions"] = UNSET
    additional_properties: Dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> Dict[str, Any]:
        update_external_id: Union[Unset, Dict[str, Any]] = UNSET
        if not isinstance(self.update_external_id, Unset):
            update_external_id = self.update_external_id.to_dict()

        update_property_profile: Union[Unset, Dict[str, Any]] = UNSET
        if not isinstance(self.update_property_profile, Unset):
            update_property_profile = self.update_property_profile.to_dict()

        update_account_alias: Union[Unset, Dict[str, Any]] = UNSET
        if not isinstance(self.update_account_alias, Unset):
            update_account_alias = self.update_account_alias.to_dict()

        change_base_currency: Union[Unset, Dict[str, Any]] = UNSET
        if not isinstance(self.change_base_currency, Unset):
            change_base_currency = self.change_base_currency.to_dict()

        abandon_account: Union[Unset, Dict[str, Any]] = UNSET
        if not isinstance(self.abandon_account, Unset):
            abandon_account = self.abandon_account.to_dict()

        add_new_user: Union[Unset, Dict[str, Any]] = UNSET
        if not isinstance(self.add_new_user, Unset):
            add_new_user = self.add_new_user.to_dict()

        add_lev_fx_capability: Union[Unset, Dict[str, Any]] = UNSET
        if not isinstance(self.add_lev_fx_capability, Unset):
            add_lev_fx_capability = self.add_lev_fx_capability.to_dict()

        add_mi_fir_data: Union[Unset, Dict[str, Any]] = UNSET
        if not isinstance(self.add_mi_fir_data, Unset):
            add_mi_fir_data = self.add_mi_fir_data.to_dict()

        add_trading_permissions: Union[Unset, Dict[str, Any]] = UNSET
        if not isinstance(self.add_trading_permissions, Unset):
            add_trading_permissions = self.add_trading_permissions.to_dict()

        remove_trading_permissions: Union[Unset, Dict[str, Any]] = UNSET
        if not isinstance(self.remove_trading_permissions, Unset):
            remove_trading_permissions = self.remove_trading_permissions.to_dict()

        change_margin_type: Union[Unset, Dict[str, Any]] = UNSET
        if not isinstance(self.change_margin_type, Unset):
            change_margin_type = self.change_margin_type.to_dict()

        add_clp_capability: Union[Unset, Dict[str, Any]] = UNSET
        if not isinstance(self.add_clp_capability, Unset):
            add_clp_capability = self.add_clp_capability.to_dict()

        change_financial_information: Union[Unset, Dict[str, Any]] = UNSET
        if not isinstance(self.change_financial_information, Unset):
            change_financial_information = self.change_financial_information.to_dict()

        reset_abandoned_account: Union[Unset, Dict[str, Any]] = UNSET
        if not isinstance(self.reset_abandoned_account, Unset):
            reset_abandoned_account = self.reset_abandoned_account.to_dict()

        update_credentials: Union[Unset, Dict[str, Any]] = UNSET
        if not isinstance(self.update_credentials, Unset):
            update_credentials = self.update_credentials.to_dict()

        update_account_representatives: Union[Unset, Dict[str, Any]] = UNSET
        if not isinstance(self.update_account_representatives, Unset):
            update_account_representatives = self.update_account_representatives.to_dict()

        complete_login_message: Union[Unset, Dict[str, Any]] = UNSET
        if not isinstance(self.complete_login_message, Unset):
            complete_login_message = self.complete_login_message.to_dict()

        reopen_account: Union[Unset, Dict[str, Any]] = UNSET
        if not isinstance(self.reopen_account, Unset):
            reopen_account = self.reopen_account.to_dict()

        enroll_in_syep: Union[Unset, Dict[str, Any]] = UNSET
        if not isinstance(self.enroll_in_syep, Unset):
            enroll_in_syep = self.enroll_in_syep.to_dict()

        leave_syep: Union[Unset, Dict[str, Any]] = UNSET
        if not isinstance(self.leave_syep, Unset):
            leave_syep = self.leave_syep.to_dict()

        enroll_in_drip: Union[Unset, Dict[str, Any]] = UNSET
        if not isinstance(self.enroll_in_drip, Unset):
            enroll_in_drip = self.enroll_in_drip.to_dict()

        leave_drip: Union[Unset, Dict[str, Any]] = UNSET
        if not isinstance(self.leave_drip, Unset):
            leave_drip = self.leave_drip.to_dict()

        update_w8_ben: Union[Unset, Dict[str, Any]] = UNSET
        if not isinstance(self.update_w8_ben, Unset):
            update_w8_ben = self.update_w8_ben.to_dict()

        yodlee_session: Union[Unset, Dict[str, Any]] = UNSET
        if not isinstance(self.yodlee_session, Unset):
            yodlee_session = self.yodlee_session.to_dict()

        enable_account_in_brokerage: Union[Unset, Dict[str, Any]] = UNSET
        if not isinstance(self.enable_account_in_brokerage, Unset):
            enable_account_in_brokerage = self.enable_account_in_brokerage.to_dict()

        disable_account_in_brokerage: Union[Unset, Dict[str, Any]] = UNSET
        if not isinstance(self.disable_account_in_brokerage, Unset):
            disable_account_in_brokerage = self.disable_account_in_brokerage.to_dict()

        link_duplicate_account: Union[Unset, Dict[str, Any]] = UNSET
        if not isinstance(self.link_duplicate_account, Unset):
            link_duplicate_account = self.link_duplicate_account.to_dict()

        duplicate_account: Union[Unset, Dict[str, Any]] = UNSET
        if not isinstance(self.duplicate_account, Unset):
            duplicate_account = self.duplicate_account.to_dict()

        ach_instruction: Union[Unset, Dict[str, Any]] = UNSET
        if not isinstance(self.ach_instruction, Unset):
            ach_instruction = self.ach_instruction.to_dict()

        recurring_transaction: Union[Unset, Dict[str, Any]] = UNSET
        if not isinstance(self.recurring_transaction, Unset):
            recurring_transaction = self.recurring_transaction.to_dict()

        deposit_notification: Union[Unset, Dict[str, Any]] = UNSET
        if not isinstance(self.deposit_notification, Unset):
            deposit_notification = self.deposit_notification.to_dict()

        document_submission: Union[Unset, Dict[str, Any]] = UNSET
        if not isinstance(self.document_submission, Unset):
            document_submission = self.document_submission.to_dict()

        process_documents: Union[Unset, Dict[str, Any]] = UNSET
        if not isinstance(self.process_documents, Unset):
            process_documents = self.process_documents.to_dict()

        update_bcan: Union[Unset, Dict[str, Any]] = UNSET
        if not isinstance(self.update_bcan, Unset):
            update_bcan = self.update_bcan.to_dict()

        prohibited_country_questionnaire: Union[Unset, Dict[str, Any]] = UNSET
        if not isinstance(self.prohibited_country_questionnaire, Unset):
            prohibited_country_questionnaire = self.prohibited_country_questionnaire.to_dict()

        update_withholding_statement: Union[Unset, Dict[str, Any]] = UNSET
        if not isinstance(self.update_withholding_statement, Unset):
            update_withholding_statement = self.update_withholding_statement.to_dict()

        accredited_investor: Union[Unset, Dict[str, Any]] = UNSET
        if not isinstance(self.accredited_investor, Unset):
            accredited_investor = self.accredited_investor.to_dict()

        change_account_holder_detail: Union[Unset, Dict[str, Any]] = UNSET
        if not isinstance(self.change_account_holder_detail, Unset):
            change_account_holder_detail = self.change_account_holder_detail.to_dict()

        get_java_script: Union[Unset, Dict[str, Any]] = UNSET
        if not isinstance(self.get_java_script, Unset):
            get_java_script = self.get_java_script.to_dict()

        update_user_access_rights: Union[Unset, Dict[str, Any]] = UNSET
        if not isinstance(self.update_user_access_rights, Unset):
            update_user_access_rights = self.update_user_access_rights.to_dict()

        information_change: Union[Unset, Dict[str, Any]] = UNSET
        if not isinstance(self.information_change, Unset):
            information_change = self.information_change.to_dict()

        add_additional_account: Union[Unset, Dict[str, Any]] = UNSET
        if not isinstance(self.add_additional_account, Unset):
            add_additional_account = self.add_additional_account.to_dict()

        account_configuration: Union[Unset, Dict[str, Any]] = UNSET
        if not isinstance(self.account_configuration, Unset):
            account_configuration = self.account_configuration.to_dict()

        allocate_van: Union[Unset, Dict[str, Any]] = UNSET
        if not isinstance(self.allocate_van, Unset):
            allocate_van = self.allocate_van.to_dict()

        create_user_for_second_holder: Union[Unset, Dict[str, Any]] = UNSET
        if not isinstance(self.create_user_for_second_holder, Unset):
            create_user_for_second_holder = self.create_user_for_second_holder.to_dict()

        create_user: Union[Unset, Dict[str, Any]] = UNSET
        if not isinstance(self.create_user, Unset):
            create_user = self.create_user.to_dict()

        update_tax_form: Union[Unset, Dict[str, Any]] = UNSET
        if not isinstance(self.update_tax_form, Unset):
            update_tax_form = self.update_tax_form.to_dict()

        questionnaires: Union[Unset, Dict[str, Any]] = UNSET
        if not isinstance(self.questionnaires, Unset):
            questionnaires = self.questionnaires.to_dict()

        security_questions: Union[Unset, Dict[str, Any]] = UNSET
        if not isinstance(self.security_questions, Unset):
            security_questions = self.security_questions.to_dict()

        field_dict: Dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if update_external_id is not UNSET:
            field_dict["updateExternalId"] = update_external_id
        if update_property_profile is not UNSET:
            field_dict["updatePropertyProfile"] = update_property_profile
        if update_account_alias is not UNSET:
            field_dict["updateAccountAlias"] = update_account_alias
        if change_base_currency is not UNSET:
            field_dict["changeBaseCurrency"] = change_base_currency
        if abandon_account is not UNSET:
            field_dict["abandonAccount"] = abandon_account
        if add_new_user is not UNSET:
            field_dict["addNewUser"] = add_new_user
        if add_lev_fx_capability is not UNSET:
            field_dict["addLevFxCapability"] = add_lev_fx_capability
        if add_mi_fir_data is not UNSET:
            field_dict["addMiFirData"] = add_mi_fir_data
        if add_trading_permissions is not UNSET:
            field_dict["addTradingPermissions"] = add_trading_permissions
        if remove_trading_permissions is not UNSET:
            field_dict["removeTradingPermissions"] = remove_trading_permissions
        if change_margin_type is not UNSET:
            field_dict["changeMarginType"] = change_margin_type
        if add_clp_capability is not UNSET:
            field_dict["addCLPCapability"] = add_clp_capability
        if change_financial_information is not UNSET:
            field_dict["changeFinancialInformation"] = change_financial_information
        if reset_abandoned_account is not UNSET:
            field_dict["resetAbandonedAccount"] = reset_abandoned_account
        if update_credentials is not UNSET:
            field_dict["updateCredentials"] = update_credentials
        if update_account_representatives is not UNSET:
            field_dict["updateAccountRepresentatives"] = update_account_representatives
        if complete_login_message is not UNSET:
            field_dict["completeLoginMessage"] = complete_login_message
        if reopen_account is not UNSET:
            field_dict["reopenAccount"] = reopen_account
        if enroll_in_syep is not UNSET:
            field_dict["enrollInSyep"] = enroll_in_syep
        if leave_syep is not UNSET:
            field_dict["leaveSyep"] = leave_syep
        if enroll_in_drip is not UNSET:
            field_dict["enrollInDrip"] = enroll_in_drip
        if leave_drip is not UNSET:
            field_dict["leaveDrip"] = leave_drip
        if update_w8_ben is not UNSET:
            field_dict["updateW8Ben"] = update_w8_ben
        if yodlee_session is not UNSET:
            field_dict["yodleeSession"] = yodlee_session
        if enable_account_in_brokerage is not UNSET:
            field_dict["enableAccountInBrokerage"] = enable_account_in_brokerage
        if disable_account_in_brokerage is not UNSET:
            field_dict["disableAccountInBrokerage"] = disable_account_in_brokerage
        if link_duplicate_account is not UNSET:
            field_dict["linkDuplicateAccount"] = link_duplicate_account
        if duplicate_account is not UNSET:
            field_dict["duplicateAccount"] = duplicate_account
        if ach_instruction is not UNSET:
            field_dict["achInstruction"] = ach_instruction
        if recurring_transaction is not UNSET:
            field_dict["recurringTransaction"] = recurring_transaction
        if deposit_notification is not UNSET:
            field_dict["depositNotification"] = deposit_notification
        if document_submission is not UNSET:
            field_dict["documentSubmission"] = document_submission
        if process_documents is not UNSET:
            field_dict["processDocuments"] = process_documents
        if update_bcan is not UNSET:
            field_dict["updateBcan"] = update_bcan
        if prohibited_country_questionnaire is not UNSET:
            field_dict["prohibitedCountryQuestionnaire"] = prohibited_country_questionnaire
        if update_withholding_statement is not UNSET:
            field_dict["updateWithholdingStatement"] = update_withholding_statement
        if accredited_investor is not UNSET:
            field_dict["accreditedInvestor"] = accredited_investor
        if change_account_holder_detail is not UNSET:
            field_dict["changeAccountHolderDetail"] = change_account_holder_detail
        if get_java_script is not UNSET:
            field_dict["getJavaScript"] = get_java_script
        if update_user_access_rights is not UNSET:
            field_dict["updateUserAccessRights"] = update_user_access_rights
        if information_change is not UNSET:
            field_dict["informationChange"] = information_change
        if add_additional_account is not UNSET:
            field_dict["addAdditionalAccount"] = add_additional_account
        if account_configuration is not UNSET:
            field_dict["accountConfiguration"] = account_configuration
        if allocate_van is not UNSET:
            field_dict["allocateVan"] = allocate_van
        if create_user_for_second_holder is not UNSET:
            field_dict["createUserForSecondHolder"] = create_user_for_second_holder
        if create_user is not UNSET:
            field_dict["createUser"] = create_user
        if update_tax_form is not UNSET:
            field_dict["updateTaxForm"] = update_tax_form
        if questionnaires is not UNSET:
            field_dict["questionnaires"] = questionnaires
        if security_questions is not UNSET:
            field_dict["securityQuestions"] = security_questions

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        from ..models.abandon_account import AbandonAccount
        from ..models.account_configuration import AccountConfiguration
        from ..models.accredited_investor import AccreditedInvestor
        from ..models.ach_instruction import ACHInstruction
        from ..models.add_additional_account import AddAdditionalAccount
        from ..models.add_clp_capability import AddCLPCapability
        from ..models.add_levfx_capability import AddLEVFXCapability
        from ..models.add_mi_fir_data import AddMiFIRData
        from ..models.add_new_user import AddNewUser
        from ..models.add_trading_permissions import AddTradingPermissions
        from ..models.allocate_van import AllocateVAN
        from ..models.change_account_holder_detail import ChangeAccountHolderDetail
        from ..models.change_base_currency import ChangeBaseCurrency
        from ..models.change_financial_information import ChangeFinancialInformation
        from ..models.change_margin_type import ChangeMarginType
        from ..models.complete_login_message import CompleteLoginMessage
        from ..models.create_user import CreateUser
        from ..models.create_user_for_second_holder import CreateUserForSecondHolder
        from ..models.deposit_notification import DepositNotification
        from ..models.disable_account_in_brokerage import DisableAccountInBrokerage
        from ..models.document_submission import DocumentSubmission
        from ..models.duplicate_account import DuplicateAccount
        from ..models.enable_account_in_brokerage import EnableAccountInBrokerage
        from ..models.enroll_in_drip import EnrollInDRIP
        from ..models.enroll_in_syep import EnrollInSYEP
        from ..models.get_java_script import GetJavaScript
        from ..models.information_change import InformationChange
        from ..models.leave_drip import LeaveDRIP
        from ..models.leave_syep import LeaveSYEP
        from ..models.link_duplicate_account import LinkDuplicateAccount
        from ..models.process_documents import ProcessDocuments
        from ..models.prohibited_country_questionnaire import ProhibitedCountryQuestionnaire
        from ..models.questionnaires import Questionnaires
        from ..models.recurring_transaction import RecurringTransaction
        from ..models.remove_trading_permissions import RemoveTradingPermissions
        from ..models.reopen_account import ReopenAccount
        from ..models.reset_abandoned_account import ResetAbandonedAccount
        from ..models.security_questions import SecurityQuestions
        from ..models.update_account_alias import UpdateAccountAlias
        from ..models.update_account_representatives import UpdateAccountRepresentatives
        from ..models.update_bcan import UpdateBCAN
        from ..models.update_credentials import UpdateCredentials
        from ..models.update_external_id import UpdateExternalId
        from ..models.update_property_profile import UpdatePropertyProfile
        from ..models.update_tax_form import UpdateTaxForm
        from ..models.update_user_access_rights import UpdateUserAccessRights
        from ..models.update_w8ben import UpdateW8BEN
        from ..models.update_withholding_statement import UpdateWithholdingStatement
        from ..models.yodlee_session import YodleeSession

        d = src_dict.copy()
        _update_external_id = d.pop("updateExternalId", UNSET)
        update_external_id: Union[Unset, UpdateExternalId]
        if isinstance(_update_external_id, Unset):
            update_external_id = UNSET
        else:
            update_external_id = UpdateExternalId.from_dict(_update_external_id)

        _update_property_profile = d.pop("updatePropertyProfile", UNSET)
        update_property_profile: Union[Unset, UpdatePropertyProfile]
        if isinstance(_update_property_profile, Unset):
            update_property_profile = UNSET
        else:
            update_property_profile = UpdatePropertyProfile.from_dict(_update_property_profile)

        _update_account_alias = d.pop("updateAccountAlias", UNSET)
        update_account_alias: Union[Unset, UpdateAccountAlias]
        if isinstance(_update_account_alias, Unset):
            update_account_alias = UNSET
        else:
            update_account_alias = UpdateAccountAlias.from_dict(_update_account_alias)

        _change_base_currency = d.pop("changeBaseCurrency", UNSET)
        change_base_currency: Union[Unset, ChangeBaseCurrency]
        if isinstance(_change_base_currency, Unset):
            change_base_currency = UNSET
        else:
            change_base_currency = ChangeBaseCurrency.from_dict(_change_base_currency)

        _abandon_account = d.pop("abandonAccount", UNSET)
        abandon_account: Union[Unset, AbandonAccount]
        if isinstance(_abandon_account, Unset):
            abandon_account = UNSET
        else:
            abandon_account = AbandonAccount.from_dict(_abandon_account)

        _add_new_user = d.pop("addNewUser", UNSET)
        add_new_user: Union[Unset, AddNewUser]
        if isinstance(_add_new_user, Unset):
            add_new_user = UNSET
        else:
            add_new_user = AddNewUser.from_dict(_add_new_user)

        _add_lev_fx_capability = d.pop("addLevFxCapability", UNSET)
        add_lev_fx_capability: Union[Unset, AddLEVFXCapability]
        if isinstance(_add_lev_fx_capability, Unset):
            add_lev_fx_capability = UNSET
        else:
            add_lev_fx_capability = AddLEVFXCapability.from_dict(_add_lev_fx_capability)

        _add_mi_fir_data = d.pop("addMiFirData", UNSET)
        add_mi_fir_data: Union[Unset, AddMiFIRData]
        if isinstance(_add_mi_fir_data, Unset):
            add_mi_fir_data = UNSET
        else:
            add_mi_fir_data = AddMiFIRData.from_dict(_add_mi_fir_data)

        _add_trading_permissions = d.pop("addTradingPermissions", UNSET)
        add_trading_permissions: Union[Unset, AddTradingPermissions]
        if isinstance(_add_trading_permissions, Unset):
            add_trading_permissions = UNSET
        else:
            add_trading_permissions = AddTradingPermissions.from_dict(_add_trading_permissions)

        _remove_trading_permissions = d.pop("removeTradingPermissions", UNSET)
        remove_trading_permissions: Union[Unset, RemoveTradingPermissions]
        if isinstance(_remove_trading_permissions, Unset):
            remove_trading_permissions = UNSET
        else:
            remove_trading_permissions = RemoveTradingPermissions.from_dict(_remove_trading_permissions)

        _change_margin_type = d.pop("changeMarginType", UNSET)
        change_margin_type: Union[Unset, ChangeMarginType]
        if isinstance(_change_margin_type, Unset):
            change_margin_type = UNSET
        else:
            change_margin_type = ChangeMarginType.from_dict(_change_margin_type)

        _add_clp_capability = d.pop("addCLPCapability", UNSET)
        add_clp_capability: Union[Unset, AddCLPCapability]
        if isinstance(_add_clp_capability, Unset):
            add_clp_capability = UNSET
        else:
            add_clp_capability = AddCLPCapability.from_dict(_add_clp_capability)

        _change_financial_information = d.pop("changeFinancialInformation", UNSET)
        change_financial_information: Union[Unset, ChangeFinancialInformation]
        if isinstance(_change_financial_information, Unset):
            change_financial_information = UNSET
        else:
            change_financial_information = ChangeFinancialInformation.from_dict(_change_financial_information)

        _reset_abandoned_account = d.pop("resetAbandonedAccount", UNSET)
        reset_abandoned_account: Union[Unset, ResetAbandonedAccount]
        if isinstance(_reset_abandoned_account, Unset):
            reset_abandoned_account = UNSET
        else:
            reset_abandoned_account = ResetAbandonedAccount.from_dict(_reset_abandoned_account)

        _update_credentials = d.pop("updateCredentials", UNSET)
        update_credentials: Union[Unset, UpdateCredentials]
        if isinstance(_update_credentials, Unset):
            update_credentials = UNSET
        else:
            update_credentials = UpdateCredentials.from_dict(_update_credentials)

        _update_account_representatives = d.pop("updateAccountRepresentatives", UNSET)
        update_account_representatives: Union[Unset, UpdateAccountRepresentatives]
        if isinstance(_update_account_representatives, Unset):
            update_account_representatives = UNSET
        else:
            update_account_representatives = UpdateAccountRepresentatives.from_dict(_update_account_representatives)

        _complete_login_message = d.pop("completeLoginMessage", UNSET)
        complete_login_message: Union[Unset, CompleteLoginMessage]
        if isinstance(_complete_login_message, Unset):
            complete_login_message = UNSET
        else:
            complete_login_message = CompleteLoginMessage.from_dict(_complete_login_message)

        _reopen_account = d.pop("reopenAccount", UNSET)
        reopen_account: Union[Unset, ReopenAccount]
        if isinstance(_reopen_account, Unset):
            reopen_account = UNSET
        else:
            reopen_account = ReopenAccount.from_dict(_reopen_account)

        _enroll_in_syep = d.pop("enrollInSyep", UNSET)
        enroll_in_syep: Union[Unset, EnrollInSYEP]
        if isinstance(_enroll_in_syep, Unset):
            enroll_in_syep = UNSET
        else:
            enroll_in_syep = EnrollInSYEP.from_dict(_enroll_in_syep)

        _leave_syep = d.pop("leaveSyep", UNSET)
        leave_syep: Union[Unset, LeaveSYEP]
        if isinstance(_leave_syep, Unset):
            leave_syep = UNSET
        else:
            leave_syep = LeaveSYEP.from_dict(_leave_syep)

        _enroll_in_drip = d.pop("enrollInDrip", UNSET)
        enroll_in_drip: Union[Unset, EnrollInDRIP]
        if isinstance(_enroll_in_drip, Unset):
            enroll_in_drip = UNSET
        else:
            enroll_in_drip = EnrollInDRIP.from_dict(_enroll_in_drip)

        _leave_drip = d.pop("leaveDrip", UNSET)
        leave_drip: Union[Unset, LeaveDRIP]
        if isinstance(_leave_drip, Unset):
            leave_drip = UNSET
        else:
            leave_drip = LeaveDRIP.from_dict(_leave_drip)

        _update_w8_ben = d.pop("updateW8Ben", UNSET)
        update_w8_ben: Union[Unset, UpdateW8BEN]
        if isinstance(_update_w8_ben, Unset):
            update_w8_ben = UNSET
        else:
            update_w8_ben = UpdateW8BEN.from_dict(_update_w8_ben)

        _yodlee_session = d.pop("yodleeSession", UNSET)
        yodlee_session: Union[Unset, YodleeSession]
        if isinstance(_yodlee_session, Unset):
            yodlee_session = UNSET
        else:
            yodlee_session = YodleeSession.from_dict(_yodlee_session)

        _enable_account_in_brokerage = d.pop("enableAccountInBrokerage", UNSET)
        enable_account_in_brokerage: Union[Unset, EnableAccountInBrokerage]
        if isinstance(_enable_account_in_brokerage, Unset):
            enable_account_in_brokerage = UNSET
        else:
            enable_account_in_brokerage = EnableAccountInBrokerage.from_dict(_enable_account_in_brokerage)

        _disable_account_in_brokerage = d.pop("disableAccountInBrokerage", UNSET)
        disable_account_in_brokerage: Union[Unset, DisableAccountInBrokerage]
        if isinstance(_disable_account_in_brokerage, Unset):
            disable_account_in_brokerage = UNSET
        else:
            disable_account_in_brokerage = DisableAccountInBrokerage.from_dict(_disable_account_in_brokerage)

        _link_duplicate_account = d.pop("linkDuplicateAccount", UNSET)
        link_duplicate_account: Union[Unset, LinkDuplicateAccount]
        if isinstance(_link_duplicate_account, Unset):
            link_duplicate_account = UNSET
        else:
            link_duplicate_account = LinkDuplicateAccount.from_dict(_link_duplicate_account)

        _duplicate_account = d.pop("duplicateAccount", UNSET)
        duplicate_account: Union[Unset, DuplicateAccount]
        if isinstance(_duplicate_account, Unset):
            duplicate_account = UNSET
        else:
            duplicate_account = DuplicateAccount.from_dict(_duplicate_account)

        _ach_instruction = d.pop("achInstruction", UNSET)
        ach_instruction: Union[Unset, ACHInstruction]
        if isinstance(_ach_instruction, Unset):
            ach_instruction = UNSET
        else:
            ach_instruction = ACHInstruction.from_dict(_ach_instruction)

        _recurring_transaction = d.pop("recurringTransaction", UNSET)
        recurring_transaction: Union[Unset, RecurringTransaction]
        if isinstance(_recurring_transaction, Unset):
            recurring_transaction = UNSET
        else:
            recurring_transaction = RecurringTransaction.from_dict(_recurring_transaction)

        _deposit_notification = d.pop("depositNotification", UNSET)
        deposit_notification: Union[Unset, DepositNotification]
        if isinstance(_deposit_notification, Unset):
            deposit_notification = UNSET
        else:
            deposit_notification = DepositNotification.from_dict(_deposit_notification)

        _document_submission = d.pop("documentSubmission", UNSET)
        document_submission: Union[Unset, DocumentSubmission]
        if isinstance(_document_submission, Unset):
            document_submission = UNSET
        else:
            document_submission = DocumentSubmission.from_dict(_document_submission)

        _process_documents = d.pop("processDocuments", UNSET)
        process_documents: Union[Unset, ProcessDocuments]
        if isinstance(_process_documents, Unset):
            process_documents = UNSET
        else:
            process_documents = ProcessDocuments.from_dict(_process_documents)

        _update_bcan = d.pop("updateBcan", UNSET)
        update_bcan: Union[Unset, UpdateBCAN]
        if isinstance(_update_bcan, Unset):
            update_bcan = UNSET
        else:
            update_bcan = UpdateBCAN.from_dict(_update_bcan)

        _prohibited_country_questionnaire = d.pop("prohibitedCountryQuestionnaire", UNSET)
        prohibited_country_questionnaire: Union[Unset, ProhibitedCountryQuestionnaire]
        if isinstance(_prohibited_country_questionnaire, Unset):
            prohibited_country_questionnaire = UNSET
        else:
            prohibited_country_questionnaire = ProhibitedCountryQuestionnaire.from_dict(
                _prohibited_country_questionnaire
            )

        _update_withholding_statement = d.pop("updateWithholdingStatement", UNSET)
        update_withholding_statement: Union[Unset, UpdateWithholdingStatement]
        if isinstance(_update_withholding_statement, Unset):
            update_withholding_statement = UNSET
        else:
            update_withholding_statement = UpdateWithholdingStatement.from_dict(_update_withholding_statement)

        _accredited_investor = d.pop("accreditedInvestor", UNSET)
        accredited_investor: Union[Unset, AccreditedInvestor]
        if isinstance(_accredited_investor, Unset):
            accredited_investor = UNSET
        else:
            accredited_investor = AccreditedInvestor.from_dict(_accredited_investor)

        _change_account_holder_detail = d.pop("changeAccountHolderDetail", UNSET)
        change_account_holder_detail: Union[Unset, ChangeAccountHolderDetail]
        if isinstance(_change_account_holder_detail, Unset):
            change_account_holder_detail = UNSET
        else:
            change_account_holder_detail = ChangeAccountHolderDetail.from_dict(_change_account_holder_detail)

        _get_java_script = d.pop("getJavaScript", UNSET)
        get_java_script: Union[Unset, GetJavaScript]
        if isinstance(_get_java_script, Unset):
            get_java_script = UNSET
        else:
            get_java_script = GetJavaScript.from_dict(_get_java_script)

        _update_user_access_rights = d.pop("updateUserAccessRights", UNSET)
        update_user_access_rights: Union[Unset, UpdateUserAccessRights]
        if isinstance(_update_user_access_rights, Unset):
            update_user_access_rights = UNSET
        else:
            update_user_access_rights = UpdateUserAccessRights.from_dict(_update_user_access_rights)

        _information_change = d.pop("informationChange", UNSET)
        information_change: Union[Unset, InformationChange]
        if isinstance(_information_change, Unset):
            information_change = UNSET
        else:
            information_change = InformationChange.from_dict(_information_change)

        _add_additional_account = d.pop("addAdditionalAccount", UNSET)
        add_additional_account: Union[Unset, AddAdditionalAccount]
        if isinstance(_add_additional_account, Unset):
            add_additional_account = UNSET
        else:
            add_additional_account = AddAdditionalAccount.from_dict(_add_additional_account)

        _account_configuration = d.pop("accountConfiguration", UNSET)
        account_configuration: Union[Unset, AccountConfiguration]
        if isinstance(_account_configuration, Unset):
            account_configuration = UNSET
        else:
            account_configuration = AccountConfiguration.from_dict(_account_configuration)

        _allocate_van = d.pop("allocateVan", UNSET)
        allocate_van: Union[Unset, AllocateVAN]
        if isinstance(_allocate_van, Unset):
            allocate_van = UNSET
        else:
            allocate_van = AllocateVAN.from_dict(_allocate_van)

        _create_user_for_second_holder = d.pop("createUserForSecondHolder", UNSET)
        create_user_for_second_holder: Union[Unset, CreateUserForSecondHolder]
        if isinstance(_create_user_for_second_holder, Unset):
            create_user_for_second_holder = UNSET
        else:
            create_user_for_second_holder = CreateUserForSecondHolder.from_dict(_create_user_for_second_holder)

        _create_user = d.pop("createUser", UNSET)
        create_user: Union[Unset, CreateUser]
        if isinstance(_create_user, Unset):
            create_user = UNSET
        else:
            create_user = CreateUser.from_dict(_create_user)

        _update_tax_form = d.pop("updateTaxForm", UNSET)
        update_tax_form: Union[Unset, UpdateTaxForm]
        if isinstance(_update_tax_form, Unset):
            update_tax_form = UNSET
        else:
            update_tax_form = UpdateTaxForm.from_dict(_update_tax_form)

        _questionnaires = d.pop("questionnaires", UNSET)
        questionnaires: Union[Unset, Questionnaires]
        if isinstance(_questionnaires, Unset):
            questionnaires = UNSET
        else:
            questionnaires = Questionnaires.from_dict(_questionnaires)

        _security_questions = d.pop("securityQuestions", UNSET)
        security_questions: Union[Unset, SecurityQuestions]
        if isinstance(_security_questions, Unset):
            security_questions = UNSET
        else:
            security_questions = SecurityQuestions.from_dict(_security_questions)

        account_management_requests = cls(
            update_external_id=update_external_id,
            update_property_profile=update_property_profile,
            update_account_alias=update_account_alias,
            change_base_currency=change_base_currency,
            abandon_account=abandon_account,
            add_new_user=add_new_user,
            add_lev_fx_capability=add_lev_fx_capability,
            add_mi_fir_data=add_mi_fir_data,
            add_trading_permissions=add_trading_permissions,
            remove_trading_permissions=remove_trading_permissions,
            change_margin_type=change_margin_type,
            add_clp_capability=add_clp_capability,
            change_financial_information=change_financial_information,
            reset_abandoned_account=reset_abandoned_account,
            update_credentials=update_credentials,
            update_account_representatives=update_account_representatives,
            complete_login_message=complete_login_message,
            reopen_account=reopen_account,
            enroll_in_syep=enroll_in_syep,
            leave_syep=leave_syep,
            enroll_in_drip=enroll_in_drip,
            leave_drip=leave_drip,
            update_w8_ben=update_w8_ben,
            yodlee_session=yodlee_session,
            enable_account_in_brokerage=enable_account_in_brokerage,
            disable_account_in_brokerage=disable_account_in_brokerage,
            link_duplicate_account=link_duplicate_account,
            duplicate_account=duplicate_account,
            ach_instruction=ach_instruction,
            recurring_transaction=recurring_transaction,
            deposit_notification=deposit_notification,
            document_submission=document_submission,
            process_documents=process_documents,
            update_bcan=update_bcan,
            prohibited_country_questionnaire=prohibited_country_questionnaire,
            update_withholding_statement=update_withholding_statement,
            accredited_investor=accredited_investor,
            change_account_holder_detail=change_account_holder_detail,
            get_java_script=get_java_script,
            update_user_access_rights=update_user_access_rights,
            information_change=information_change,
            add_additional_account=add_additional_account,
            account_configuration=account_configuration,
            allocate_van=allocate_van,
            create_user_for_second_holder=create_user_for_second_holder,
            create_user=create_user,
            update_tax_form=update_tax_form,
            questionnaires=questionnaires,
            security_questions=security_questions,
        )

        account_management_requests.additional_properties = d
        return account_management_requests

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
