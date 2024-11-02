from typing import Any, Dict, List, Type, TypeVar, Union

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

T = TypeVar("T", bound="TokenRequest")


@_attrs_define
class TokenRequest:
    """
    Attributes:
        grant_type (str): The [authorization grant flow](https://dataetracker.ietf.org/doc/html/rfc6749#section-1.3) for
            the creation of the tokens.
        client_assertion (str): The compact [client assertion](https://www.rfc-editor.org/rfc/rfc7521.html) token used
            to authenticate you as a registered client.
        client_assertion_type (str): The [client assertion type](https://www.rfc-
            editor.org/rfc/rfc7521.html#section-4.2) that identifies the client assertion.
        scope (Union[Unset, str]): The space-delimited list of scopes Example: echo.read echo.write.
    """

    grant_type: str
    client_assertion: str
    client_assertion_type: str
    scope: Union[Unset, str] = UNSET
    additional_properties: Dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> Dict[str, Any]:
        grant_type = self.grant_type

        client_assertion = self.client_assertion

        client_assertion_type = self.client_assertion_type

        scope = self.scope

        field_dict: Dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "grant_type": grant_type,
                "client_assertion": client_assertion,
                "client_assertion_type": client_assertion_type,
            }
        )
        if scope is not UNSET:
            field_dict["scope"] = scope

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        d = src_dict.copy()
        grant_type = d.pop("grant_type")

        client_assertion = d.pop("client_assertion")

        client_assertion_type = d.pop("client_assertion_type")

        scope = d.pop("scope", UNSET)

        token_request = cls(
            grant_type=grant_type,
            client_assertion=client_assertion,
            client_assertion_type=client_assertion_type,
            scope=scope,
        )

        token_request.additional_properties = d
        return token_request

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
