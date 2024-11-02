from typing import Any, Dict, List, Type, TypeVar, Union

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

T = TypeVar("T", bound="SsoValidateResponseFeatures")


@_attrs_define
class SsoValidateResponseFeatures:
    """Returns supported features such as bonds and option trading.

    Attributes:
        envs (Union[Unset, str]): Returns the connecting environment to distinguish production or paper.
        wlms (Union[Unset, bool]): Internal Use Only
        realtime (Union[Unset, bool]): Returns if realtime market data is available
        bond (Union[Unset, bool]): Returns if bonds can be traded.
        option_chains (Union[Unset, bool]): Returns if option chains can be retrieved in the account.
        calendar (Union[Unset, bool]): Returns if trading calendars are enabled
        new_mf (Union[Unset, bool]): Internal Use Only
    """

    envs: Union[Unset, str] = UNSET
    wlms: Union[Unset, bool] = UNSET
    realtime: Union[Unset, bool] = UNSET
    bond: Union[Unset, bool] = UNSET
    option_chains: Union[Unset, bool] = UNSET
    calendar: Union[Unset, bool] = UNSET
    new_mf: Union[Unset, bool] = UNSET
    additional_properties: Dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> Dict[str, Any]:
        envs = self.envs

        wlms = self.wlms

        realtime = self.realtime

        bond = self.bond

        option_chains = self.option_chains

        calendar = self.calendar

        new_mf = self.new_mf

        field_dict: Dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if envs is not UNSET:
            field_dict["envs"] = envs
        if wlms is not UNSET:
            field_dict["wlms"] = wlms
        if realtime is not UNSET:
            field_dict["realtime"] = realtime
        if bond is not UNSET:
            field_dict["bond"] = bond
        if option_chains is not UNSET:
            field_dict["optionChains"] = option_chains
        if calendar is not UNSET:
            field_dict["calendar"] = calendar
        if new_mf is not UNSET:
            field_dict["newMf"] = new_mf

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        d = src_dict.copy()
        envs = d.pop("envs", UNSET)

        wlms = d.pop("wlms", UNSET)

        realtime = d.pop("realtime", UNSET)

        bond = d.pop("bond", UNSET)

        option_chains = d.pop("optionChains", UNSET)

        calendar = d.pop("calendar", UNSET)

        new_mf = d.pop("newMf", UNSET)

        sso_validate_response_features = cls(
            envs=envs,
            wlms=wlms,
            realtime=realtime,
            bond=bond,
            option_chains=option_chains,
            calendar=calendar,
            new_mf=new_mf,
        )

        sso_validate_response_features.additional_properties = d
        return sso_validate_response_features

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
