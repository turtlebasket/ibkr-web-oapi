from typing import TYPE_CHECKING, Any, Dict, List, Type, TypeVar, Union

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.sso_validate_response_features import SsoValidateResponseFeatures


T = TypeVar("T", bound="SsoValidateResponse")


@_attrs_define
class SsoValidateResponse:
    """
    Attributes:
        user_id (Union[Unset, int]): Internal user identifier.
        user_name (Union[Unset, str]): current username logged in for the session.
        result (Union[Unset, bool]): Confirms if validation was successful. True if session was validated; false if not.
        auth_time (Union[Unset, int]): Returns the time of authentication in epoch time.
        sf_enabled (Union[Unset, bool]): (Internal use only)
        is_free_trial (Union[Unset, bool]): Returns if the account is a trial account or a funded account.
        credential (Union[Unset, str]): Returns the underlying username of the account.
        ip (Union[Unset, str]): Internal use only. Does not reflect the IP address of the user.
        expires (Union[Unset, int]): Returns the time until SSO session expiration in milliseconds.
        qualified_for_mobile_auth (Union[Unset, bool]): Returns if the customer requires two factor authentication.
        landing_app (Union[Unset, str]): Used for Client Portal (Internal use only)
        is_master (Union[Unset, bool]): Returns whether the account is a master account (true) or subaccount (false).
        last_accessed (Union[Unset, int]): Returns the last time the user was accessed in epoch time.
        login_type (Union[Unset, int]): Returns the login type. 1 for Live, 2 for Paper
        paper_user_name (Union[Unset, str]): Returns the paper username for the account.
        features (Union[Unset, SsoValidateResponseFeatures]): Returns supported features such as bonds and option
            trading.
        region (Union[Unset, str]): Returns the region connected to internally.
    """

    user_id: Union[Unset, int] = UNSET
    user_name: Union[Unset, str] = UNSET
    result: Union[Unset, bool] = UNSET
    auth_time: Union[Unset, int] = UNSET
    sf_enabled: Union[Unset, bool] = UNSET
    is_free_trial: Union[Unset, bool] = UNSET
    credential: Union[Unset, str] = UNSET
    ip: Union[Unset, str] = UNSET
    expires: Union[Unset, int] = UNSET
    qualified_for_mobile_auth: Union[Unset, bool] = UNSET
    landing_app: Union[Unset, str] = UNSET
    is_master: Union[Unset, bool] = UNSET
    last_accessed: Union[Unset, int] = UNSET
    login_type: Union[Unset, int] = UNSET
    paper_user_name: Union[Unset, str] = UNSET
    features: Union[Unset, "SsoValidateResponseFeatures"] = UNSET
    region: Union[Unset, str] = UNSET
    additional_properties: Dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> Dict[str, Any]:
        user_id = self.user_id

        user_name = self.user_name

        result = self.result

        auth_time = self.auth_time

        sf_enabled = self.sf_enabled

        is_free_trial = self.is_free_trial

        credential = self.credential

        ip = self.ip

        expires = self.expires

        qualified_for_mobile_auth = self.qualified_for_mobile_auth

        landing_app = self.landing_app

        is_master = self.is_master

        last_accessed = self.last_accessed

        login_type = self.login_type

        paper_user_name = self.paper_user_name

        features: Union[Unset, Dict[str, Any]] = UNSET
        if not isinstance(self.features, Unset):
            features = self.features.to_dict()

        region = self.region

        field_dict: Dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if user_id is not UNSET:
            field_dict["USER_ID"] = user_id
        if user_name is not UNSET:
            field_dict["USER_NAME"] = user_name
        if result is not UNSET:
            field_dict["RESULT"] = result
        if auth_time is not UNSET:
            field_dict["AUTH_TIME"] = auth_time
        if sf_enabled is not UNSET:
            field_dict["SF_ENABLED"] = sf_enabled
        if is_free_trial is not UNSET:
            field_dict["IS_FREE_TRIAL"] = is_free_trial
        if credential is not UNSET:
            field_dict["CREDENTIAL"] = credential
        if ip is not UNSET:
            field_dict["IP"] = ip
        if expires is not UNSET:
            field_dict["EXPIRES"] = expires
        if qualified_for_mobile_auth is not UNSET:
            field_dict["QUALIFIED_FOR_MOBILE_AUTH"] = qualified_for_mobile_auth
        if landing_app is not UNSET:
            field_dict["LANDING_APP"] = landing_app
        if is_master is not UNSET:
            field_dict["IS_MASTER"] = is_master
        if last_accessed is not UNSET:
            field_dict["lastAccessed"] = last_accessed
        if login_type is not UNSET:
            field_dict["loginType"] = login_type
        if paper_user_name is not UNSET:
            field_dict["PAPER_USER_NAME"] = paper_user_name
        if features is not UNSET:
            field_dict["features"] = features
        if region is not UNSET:
            field_dict["region"] = region

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        from ..models.sso_validate_response_features import SsoValidateResponseFeatures

        d = src_dict.copy()
        user_id = d.pop("USER_ID", UNSET)

        user_name = d.pop("USER_NAME", UNSET)

        result = d.pop("RESULT", UNSET)

        auth_time = d.pop("AUTH_TIME", UNSET)

        sf_enabled = d.pop("SF_ENABLED", UNSET)

        is_free_trial = d.pop("IS_FREE_TRIAL", UNSET)

        credential = d.pop("CREDENTIAL", UNSET)

        ip = d.pop("IP", UNSET)

        expires = d.pop("EXPIRES", UNSET)

        qualified_for_mobile_auth = d.pop("QUALIFIED_FOR_MOBILE_AUTH", UNSET)

        landing_app = d.pop("LANDING_APP", UNSET)

        is_master = d.pop("IS_MASTER", UNSET)

        last_accessed = d.pop("lastAccessed", UNSET)

        login_type = d.pop("loginType", UNSET)

        paper_user_name = d.pop("PAPER_USER_NAME", UNSET)

        _features = d.pop("features", UNSET)
        features: Union[Unset, SsoValidateResponseFeatures]
        if isinstance(_features, Unset):
            features = UNSET
        else:
            features = SsoValidateResponseFeatures.from_dict(_features)

        region = d.pop("region", UNSET)

        sso_validate_response = cls(
            user_id=user_id,
            user_name=user_name,
            result=result,
            auth_time=auth_time,
            sf_enabled=sf_enabled,
            is_free_trial=is_free_trial,
            credential=credential,
            ip=ip,
            expires=expires,
            qualified_for_mobile_auth=qualified_for_mobile_auth,
            landing_app=landing_app,
            is_master=is_master,
            last_accessed=last_accessed,
            login_type=login_type,
            paper_user_name=paper_user_name,
            features=features,
            region=region,
        )

        sso_validate_response.additional_properties = d
        return sso_validate_response

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
