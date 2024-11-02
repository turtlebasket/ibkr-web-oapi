from typing import Any, Dict, List, Type, TypeVar, Union

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

T = TypeVar("T", bound="ChangeBaseCurrency")


@_attrs_define
class ChangeBaseCurrency:
    """
    Attributes:
        reference_account_id (Union[Unset, str]):
        new_base_currency (Union[Unset, str]):
    """

    reference_account_id: Union[Unset, str] = UNSET
    new_base_currency: Union[Unset, str] = UNSET
    additional_properties: Dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> Dict[str, Any]:
        reference_account_id = self.reference_account_id

        new_base_currency = self.new_base_currency

        field_dict: Dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if reference_account_id is not UNSET:
            field_dict["referenceAccountId"] = reference_account_id
        if new_base_currency is not UNSET:
            field_dict["newBaseCurrency"] = new_base_currency

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        d = src_dict.copy()
        reference_account_id = d.pop("referenceAccountId", UNSET)

        new_base_currency = d.pop("newBaseCurrency", UNSET)

        change_base_currency = cls(
            reference_account_id=reference_account_id,
            new_base_currency=new_base_currency,
        )

        change_base_currency.additional_properties = d
        return change_base_currency

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
