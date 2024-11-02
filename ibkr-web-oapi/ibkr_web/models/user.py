from typing import TYPE_CHECKING, Any, Dict, List, Type, TypeVar, Union, cast

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.user_privilege import UserPrivilege


T = TypeVar("T", bound="User")


@_attrs_define
class User:
    """
    Attributes:
        user_privileges (Union[Unset, List['UserPrivilege']]):
        md_services (Union[Unset, List[int]]):
        id (Union[Unset, str]):
        external_user_id (Union[Unset, str]):
        external_individual_id (Union[Unset, str]):
        encrypted_password (Union[Unset, str]):
        encrypted_key_name (Union[Unset, str]):
        prefix (Union[Unset, str]):
    """

    user_privileges: Union[Unset, List["UserPrivilege"]] = UNSET
    md_services: Union[Unset, List[int]] = UNSET
    id: Union[Unset, str] = UNSET
    external_user_id: Union[Unset, str] = UNSET
    external_individual_id: Union[Unset, str] = UNSET
    encrypted_password: Union[Unset, str] = UNSET
    encrypted_key_name: Union[Unset, str] = UNSET
    prefix: Union[Unset, str] = UNSET
    additional_properties: Dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> Dict[str, Any]:
        user_privileges: Union[Unset, List[Dict[str, Any]]] = UNSET
        if not isinstance(self.user_privileges, Unset):
            user_privileges = []
            for user_privileges_item_data in self.user_privileges:
                user_privileges_item = user_privileges_item_data.to_dict()
                user_privileges.append(user_privileges_item)

        md_services: Union[Unset, List[int]] = UNSET
        if not isinstance(self.md_services, Unset):
            md_services = self.md_services

        id = self.id

        external_user_id = self.external_user_id

        external_individual_id = self.external_individual_id

        encrypted_password = self.encrypted_password

        encrypted_key_name = self.encrypted_key_name

        prefix = self.prefix

        field_dict: Dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if user_privileges is not UNSET:
            field_dict["userPrivileges"] = user_privileges
        if md_services is not UNSET:
            field_dict["mdServices"] = md_services
        if id is not UNSET:
            field_dict["id"] = id
        if external_user_id is not UNSET:
            field_dict["externalUserId"] = external_user_id
        if external_individual_id is not UNSET:
            field_dict["externalIndividualId"] = external_individual_id
        if encrypted_password is not UNSET:
            field_dict["encryptedPassword"] = encrypted_password
        if encrypted_key_name is not UNSET:
            field_dict["encryptedKeyName"] = encrypted_key_name
        if prefix is not UNSET:
            field_dict["prefix"] = prefix

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        from ..models.user_privilege import UserPrivilege

        d = src_dict.copy()
        user_privileges = []
        _user_privileges = d.pop("userPrivileges", UNSET)
        for user_privileges_item_data in _user_privileges or []:
            user_privileges_item = UserPrivilege.from_dict(user_privileges_item_data)

            user_privileges.append(user_privileges_item)

        md_services = cast(List[int], d.pop("mdServices", UNSET))

        id = d.pop("id", UNSET)

        external_user_id = d.pop("externalUserId", UNSET)

        external_individual_id = d.pop("externalIndividualId", UNSET)

        encrypted_password = d.pop("encryptedPassword", UNSET)

        encrypted_key_name = d.pop("encryptedKeyName", UNSET)

        prefix = d.pop("prefix", UNSET)

        user = cls(
            user_privileges=user_privileges,
            md_services=md_services,
            id=id,
            external_user_id=external_user_id,
            external_individual_id=external_individual_id,
            encrypted_password=encrypted_password,
            encrypted_key_name=encrypted_key_name,
            prefix=prefix,
        )

        user.additional_properties = d
        return user

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
