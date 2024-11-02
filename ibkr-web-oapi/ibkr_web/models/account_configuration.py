from typing import Any, Dict, List, Type, TypeVar, Union

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

T = TypeVar("T", bound="AccountConfiguration")


@_attrs_define
class AccountConfiguration:
    """
    Attributes:
        reference_account_id (Union[Unset, str]):
        type (Union[Unset, str]):
        value (Union[Unset, bool]):
    """

    reference_account_id: Union[Unset, str] = UNSET
    type: Union[Unset, str] = UNSET
    value: Union[Unset, bool] = UNSET
    additional_properties: Dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> Dict[str, Any]:
        reference_account_id = self.reference_account_id

        type = self.type

        value = self.value

        field_dict: Dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if reference_account_id is not UNSET:
            field_dict["referenceAccountId"] = reference_account_id
        if type is not UNSET:
            field_dict["type"] = type
        if value is not UNSET:
            field_dict["value"] = value

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        d = src_dict.copy()
        reference_account_id = d.pop("referenceAccountId", UNSET)

        type = d.pop("type", UNSET)

        value = d.pop("value", UNSET)

        account_configuration = cls(
            reference_account_id=reference_account_id,
            type=type,
            value=value,
        )

        account_configuration.additional_properties = d
        return account_configuration

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
