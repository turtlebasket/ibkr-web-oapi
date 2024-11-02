from typing import Any, Dict, List, Type, TypeVar, Union, cast

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

T = TypeVar("T", bound="UpdateUserAccessRights")


@_attrs_define
class UpdateUserAccessRights:
    """
    Attributes:
        sub_accounts (Union[Unset, List[str]]):
        rep_id (Union[Unset, str]):
        action (Union[Unset, str]):
    """

    sub_accounts: Union[Unset, List[str]] = UNSET
    rep_id: Union[Unset, str] = UNSET
    action: Union[Unset, str] = UNSET
    additional_properties: Dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> Dict[str, Any]:
        sub_accounts: Union[Unset, List[str]] = UNSET
        if not isinstance(self.sub_accounts, Unset):
            sub_accounts = self.sub_accounts

        rep_id = self.rep_id

        action = self.action

        field_dict: Dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if sub_accounts is not UNSET:
            field_dict["subAccounts"] = sub_accounts
        if rep_id is not UNSET:
            field_dict["repId"] = rep_id
        if action is not UNSET:
            field_dict["action"] = action

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        d = src_dict.copy()
        sub_accounts = cast(List[str], d.pop("subAccounts", UNSET))

        rep_id = d.pop("repId", UNSET)

        action = d.pop("action", UNSET)

        update_user_access_rights = cls(
            sub_accounts=sub_accounts,
            rep_id=rep_id,
            action=action,
        )

        update_user_access_rights.additional_properties = d
        return update_user_access_rights

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
