from typing import TYPE_CHECKING, Any, Dict, List, Type, TypeVar, Union

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..models.watchlist_delete_success_action import WatchlistDeleteSuccessAction
from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.watchlist_delete_success_data import WatchlistDeleteSuccessData


T = TypeVar("T", bound="WatchlistDeleteSuccess")


@_attrs_define
class WatchlistDeleteSuccess:
    """Object detailing the successful deletion of a watchlist.

    Attributes:
        data (Union[Unset, WatchlistDeleteSuccessData]):
        action (Union[Unset, WatchlistDeleteSuccessAction]): Internal use. Always has value 'context'.
        mid (Union[Unset, str]): Internal use. Number of times endpoint has been visited during session.
    """

    data: Union[Unset, "WatchlistDeleteSuccessData"] = UNSET
    action: Union[Unset, WatchlistDeleteSuccessAction] = UNSET
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
        from ..models.watchlist_delete_success_data import WatchlistDeleteSuccessData

        d = src_dict.copy()
        _data = d.pop("data", UNSET)
        data: Union[Unset, WatchlistDeleteSuccessData]
        if isinstance(_data, Unset):
            data = UNSET
        else:
            data = WatchlistDeleteSuccessData.from_dict(_data)

        _action = d.pop("action", UNSET)
        action: Union[Unset, WatchlistDeleteSuccessAction]
        if isinstance(_action, Unset):
            action = UNSET
        else:
            action = WatchlistDeleteSuccessAction(_action)

        mid = d.pop("MID", UNSET)

        watchlist_delete_success = cls(
            data=data,
            action=action,
            mid=mid,
        )

        watchlist_delete_success.additional_properties = d
        return watchlist_delete_success

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
