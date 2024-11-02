from typing import TYPE_CHECKING, Any, Dict, List, Type, TypeVar, Union

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.account import Account
    from ..models.customer import Customer
    from ..models.document import Document
    from ..models.user import User


T = TypeVar("T", bound="AddAdditionalAccount")


@_attrs_define
class AddAdditionalAccount:
    """
    Attributes:
        customer (Union[Unset, Customer]):
        account (Union[Unset, Account]):
        documents (Union[Unset, List['Document']]):
        users (Union[Unset, List['User']]):
        reference_account_id (Union[Unset, str]):
    """

    customer: Union[Unset, "Customer"] = UNSET
    account: Union[Unset, "Account"] = UNSET
    documents: Union[Unset, List["Document"]] = UNSET
    users: Union[Unset, List["User"]] = UNSET
    reference_account_id: Union[Unset, str] = UNSET
    additional_properties: Dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> Dict[str, Any]:
        customer: Union[Unset, Dict[str, Any]] = UNSET
        if not isinstance(self.customer, Unset):
            customer = self.customer.to_dict()

        account: Union[Unset, Dict[str, Any]] = UNSET
        if not isinstance(self.account, Unset):
            account = self.account.to_dict()

        documents: Union[Unset, List[Dict[str, Any]]] = UNSET
        if not isinstance(self.documents, Unset):
            documents = []
            for documents_item_data in self.documents:
                documents_item = documents_item_data.to_dict()
                documents.append(documents_item)

        users: Union[Unset, List[Dict[str, Any]]] = UNSET
        if not isinstance(self.users, Unset):
            users = []
            for users_item_data in self.users:
                users_item = users_item_data.to_dict()
                users.append(users_item)

        reference_account_id = self.reference_account_id

        field_dict: Dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if customer is not UNSET:
            field_dict["customer"] = customer
        if account is not UNSET:
            field_dict["account"] = account
        if documents is not UNSET:
            field_dict["documents"] = documents
        if users is not UNSET:
            field_dict["users"] = users
        if reference_account_id is not UNSET:
            field_dict["referenceAccountId"] = reference_account_id

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        from ..models.account import Account
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

        _account = d.pop("account", UNSET)
        account: Union[Unset, Account]
        if isinstance(_account, Unset):
            account = UNSET
        else:
            account = Account.from_dict(_account)

        documents = []
        _documents = d.pop("documents", UNSET)
        for documents_item_data in _documents or []:
            documents_item = Document.from_dict(documents_item_data)

            documents.append(documents_item)

        users = []
        _users = d.pop("users", UNSET)
        for users_item_data in _users or []:
            users_item = User.from_dict(users_item_data)

            users.append(users_item)

        reference_account_id = d.pop("referenceAccountId", UNSET)

        add_additional_account = cls(
            customer=customer,
            account=account,
            documents=documents,
            users=users,
            reference_account_id=reference_account_id,
        )

        add_additional_account.additional_properties = d
        return add_additional_account

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
