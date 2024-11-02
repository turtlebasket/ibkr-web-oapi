from typing import TYPE_CHECKING, Any, Dict, List, Type, TypeVar, Union

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.client_public_key import ClientPublicKey


T = TypeVar("T", bound="ClientPublicKeySet")


@_attrs_define
class ClientPublicKeySet:
    """
    Attributes:
        keys (List['ClientPublicKey']):
        empty (Union[Unset, bool]):
    """

    keys: List["ClientPublicKey"]
    empty: Union[Unset, bool] = UNSET
    additional_properties: Dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> Dict[str, Any]:
        keys = []
        for keys_item_data in self.keys:
            keys_item = keys_item_data.to_dict()
            keys.append(keys_item)

        empty = self.empty

        field_dict: Dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "keys": keys,
            }
        )
        if empty is not UNSET:
            field_dict["empty"] = empty

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        from ..models.client_public_key import ClientPublicKey

        d = src_dict.copy()
        keys = []
        _keys = d.pop("keys")
        for keys_item_data in _keys:
            keys_item = ClientPublicKey.from_dict(keys_item_data)

            keys.append(keys_item)

        empty = d.pop("empty", UNSET)

        client_public_key_set = cls(
            keys=keys,
            empty=empty,
        )

        client_public_key_set.additional_properties = d
        return client_public_key_set

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
