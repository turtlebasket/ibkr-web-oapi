from typing import Any, Dict, List, Type, TypeVar, Union

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

T = TypeVar("T", bound="ACHDetails")


@_attrs_define
class ACHDetails:
    """
    Attributes:
        cust_init_ach (Union[Unset, bool]):
        bank_name (Union[Unset, str]):
    """

    cust_init_ach: Union[Unset, bool] = UNSET
    bank_name: Union[Unset, str] = UNSET
    additional_properties: Dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> Dict[str, Any]:
        cust_init_ach = self.cust_init_ach

        bank_name = self.bank_name

        field_dict: Dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if cust_init_ach is not UNSET:
            field_dict["custInitAch"] = cust_init_ach
        if bank_name is not UNSET:
            field_dict["bankName"] = bank_name

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        d = src_dict.copy()
        cust_init_ach = d.pop("custInitAch", UNSET)

        bank_name = d.pop("bankName", UNSET)

        ach_details = cls(
            cust_init_ach=cust_init_ach,
            bank_name=bank_name,
        )

        ach_details.additional_properties = d
        return ach_details

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
