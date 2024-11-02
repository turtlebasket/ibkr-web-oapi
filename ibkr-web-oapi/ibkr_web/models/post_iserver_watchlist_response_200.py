from typing import Any, Dict, List, Type, TypeVar, Union, cast

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

T = TypeVar("T", bound="PostIserverWatchlistResponse200")


@_attrs_define
class PostIserverWatchlistResponse200:
    """
    Attributes:
        id (Union[Unset, str]): The submitted watchlist ID.
        hash_ (Union[Unset, str]): IB's internal hash of the submitted watchlist.
        name (Union[Unset, str]): The submitted human-readable watchlist name.
        read_only (Union[Unset, bool]): Indicates whether watchlist is write-restricted. User-created watchlists will
            always show false.
        instruments (Union[Unset, List[str]]): Array will always be empty. Contents can be queried via GET
            /iserver/watchlist?id=
    """

    id: Union[Unset, str] = UNSET
    hash_: Union[Unset, str] = UNSET
    name: Union[Unset, str] = UNSET
    read_only: Union[Unset, bool] = UNSET
    instruments: Union[Unset, List[str]] = UNSET
    additional_properties: Dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> Dict[str, Any]:
        id = self.id

        hash_ = self.hash_

        name = self.name

        read_only = self.read_only

        instruments: Union[Unset, List[str]] = UNSET
        if not isinstance(self.instruments, Unset):
            instruments = self.instruments

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
        d = src_dict.copy()
        id = d.pop("id", UNSET)

        hash_ = d.pop("hash", UNSET)

        name = d.pop("name", UNSET)

        read_only = d.pop("readOnly", UNSET)

        instruments = cast(List[str], d.pop("instruments", UNSET))

        post_iserver_watchlist_response_200 = cls(
            id=id,
            hash_=hash_,
            name=name,
            read_only=read_only,
            instruments=instruments,
        )

        post_iserver_watchlist_response_200.additional_properties = d
        return post_iserver_watchlist_response_200

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
