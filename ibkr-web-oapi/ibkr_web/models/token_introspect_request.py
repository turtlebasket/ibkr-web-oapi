from typing import Any, Dict, List, Type, TypeVar, Union

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

T = TypeVar("T", bound="TokenIntrospectRequest")


@_attrs_define
class TokenIntrospectRequest:
    """
    Attributes:
        token (str): The token to introspect.
        token_type_hint (Union[Unset, str]): An optional hint to help the server identify the token type
    """

    token: str
    token_type_hint: Union[Unset, str] = UNSET
    additional_properties: Dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> Dict[str, Any]:
        token = self.token

        token_type_hint = self.token_type_hint

        field_dict: Dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "token": token,
            }
        )
        if token_type_hint is not UNSET:
            field_dict["token_type_hint"] = token_type_hint

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        d = src_dict.copy()
        token = d.pop("token")

        token_type_hint = d.pop("token_type_hint", UNSET)

        token_introspect_request = cls(
            token=token,
            token_type_hint=token_type_hint,
        )

        token_introspect_request.additional_properties = d
        return token_introspect_request

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