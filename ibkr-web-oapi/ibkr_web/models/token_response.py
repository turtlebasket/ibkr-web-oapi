from typing import Any, Dict, List, Type, TypeVar, Union

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

T = TypeVar("T", bound="TokenResponse")


@_attrs_define
class TokenResponse:
    """
    Attributes:
        access_token (Union[Unset, str]):
        token_type (Union[Unset, str]):
        scope (Union[Unset, str]):
        expires_in (Union[Unset, int]):
    """

    access_token: Union[Unset, str] = UNSET
    token_type: Union[Unset, str] = UNSET
    scope: Union[Unset, str] = UNSET
    expires_in: Union[Unset, int] = UNSET
    additional_properties: Dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> Dict[str, Any]:
        access_token = self.access_token

        token_type = self.token_type

        scope = self.scope

        expires_in = self.expires_in

        field_dict: Dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if access_token is not UNSET:
            field_dict["access_token"] = access_token
        if token_type is not UNSET:
            field_dict["token_type"] = token_type
        if scope is not UNSET:
            field_dict["scope"] = scope
        if expires_in is not UNSET:
            field_dict["expires_in"] = expires_in

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        d = src_dict.copy()
        access_token = d.pop("access_token", UNSET)

        token_type = d.pop("token_type", UNSET)

        scope = d.pop("scope", UNSET)

        expires_in = d.pop("expires_in", UNSET)

        token_response = cls(
            access_token=access_token,
            token_type=token_type,
            scope=scope,
            expires_in=expires_in,
        )

        token_response.additional_properties = d
        return token_response

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
