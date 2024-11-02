from typing import Any, Dict, List, Type, TypeVar, Union

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

T = TypeVar("T", bound="PostOauthLiveSessionTokenResponse200")


@_attrs_define
class PostOauthLiveSessionTokenResponse200:
    """
    Attributes:
        diffie_hellman_challenge (Union[Unset, str]): Diffie-Hellman challenge value used to compute live session token
            locally by client.
        live_session_token_signature (Union[Unset, str]): Signature value used to validate successful client-side
            computation of live session token.
        live_session_token_expiration (Union[Unset, int]): Unix timestamp in milliseconds of time of live session token
            computation by IB. Live session tokens are valid for 24 hours from this time.
    """

    diffie_hellman_challenge: Union[Unset, str] = UNSET
    live_session_token_signature: Union[Unset, str] = UNSET
    live_session_token_expiration: Union[Unset, int] = UNSET
    additional_properties: Dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> Dict[str, Any]:
        diffie_hellman_challenge = self.diffie_hellman_challenge

        live_session_token_signature = self.live_session_token_signature

        live_session_token_expiration = self.live_session_token_expiration

        field_dict: Dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if diffie_hellman_challenge is not UNSET:
            field_dict["diffie_hellman_challenge"] = diffie_hellman_challenge
        if live_session_token_signature is not UNSET:
            field_dict["live_session_token_signature"] = live_session_token_signature
        if live_session_token_expiration is not UNSET:
            field_dict["live_session_token_expiration"] = live_session_token_expiration

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        d = src_dict.copy()
        diffie_hellman_challenge = d.pop("diffie_hellman_challenge", UNSET)

        live_session_token_signature = d.pop("live_session_token_signature", UNSET)

        live_session_token_expiration = d.pop("live_session_token_expiration", UNSET)

        post_oauth_live_session_token_response_200 = cls(
            diffie_hellman_challenge=diffie_hellman_challenge,
            live_session_token_signature=live_session_token_signature,
            live_session_token_expiration=live_session_token_expiration,
        )

        post_oauth_live_session_token_response_200.additional_properties = d
        return post_oauth_live_session_token_response_200

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
