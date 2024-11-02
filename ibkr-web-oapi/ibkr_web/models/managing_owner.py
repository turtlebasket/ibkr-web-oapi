from typing import Any, Dict, List, Type, TypeVar, Union

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

T = TypeVar("T", bound="ManagingOwner")


@_attrs_define
class ManagingOwner:
    """
    Attributes:
        external_id (Union[Unset, str]):
        is_25_percent_owner (Union[Unset, bool]):
    """

    external_id: Union[Unset, str] = UNSET
    is_25_percent_owner: Union[Unset, bool] = UNSET
    additional_properties: Dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> Dict[str, Any]:
        external_id = self.external_id

        is_25_percent_owner = self.is_25_percent_owner

        field_dict: Dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if external_id is not UNSET:
            field_dict["externalId"] = external_id
        if is_25_percent_owner is not UNSET:
            field_dict["is25PercentOwner"] = is_25_percent_owner

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        d = src_dict.copy()
        external_id = d.pop("externalId", UNSET)

        is_25_percent_owner = d.pop("is25PercentOwner", UNSET)

        managing_owner = cls(
            external_id=external_id,
            is_25_percent_owner=is_25_percent_owner,
        )

        managing_owner.additional_properties = d
        return managing_owner

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
