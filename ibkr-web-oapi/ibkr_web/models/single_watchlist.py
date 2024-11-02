from typing import TYPE_CHECKING, Any, Dict, List, Type, TypeVar, Union

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.single_watchlist_entry import SingleWatchlistEntry


T = TypeVar("T", bound="SingleWatchlist")


@_attrs_define
class SingleWatchlist:
    """Object detailing a single watchlist.

    Attributes:
        id (Union[Unset, str]): Identifier of the watchlist.
        hash_ (Union[Unset, str]): Internal use. Unique hash of the watchlist.
        name (Union[Unset, str]): Human-readable display name of the watchlist.
        read_only (Union[Unset, bool]): Indicates whether the watchlist can be edited.
        instruments (Union[Unset, List['SingleWatchlistEntry']]): Array of instruments contained in the watchlist.
    """

    id: Union[Unset, str] = UNSET
    hash_: Union[Unset, str] = UNSET
    name: Union[Unset, str] = UNSET
    read_only: Union[Unset, bool] = UNSET
    instruments: Union[Unset, List["SingleWatchlistEntry"]] = UNSET
    additional_properties: Dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> Dict[str, Any]:
        id = self.id

        hash_ = self.hash_

        name = self.name

        read_only = self.read_only

        instruments: Union[Unset, List[Dict[str, Any]]] = UNSET
        if not isinstance(self.instruments, Unset):
            instruments = []
            for instruments_item_data in self.instruments:
                instruments_item = instruments_item_data.to_dict()
                instruments.append(instruments_item)

        field_dict: Dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if id is not UNSET:
            field_dict["id"] = id
        if hash_ is not UNSET:
            field_dict["hash"] = hash_
        if name is not UNSET:
            field_dict["name"] = name
        if read_only is not UNSET:
            field_dict["readOnly"] = read_only
        if instruments is not UNSET:
            field_dict["instruments"] = instruments

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        from ..models.single_watchlist_entry import SingleWatchlistEntry

        d = src_dict.copy()
        id = d.pop("id", UNSET)

        hash_ = d.pop("hash", UNSET)

        name = d.pop("name", UNSET)

        read_only = d.pop("readOnly", UNSET)

        instruments = []
        _instruments = d.pop("instruments", UNSET)
        for instruments_item_data in _instruments or []:
            instruments_item = SingleWatchlistEntry.from_dict(instruments_item_data)

            instruments.append(instruments_item)

        single_watchlist = cls(
            id=id,
            hash_=hash_,
            name=name,
            read_only=read_only,
            instruments=instruments,
        )

        single_watchlist.additional_properties = d
        return single_watchlist

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
