from typing import TYPE_CHECKING, Any, Dict, List, Type, TypeVar, Union, cast

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.user_accounts_response_acct_props import UserAccountsResponseAcctProps
    from ..models.user_accounts_response_aliases import UserAccountsResponseAliases
    from ..models.user_accounts_response_allow_features import UserAccountsResponseAllowFeatures
    from ..models.user_accounts_response_chart_periods import UserAccountsResponseChartPeriods
    from ..models.user_accounts_response_server_info import UserAccountsResponseServerInfo


T = TypeVar("T", bound="UserAccountsResponse")


@_attrs_define
class UserAccountsResponse:
    """
    Attributes:
        accounts (Union[Unset, List[str]]): Returns an array of all accessible accountIds.
        acct_props (Union[Unset, UserAccountsResponseAcctProps]): Returns an json object for each accessible account’s
            properties.
        aliases (Union[Unset, UserAccountsResponseAliases]):
        allow_features (Union[Unset, UserAccountsResponseAllowFeatures]):
        chart_periods (Union[Unset, UserAccountsResponseChartPeriods]):
        groups (Union[Unset, List[str]]):
        profiles (Union[Unset, List[str]]):
        selected_account (Union[Unset, str]):
        server_info (Union[Unset, UserAccountsResponseServerInfo]):
        session_id (Union[Unset, str]):
        is_ft (Union[Unset, bool]):
        is_paper (Union[Unset, bool]):
    """

    accounts: Union[Unset, List[str]] = UNSET
    acct_props: Union[Unset, "UserAccountsResponseAcctProps"] = UNSET
    aliases: Union[Unset, "UserAccountsResponseAliases"] = UNSET
    allow_features: Union[Unset, "UserAccountsResponseAllowFeatures"] = UNSET
    chart_periods: Union[Unset, "UserAccountsResponseChartPeriods"] = UNSET
    groups: Union[Unset, List[str]] = UNSET
    profiles: Union[Unset, List[str]] = UNSET
    selected_account: Union[Unset, str] = UNSET
    server_info: Union[Unset, "UserAccountsResponseServerInfo"] = UNSET
    session_id: Union[Unset, str] = UNSET
    is_ft: Union[Unset, bool] = UNSET
    is_paper: Union[Unset, bool] = UNSET
    additional_properties: Dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> Dict[str, Any]:
        accounts: Union[Unset, List[str]] = UNSET
        if not isinstance(self.accounts, Unset):
            accounts = self.accounts

        acct_props: Union[Unset, Dict[str, Any]] = UNSET
        if not isinstance(self.acct_props, Unset):
            acct_props = self.acct_props.to_dict()

        aliases: Union[Unset, Dict[str, Any]] = UNSET
        if not isinstance(self.aliases, Unset):
            aliases = self.aliases.to_dict()

        allow_features: Union[Unset, Dict[str, Any]] = UNSET
        if not isinstance(self.allow_features, Unset):
            allow_features = self.allow_features.to_dict()

        chart_periods: Union[Unset, Dict[str, Any]] = UNSET
        if not isinstance(self.chart_periods, Unset):
            chart_periods = self.chart_periods.to_dict()

        groups: Union[Unset, List[str]] = UNSET
        if not isinstance(self.groups, Unset):
            groups = self.groups

        profiles: Union[Unset, List[str]] = UNSET
        if not isinstance(self.profiles, Unset):
            profiles = self.profiles

        selected_account = self.selected_account

        server_info: Union[Unset, Dict[str, Any]] = UNSET
        if not isinstance(self.server_info, Unset):
            server_info = self.server_info.to_dict()

        session_id = self.session_id

        is_ft = self.is_ft

        is_paper = self.is_paper

        field_dict: Dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if accounts is not UNSET:
            field_dict["accounts"] = accounts
        if acct_props is not UNSET:
            field_dict["acctProps"] = acct_props
        if aliases is not UNSET:
            field_dict["aliases"] = aliases
        if allow_features is not UNSET:
            field_dict["allowFeatures"] = allow_features
        if chart_periods is not UNSET:
            field_dict["chartPeriods"] = chart_periods
        if groups is not UNSET:
            field_dict["groups"] = groups
        if profiles is not UNSET:
            field_dict["profiles"] = profiles
        if selected_account is not UNSET:
            field_dict["selectedAccount"] = selected_account
        if server_info is not UNSET:
            field_dict["serverInfo"] = server_info
        if session_id is not UNSET:
            field_dict["sessionId"] = session_id
        if is_ft is not UNSET:
            field_dict["isFt"] = is_ft
        if is_paper is not UNSET:
            field_dict["isPaper"] = is_paper

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        from ..models.user_accounts_response_acct_props import UserAccountsResponseAcctProps
        from ..models.user_accounts_response_aliases import UserAccountsResponseAliases
        from ..models.user_accounts_response_allow_features import UserAccountsResponseAllowFeatures
        from ..models.user_accounts_response_chart_periods import UserAccountsResponseChartPeriods
        from ..models.user_accounts_response_server_info import UserAccountsResponseServerInfo

        d = src_dict.copy()
        accounts = cast(List[str], d.pop("accounts", UNSET))

        _acct_props = d.pop("acctProps", UNSET)
        acct_props: Union[Unset, UserAccountsResponseAcctProps]
        if isinstance(_acct_props, Unset):
            acct_props = UNSET
        else:
            acct_props = UserAccountsResponseAcctProps.from_dict(_acct_props)

        _aliases = d.pop("aliases", UNSET)
        aliases: Union[Unset, UserAccountsResponseAliases]
        if isinstance(_aliases, Unset):
            aliases = UNSET
        else:
            aliases = UserAccountsResponseAliases.from_dict(_aliases)

        _allow_features = d.pop("allowFeatures", UNSET)
        allow_features: Union[Unset, UserAccountsResponseAllowFeatures]
        if isinstance(_allow_features, Unset):
            allow_features = UNSET
        else:
            allow_features = UserAccountsResponseAllowFeatures.from_dict(_allow_features)

        _chart_periods = d.pop("chartPeriods", UNSET)
        chart_periods: Union[Unset, UserAccountsResponseChartPeriods]
        if isinstance(_chart_periods, Unset):
            chart_periods = UNSET
        else:
            chart_periods = UserAccountsResponseChartPeriods.from_dict(_chart_periods)

        groups = cast(List[str], d.pop("groups", UNSET))

        profiles = cast(List[str], d.pop("profiles", UNSET))

        selected_account = d.pop("selectedAccount", UNSET)

        _server_info = d.pop("serverInfo", UNSET)
        server_info: Union[Unset, UserAccountsResponseServerInfo]
        if isinstance(_server_info, Unset):
            server_info = UNSET
        else:
            server_info = UserAccountsResponseServerInfo.from_dict(_server_info)

        session_id = d.pop("sessionId", UNSET)

        is_ft = d.pop("isFt", UNSET)

        is_paper = d.pop("isPaper", UNSET)

        user_accounts_response = cls(
            accounts=accounts,
            acct_props=acct_props,
            aliases=aliases,
            allow_features=allow_features,
            chart_periods=chart_periods,
            groups=groups,
            profiles=profiles,
            selected_account=selected_account,
            server_info=server_info,
            session_id=session_id,
            is_ft=is_ft,
            is_paper=is_paper,
        )

        user_accounts_response.additional_properties = d
        return user_accounts_response

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
