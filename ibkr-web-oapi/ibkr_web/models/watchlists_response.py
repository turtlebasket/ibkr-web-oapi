from typing import TYPE_CHECKING, Any, Dict, List, Type, TypeVar, Union

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..models.watchlists_response_action import WatchlistsResponseAction
from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.watchlists_response_data import WatchlistsResponseData


T = TypeVar("T", bound="WatchlistsResponse")


@_attrs_define
class WatchlistsResponse:
    """Object containing a successful query for watchlists saved for the username in use in the current Web API session.

    Attributes:
        data (Union[Unset, WatchlistsResponseData]): Contains the watchlist query results.
        action (Union[Unset, WatchlistsResponseAction]): Internal use. Always has value 'content'.
        mid (Union[Unset, str]): Internal use. Number of times endpoint has been visited during session.
    """

    data: Union[Unset, "WatchlistsResponseData"] = UNSET
    action: Union[Unset, WatchlistsResponseAction] = UNSET
    mid: Union[Unset, str] = UNSET
    additional_properties: Dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> Dict[str, Any]:
        data: Union[Unset, Dict[str, Any]] = UNSET
        if not isinstance(self.data, Unset):
            data = self.data.to_dict()

        action: Union[Unset, str] = UNSET
        if not isinstance(self.action, Unset):
            action = self.action.value

        mid = self.mid

        field_dict: Dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if data is not UNSET:
            field_dict["data"] = data
        if action is not UNSET:
            field_dict["action"] = action
        if mid is not UNSET:
            field_dict["MID"] = mid

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        from ..models.watchlists_response_data import WatchlistsResponseData

        d = src_dict.copy()
        _data = d.pop("data", UNSET)
        data: Union[Unset, WatchlistsResponseData]
        if isinstance(_data, Unset):
            data = UNSET
        else:
            data = WatchlistsResponseData.from_dict(_data)

        _action = d.pop("action", UNSET)
        action: Union[Unset, WatchlistsResponseAction]
        if isinstance(_action, Unset):
            action = UNSET
        else:
            action = WatchlistsResponseAction(_action)

        mid = d.pop("MID", UNSET)

        watchlists_response = cls(
            data=data,
            action=action,
            mid=mid,
        )

        watchlists_response.additional_properties = d
        return watchlists_response

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
