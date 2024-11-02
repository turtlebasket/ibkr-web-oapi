from typing import Any, Dict, List, Type, TypeVar, Union

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

T = TypeVar("T", bound="UpdatePassword")


@_attrs_define
class UpdatePassword:
    """
    Attributes:
        encrypted_password (Union[Unset, str]):
        encrypted_key_name (Union[Unset, str]):
        token (Union[Unset, str]):
    """

    encrypted_password: Union[Unset, str] = UNSET
    encrypted_key_name: Union[Unset, str] = UNSET
    token: Union[Unset, str] = UNSET
    additional_properties: Dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> Dict[str, Any]:
        encrypted_password = self.encrypted_password

        encrypted_key_name = self.encrypted_key_name

        token = self.token

        field_dict: Dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if encrypted_password is not UNSET:
            field_dict["encryptedPassword"] = encrypted_password
        if encrypted_key_name is not UNSET:
            field_dict["encryptedKeyName"] = encrypted_key_name
        if token is not UNSET:
            field_dict["token"] = token

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        d = src_dict.copy()
        encrypted_password = d.pop("encryptedPassword", UNSET)

        encrypted_key_name = d.pop("encryptedKeyName", UNSET)

        token = d.pop("token", UNSET)

        update_password = cls(
            encrypted_password=encrypted_password,
            encrypted_key_name=encrypted_key_name,
            token=token,
        )

        update_password.additional_properties = d
        return update_password

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
