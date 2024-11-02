from typing import TYPE_CHECKING, Any, Dict, List, Type, TypeVar, Union

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.watchlists_response_data_user_lists_item import WatchlistsResponseDataUserListsItem


T = TypeVar("T", bound="WatchlistsResponseData")


@_attrs_define
class WatchlistsResponseData:
    """Contains the watchlist query results.

    Attributes:
        scanners_only (Union[Unset, bool]): Indicates if query results contain only market scanners.
        show_scanners (Union[Unset, bool]): Indicates if market scanners are included in query results.
        bulk_delete (Union[Unset, bool]): Indicates if username's watchlists can be bulk-deleted.
        user_lists (Union[Unset, List['WatchlistsResponseDataUserListsItem']]): Array of objects detailing the
            watchlists saved for the username in use in the current Web API session.
    """

    scanners_only: Union[Unset, bool] = UNSET
    show_scanners: Union[Unset, bool] = UNSET
    bulk_delete: Union[Unset, bool] = UNSET
    user_lists: Union[Unset, List["WatchlistsResponseDataUserListsItem"]] = UNSET
    additional_properties: Dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> Dict[str, Any]:
        scanners_only = self.scanners_only

        show_scanners = self.show_scanners

        bulk_delete = self.bulk_delete

        user_lists: Union[Unset, List[Dict[str, Any]]] = UNSET
        if not isinstance(self.user_lists, Unset):
            user_lists = []
            for user_lists_item_data in self.user_lists:
                user_lists_item = user_lists_item_data.to_dict()
                user_lists.append(user_lists_item)

        field_dict: Dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if scanners_only is not UNSET:
            field_dict["scanners_only"] = scanners_only
        if show_scanners is not UNSET:
            field_dict["show_scanners"] = show_scanners
        if bulk_delete is not UNSET:
            field_dict["bulk_delete"] = bulk_delete
        if user_lists is not UNSET:
            field_dict["user_lists"] = user_lists

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        from ..models.watchlists_response_data_user_lists_item import WatchlistsResponseDataUserListsItem

        d = src_dict.copy()
        scanners_only = d.pop("scanners_only", UNSET)

        show_scanners = d.pop("show_scanners", UNSET)

        bulk_delete = d.pop("bulk_delete", UNSET)

        user_lists = []
        _user_lists = d.pop("user_lists", UNSET)
        for user_lists_item_data in _user_lists or []:
            user_lists_item = WatchlistsResponseDataUserListsItem.from_dict(user_lists_item_data)

            user_lists.append(user_lists_item)

        watchlists_response_data = cls(
            scanners_only=scanners_only,
            show_scanners=show_scanners,
            bulk_delete=bulk_delete,
            user_lists=user_lists,
        )

        watchlists_response_data.additional_properties = d
        return watchlists_response_data

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
