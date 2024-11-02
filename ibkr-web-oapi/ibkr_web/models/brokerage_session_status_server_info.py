from typing import Any, Dict, List, Type, TypeVar, Union

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

T = TypeVar("T", bound="BrokerageSessionStatusServerInfo")


@_attrs_define
class BrokerageSessionStatusServerInfo:
    """
    Attributes:
        server_name (Union[Unset, str]): IBKR server information. Internal use only.
        server_version (Union[Unset, str]): IBKR version information. Internal use only.
        fail (Union[Unset, str]): Returns the reason for failing to retrieve authentication status.
    """

    server_name: Union[Unset, str] = UNSET
    server_version: Union[Unset, str] = UNSET
    fail: Union[Unset, str] = UNSET
    additional_properties: Dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> Dict[str, Any]:
        server_name = self.server_name

        server_version = self.server_version

        fail = self.fail

        field_dict: Dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if server_name is not UNSET:
            field_dict["serverName"] = server_name
        if server_version is not UNSET:
            field_dict["serverVersion"] = server_version
        if fail is not UNSET:
            field_dict["fail"] = fail

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        d = src_dict.copy()
        server_name = d.pop("serverName", UNSET)

        server_version = d.pop("serverVersion", UNSET)

        fail = d.pop("fail", UNSET)

        brokerage_session_status_server_info = cls(
            server_name=server_name,
            server_version=server_version,
            fail=fail,
        )

        brokerage_session_status_server_info.additional_properties = d
        return brokerage_session_status_server_info

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
