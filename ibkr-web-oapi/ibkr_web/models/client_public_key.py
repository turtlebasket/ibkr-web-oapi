from typing import Any, Dict, List, Type, TypeVar, Union

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

T = TypeVar("T", bound="ClientPublicKey")


@_attrs_define
class ClientPublicKey:
    """
    Attributes:
        key_id (str):
        key_bit_size (Union[Unset, int]):
        key_status (Union[Unset, str]):
        active (Union[Unset, bool]):
        symmetric (Union[Unset, bool]):
        public (Union[Unset, bool]):
        private (Union[Unset, bool]):
        asymmetric (Union[Unset, bool]):
        empty (Union[Unset, bool]):
    """

    key_id: str
    key_bit_size: Union[Unset, int] = UNSET
    key_status: Union[Unset, str] = UNSET
    active: Union[Unset, bool] = UNSET
    symmetric: Union[Unset, bool] = UNSET
    public: Union[Unset, bool] = UNSET
    private: Union[Unset, bool] = UNSET
    asymmetric: Union[Unset, bool] = UNSET
    empty: Union[Unset, bool] = UNSET
    additional_properties: Dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> Dict[str, Any]:
        key_id = self.key_id

        key_bit_size = self.key_bit_size

        key_status = self.key_status

        active = self.active

        symmetric = self.symmetric

        public = self.public

        private = self.private

        asymmetric = self.asymmetric

        empty = self.empty

        field_dict: Dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "keyId": key_id,
            }
        )
        if key_bit_size is not UNSET:
            field_dict["keyBitSize"] = key_bit_size
        if key_status is not UNSET:
            field_dict["keyStatus"] = key_status
        if active is not UNSET:
            field_dict["active"] = active
        if symmetric is not UNSET:
            field_dict["symmetric"] = symmetric
        if public is not UNSET:
            field_dict["public"] = public
        if private is not UNSET:
            field_dict["private"] = private
        if asymmetric is not UNSET:
            field_dict["asymmetric"] = asymmetric
        if empty is not UNSET:
            field_dict["empty"] = empty

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        d = src_dict.copy()
        key_id = d.pop("keyId")

        key_bit_size = d.pop("keyBitSize", UNSET)

        key_status = d.pop("keyStatus", UNSET)

        active = d.pop("active", UNSET)

        symmetric = d.pop("symmetric", UNSET)

        public = d.pop("public", UNSET)

        private = d.pop("private", UNSET)

        asymmetric = d.pop("asymmetric", UNSET)

        empty = d.pop("empty", UNSET)

        client_public_key = cls(
            key_id=key_id,
            key_bit_size=key_bit_size,
            key_status=key_status,
            active=active,
            symmetric=symmetric,
            public=public,
            private=private,
            asymmetric=asymmetric,
            empty=empty,
        )

        client_public_key.additional_properties = d
        return client_public_key

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
