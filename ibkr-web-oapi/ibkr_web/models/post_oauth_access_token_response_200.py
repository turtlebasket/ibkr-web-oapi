from typing import Any, Dict, List, Type, TypeVar, Union

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

T = TypeVar("T", bound="PostOauthAccessTokenResponse200")


@_attrs_define
class PostOauthAccessTokenResponse200:
    """
    Attributes:
        is_true (Union[Unset, bool]): Indicates whether the authorizing username is paper or not.
        oauth_token (Union[Unset, str]): Permanent OAuth access token for the consumer with respect to the authorizing
            username. 20 character hex value.
        oauth_token_secret (Union[Unset, str]): OAuth token secret value. Base64-encoded string.
    """

    is_true: Union[Unset, bool] = UNSET
    oauth_token: Union[Unset, str] = UNSET
    oauth_token_secret: Union[Unset, str] = UNSET
    additional_properties: Dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> Dict[str, Any]:
        is_true = self.is_true

        oauth_token = self.oauth_token

        oauth_token_secret = self.oauth_token_secret

        field_dict: Dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if is_true is not UNSET:
            field_dict["is_true"] = is_true
        if oauth_token is not UNSET:
            field_dict["oauth_token"] = oauth_token
        if oauth_token_secret is not UNSET:
            field_dict["oauth_token_secret"] = oauth_token_secret

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        d = src_dict.copy()
        is_true = d.pop("is_true", UNSET)

        oauth_token = d.pop("oauth_token", UNSET)

        oauth_token_secret = d.pop("oauth_token_secret", UNSET)

        post_oauth_access_token_response_200 = cls(
            is_true=is_true,
            oauth_token=oauth_token,
            oauth_token_secret=oauth_token_secret,
        )

        post_oauth_access_token_response_200.additional_properties = d
        return post_oauth_access_token_response_200

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
