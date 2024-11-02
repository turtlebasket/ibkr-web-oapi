from typing import TYPE_CHECKING, Any, Dict, List, Type, TypeVar, Union

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..models.application_input_language import ApplicationInputLanguage
from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.account import Account
    from ..models.add_additional_account import AddAdditionalAccount
    from ..models.customer import Customer
    from ..models.document import Document
    from ..models.user import User


T = TypeVar("T", bound="Application")


@_attrs_define
class Application:
    """
    Attributes:
        customer (Union[Unset, Customer]):
        accounts (Union[Unset, List['Account']]):
        users (Union[Unset, List['User']]):
        documents (Union[Unset, List['Document']]):
        additional_accounts (Union[Unset, List['AddAdditionalAccount']]):
        master_account_id (Union[Unset, str]):
        id (Union[Unset, str]):
        input_language (Union[Unset, ApplicationInputLanguage]):
        translation (Union[Unset, bool]):
        paper_account (Union[Unset, bool]):
    """

    customer: Union[Unset, "Customer"] = UNSET
    accounts: Union[Unset, List["Account"]] = UNSET
    users: Union[Unset, List["User"]] = UNSET
    documents: Union[Unset, List["Document"]] = UNSET
    additional_accounts: Union[Unset, List["AddAdditionalAccount"]] = UNSET
    master_account_id: Union[Unset, str] = UNSET
    id: Union[Unset, str] = UNSET
    input_language: Union[Unset, ApplicationInputLanguage] = UNSET
    translation: Union[Unset, bool] = UNSET
    paper_account: Union[Unset, bool] = UNSET
    additional_properties: Dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> Dict[str, Any]:
        customer: Union[Unset, Dict[str, Any]] = UNSET
        if not isinstance(self.customer, Unset):
            customer = self.customer.to_dict()

        accounts: Union[Unset, List[Dict[str, Any]]] = UNSET
        if not isinstance(self.accounts, Unset):
            accounts = []
            for accounts_item_data in self.accounts:
                accounts_item = accounts_item_data.to_dict()
                accounts.append(accounts_item)

        users: Union[Unset, List[Dict[str, Any]]] = UNSET
        if not isinstance(self.users, Unset):
            users = []
            for users_item_data in self.users:
                users_item = users_item_data.to_dict()
                users.append(users_item)

        documents: Union[Unset, List[Dict[str, Any]]] = UNSET
        if not isinstance(self.documents, Unset):
            documents = []
            for documents_item_data in self.documents:
                documents_item = documents_item_data.to_dict()
                documents.append(documents_item)

        additional_accounts: Union[Unset, List[Dict[str, Any]]] = UNSET
        if not isinstance(self.additional_accounts, Unset):
            additional_accounts = []
            for additional_accounts_item_data in self.additional_accounts:
                additional_accounts_item = additional_accounts_item_data.to_dict()
                additional_accounts.append(additional_accounts_item)

        master_account_id = self.master_account_id

        id = self.id

        input_language: Union[Unset, str] = UNSET
        if not isinstance(self.input_language, Unset):
            input_language = self.input_language.value

        translation = self.translation

        paper_account = self.paper_account

        field_dict: Dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if customer is not UNSET:
            field_dict["customer"] = customer
        if accounts is not UNSET:
            field_dict["accounts"] = accounts
        if users is not UNSET:
            field_dict["users"] = users
        if documents is not UNSET:
            field_dict["documents"] = documents
        if additional_accounts is not UNSET:
            field_dict["additionalAccounts"] = additional_accounts
        if master_account_id is not UNSET:
            field_dict["masterAccountId"] = master_account_id
        if id is not UNSET:
            field_dict["id"] = id
        if input_language is not UNSET:
            field_dict["inputLanguage"] = input_language
        if translation is not UNSET:
            field_dict["translation"] = translation
        if paper_account is not UNSET:
            field_dict["paperAccount"] = paper_account

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        from ..models.account import Account
        from ..models.add_additional_account import AddAdditionalAccount
        from ..models.customer import Customer
        from ..models.document import Document
        from ..models.user import User

        d = src_dict.copy()
        _customer = d.pop("customer", UNSET)
        customer: Union[Unset, Customer]
        if isinstance(_customer, Unset):
            customer = UNSET
        else:
            customer = Customer.from_dict(_customer)

        accounts = []
        _accounts = d.pop("accounts", UNSET)
        for accounts_item_data in _accounts or []:
            accounts_item = Account.from_dict(accounts_item_data)

            accounts.append(accounts_item)

        users = []
        _users = d.pop("users", UNSET)
        for users_item_data in _users or []:
            users_item = User.from_dict(users_item_data)

            users.append(users_item)

        documents = []
        _documents = d.pop("documents", UNSET)
        for documents_item_data in _documents or []:
            documents_item = Document.from_dict(documents_item_data)

            documents.append(documents_item)

        additional_accounts = []
        _additional_accounts = d.pop("additionalAccounts", UNSET)
        for additional_accounts_item_data in _additional_accounts or []:
            additional_accounts_item = AddAdditionalAccount.from_dict(additional_accounts_item_data)

            additional_accounts.append(additional_accounts_item)

        master_account_id = d.pop("masterAccountId", UNSET)

        id = d.pop("id", UNSET)

        _input_language = d.pop("inputLanguage", UNSET)
        input_language: Union[Unset, ApplicationInputLanguage]
        if isinstance(_input_language, Unset):
            input_language = UNSET
        else:
            input_language = ApplicationInputLanguage(_input_language)

        translation = d.pop("translation", UNSET)

        paper_account = d.pop("paperAccount", UNSET)

        application = cls(
            customer=customer,
            accounts=accounts,
            users=users,
            documents=documents,
            additional_accounts=additional_accounts,
            master_account_id=master_account_id,
            id=id,
            input_language=input_language,
            translation=translation,
            paper_account=paper_account,
        )

        application.additional_properties = d
        return application

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
