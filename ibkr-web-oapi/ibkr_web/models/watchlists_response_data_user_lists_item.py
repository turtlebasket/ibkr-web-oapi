from typing import Any, Dict, List, Type, TypeVar, Union

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..models.watchlists_response_data_user_lists_item_type import WatchlistsResponseDataUserListsItemType
from ..types import UNSET, Unset

T = TypeVar("T", bound="WatchlistsResponseDataUserListsItem")


@_attrs_define
class WatchlistsResponseDataUserListsItem:
    """Details of a single watchlist.

    Attributes:
        is_open (Union[Unset, bool]): Internal use. Indicates if the watchlist is currently in use.
        read_only (Union[Unset, bool]): Indicates if the watchlist can be edited.
        name (Union[Unset, str]): Display name of the watchlist.
        modified (Union[Unset, int]): Unix timestamp in milliseconds of the last modification of the watchlist.
        id (Union[Unset, str]): Watchlist ID of the watchlist.
        type (Union[Unset, WatchlistsResponseDataUserListsItemType]): Always has value 'watchlist'.
    """

    is_open: Union[Unset, bool] = UNSET
    read_only: Union[Unset, bool] = UNSET
    name: Union[Unset, str] = UNSET
    modified: Union[Unset, int] = UNSET
    id: Union[Unset, str] = UNSET
    type: Union[Unset, WatchlistsResponseDataUserListsItemType] = UNSET
    additional_properties: Dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> Dict[str, Any]:
        is_open = self.is_open

        read_only = self.read_only

        name = self.name

        modified = self.modified

        id = self.id

        type: Union[Unset, str] = UNSET
        if not isinstance(self.type, Unset):
            type = self.type.value

        field_dict: Dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if is_open is not UNSET:
            field_dict["is_open"] = is_open
        if read_only is not UNSET:
            field_dict["read_only"] = read_only
        if name is not UNSET:
            field_dict["name"] = name
        if modified is not UNSET:
            field_dict["modified"] = modified
        if id is not UNSET:
            field_dict["id"] = id
        if type is not UNSET:
            field_dict["type"] = type

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        d = src_dict.copy()
        is_open = d.pop("is_open", UNSET)

        read_only = d.pop("read_only", UNSET)

        name = d.pop("name", UNSET)

        modified = d.pop("modified", UNSET)

        id = d.pop("id", UNSET)

        _type = d.pop("type", UNSET)
        type: Union[Unset, WatchlistsResponseDataUserListsItemType]
        if isinstance(_type, Unset):
            type = UNSET
        else:
            type = WatchlistsResponseDataUserListsItemType(_type)

        watchlists_response_data_user_lists_item = cls(
            is_open=is_open,
            read_only=read_only,
            name=name,
            modified=modified,
            id=id,
            type=type,
        )

        watchlists_response_data_user_lists_item.additional_properties = d
        return watchlists_response_data_user_lists_item

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
