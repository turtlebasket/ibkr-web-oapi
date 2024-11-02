from typing import TYPE_CHECKING, Any, Dict, List, Type, TypeVar, Union

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.brokerage_session_status_server_info import BrokerageSessionStatusServerInfo


T = TypeVar("T", bound="BrokerageSessionStatus")


@_attrs_define
class BrokerageSessionStatus:
    """
    Attributes:
        authenticated (Union[Unset, bool]): Returns whether your brokerage session is authenticated or not.
        competing (Union[Unset, bool]): Returns whether you have a competing brokerage session in another connection.
        connected (Union[Unset, bool]): Returns whether you are connected to the gateway or not.
        message (Union[Unset, str]): A message about your authenticate status if any.
        mac (Union[Unset, str]): Device MAC information.
        server_info (Union[Unset, BrokerageSessionStatusServerInfo]):
    """

    authenticated: Union[Unset, bool] = UNSET
    competing: Union[Unset, bool] = UNSET
    connected: Union[Unset, bool] = UNSET
    message: Union[Unset, str] = UNSET
    mac: Union[Unset, str] = UNSET
    server_info: Union[Unset, "BrokerageSessionStatusServerInfo"] = UNSET
    additional_properties: Dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> Dict[str, Any]:
        authenticated = self.authenticated

        competing = self.competing

        connected = self.connected

        message = self.message

        mac = self.mac

        server_info: Union[Unset, Dict[str, Any]] = UNSET
        if not isinstance(self.server_info, Unset):
            server_info = self.server_info.to_dict()

        field_dict: Dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if authenticated is not UNSET:
            field_dict["authenticated"] = authenticated
        if competing is not UNSET:
            field_dict["competing"] = competing
        if connected is not UNSET:
            field_dict["connected"] = connected
        if message is not UNSET:
            field_dict["message"] = message
        if mac is not UNSET:
            field_dict["MAC"] = mac
        if server_info is not UNSET:
            field_dict["serverInfo"] = server_info

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        from ..models.brokerage_session_status_server_info import BrokerageSessionStatusServerInfo

        d = src_dict.copy()
        authenticated = d.pop("authenticated", UNSET)

        competing = d.pop("competing", UNSET)

        connected = d.pop("connected", UNSET)

        message = d.pop("message", UNSET)

        mac = d.pop("MAC", UNSET)

        _server_info = d.pop("serverInfo", UNSET)
        server_info: Union[Unset, BrokerageSessionStatusServerInfo]
        if isinstance(_server_info, Unset):
            server_info = UNSET
        else:
            server_info = BrokerageSessionStatusServerInfo.from_dict(_server_info)

        brokerage_session_status = cls(
            authenticated=authenticated,
            competing=competing,
            connected=connected,
            message=message,
            mac=mac,
            server_info=server_info,
        )

        brokerage_session_status.additional_properties = d
        return brokerage_session_status

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
