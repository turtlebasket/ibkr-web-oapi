from typing import TYPE_CHECKING, Any, Dict, List, Type, TypeVar, Union

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.account_status_response import AccountStatusResponse


T = TypeVar("T", bound="AccountStatusBulkResponse")


@_attrs_define
class AccountStatusBulkResponse:
    """
    Attributes:
        accounts (Union[Unset, List['AccountStatusResponse']]):
        offset (Union[Unset, int]):
        limit (Union[Unset, int]):
        total (Union[Unset, int]):
    """

    accounts: Union[Unset, List["AccountStatusResponse"]] = UNSET
    offset: Union[Unset, int] = UNSET
    limit: Union[Unset, int] = UNSET
    total: Union[Unset, int] = UNSET
    additional_properties: Dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> Dict[str, Any]:
        accounts: Union[Unset, List[Dict[str, Any]]] = UNSET
        if not isinstance(self.accounts, Unset):
            accounts = []
            for accounts_item_data in self.accounts:
                accounts_item = accounts_item_data.to_dict()
                accounts.append(accounts_item)

        offset = self.offset

        limit = self.limit

        total = self.total

        field_dict: Dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if accounts is not UNSET:
            field_dict["accounts"] = accounts
        if offset is not UNSET:
            field_dict["offset"] = offset
        if limit is not UNSET:
            field_dict["limit"] = limit
        if total is not UNSET:
            field_dict["total"] = total

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        from ..models.account_status_response import AccountStatusResponse

        d = src_dict.copy()
        accounts = []
        _accounts = d.pop("accounts", UNSET)
        for accounts_item_data in _accounts or []:
            accounts_item = AccountStatusResponse.from_dict(accounts_item_data)

            accounts.append(accounts_item)

        offset = d.pop("offset", UNSET)

        limit = d.pop("limit", UNSET)

        total = d.pop("total", UNSET)

        account_status_bulk_response = cls(
            accounts=accounts,
            offset=offset,
            limit=limit,
            total=total,
        )

        account_status_bulk_response.additional_properties = d
        return account_status_bulk_response

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
