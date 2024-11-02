from typing import Any, Dict, List, Type, TypeVar, Union

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

T = TypeVar("T", bound="DynAccountSearchResponseMatchedAccountsItem")


@_attrs_define
class DynAccountSearchResponseMatchedAccountsItem:
    """
    Attributes:
        account_id (Union[Unset, str]): Returns a matching account ID that corresponds to the matching value.
        alias (Union[Unset, str]): Returns the corresponding alias or alternative name for the specific account ID. May
            be a duplicate of the accountId value in most cases.
        allocation_id (Union[Unset, str]): Returns the allocation identifier used internally for the account.
    """

    account_id: Union[Unset, str] = UNSET
    alias: Union[Unset, str] = UNSET
    allocation_id: Union[Unset, str] = UNSET
    additional_properties: Dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> Dict[str, Any]:
        account_id = self.account_id

        alias = self.alias

        allocation_id = self.allocation_id

        field_dict: Dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if account_id is not UNSET:
            field_dict["accountId"] = account_id
        if alias is not UNSET:
            field_dict["alias"] = alias
        if allocation_id is not UNSET:
            field_dict["allocationId"] = allocation_id

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        d = src_dict.copy()
        account_id = d.pop("accountId", UNSET)

        alias = d.pop("alias", UNSET)

        allocation_id = d.pop("allocationId", UNSET)

        dyn_account_search_response_matched_accounts_item = cls(
            account_id=account_id,
            alias=alias,
            allocation_id=allocation_id,
        )

        dyn_account_search_response_matched_accounts_item.additional_properties = d
        return dyn_account_search_response_matched_accounts_item

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
