from typing import Any, Dict, List, Type, TypeVar, Union

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..models.user_privilege_privilege import UserPrivilegePrivilege
from ..types import UNSET, Unset

T = TypeVar("T", bound="UserPrivilege")


@_attrs_define
class UserPrivilege:
    """
    Attributes:
        external_account_id (Union[Unset, str]):
        privilege (Union[Unset, UserPrivilegePrivilege]):
    """

    external_account_id: Union[Unset, str] = UNSET
    privilege: Union[Unset, UserPrivilegePrivilege] = UNSET
    additional_properties: Dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> Dict[str, Any]:
        external_account_id = self.external_account_id

        privilege: Union[Unset, str] = UNSET
        if not isinstance(self.privilege, Unset):
            privilege = self.privilege.value

        field_dict: Dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if external_account_id is not UNSET:
            field_dict["externalAccountId"] = external_account_id
        if privilege is not UNSET:
            field_dict["privilege"] = privilege

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        d = src_dict.copy()
        external_account_id = d.pop("externalAccountId", UNSET)

        _privilege = d.pop("privilege", UNSET)
        privilege: Union[Unset, UserPrivilegePrivilege]
        if isinstance(_privilege, Unset):
            privilege = UNSET
        else:
            privilege = UserPrivilegePrivilege(_privilege)

        user_privilege = cls(
            external_account_id=external_account_id,
            privilege=privilege,
        )

        user_privilege.additional_properties = d
        return user_privilege

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
