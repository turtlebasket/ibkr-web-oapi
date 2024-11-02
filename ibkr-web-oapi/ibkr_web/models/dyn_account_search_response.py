from typing import TYPE_CHECKING, Any, Dict, List, Type, TypeVar, Union

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.dyn_account_search_response_matched_accounts_item import DynAccountSearchResponseMatchedAccountsItem


T = TypeVar("T", bound="DynAccountSearchResponse")


@_attrs_define
class DynAccountSearchResponse:
    """
    Attributes:
        matched_accounts (Union[Unset, List['DynAccountSearchResponseMatchedAccountsItem']]): Contains a series of
            objects that pertain to the account information requested.
        pattern (Union[Unset, str]): Displays the searchPattern used for the request.
    """

    matched_accounts: Union[Unset, List["DynAccountSearchResponseMatchedAccountsItem"]] = UNSET
    pattern: Union[Unset, str] = UNSET
    additional_properties: Dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> Dict[str, Any]:
        matched_accounts: Union[Unset, List[Dict[str, Any]]] = UNSET
        if not isinstance(self.matched_accounts, Unset):
            matched_accounts = []
            for matched_accounts_item_data in self.matched_accounts:
                matched_accounts_item = matched_accounts_item_data.to_dict()
                matched_accounts.append(matched_accounts_item)

        pattern = self.pattern

        field_dict: Dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if matched_accounts is not UNSET:
            field_dict["matchedAccounts"] = matched_accounts
        if pattern is not UNSET:
            field_dict["pattern"] = pattern

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        from ..models.dyn_account_search_response_matched_accounts_item import (
            DynAccountSearchResponseMatchedAccountsItem,
        )

        d = src_dict.copy()
        matched_accounts = []
        _matched_accounts = d.pop("matchedAccounts", UNSET)
        for matched_accounts_item_data in _matched_accounts or []:
            matched_accounts_item = DynAccountSearchResponseMatchedAccountsItem.from_dict(matched_accounts_item_data)

            matched_accounts.append(matched_accounts_item)

        pattern = d.pop("pattern", UNSET)

        dyn_account_search_response = cls(
            matched_accounts=matched_accounts,
            pattern=pattern,
        )

        dyn_account_search_response.additional_properties = d
        return dyn_account_search_response

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
