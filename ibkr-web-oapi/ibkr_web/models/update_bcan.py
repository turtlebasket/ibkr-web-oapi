from typing import Any, Dict, List, Type, TypeVar, Union

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

T = TypeVar("T", bound="UpdateBCAN")


@_attrs_define
class UpdateBCAN:
    """
    Attributes:
        reference_account_id (Union[Unset, str]):
        bcan (Union[Unset, str]):
        ce_number (Union[Unset, str]):
    """

    reference_account_id: Union[Unset, str] = UNSET
    bcan: Union[Unset, str] = UNSET
    ce_number: Union[Unset, str] = UNSET
    additional_properties: Dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> Dict[str, Any]:
        reference_account_id = self.reference_account_id

        bcan = self.bcan

        ce_number = self.ce_number

        field_dict: Dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if reference_account_id is not UNSET:
            field_dict["referenceAccountId"] = reference_account_id
        if bcan is not UNSET:
            field_dict["bcan"] = bcan
        if ce_number is not UNSET:
            field_dict["ceNumber"] = ce_number

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        d = src_dict.copy()
        reference_account_id = d.pop("referenceAccountId", UNSET)

        bcan = d.pop("bcan", UNSET)

        ce_number = d.pop("ceNumber", UNSET)

        update_bcan = cls(
            reference_account_id=reference_account_id,
            bcan=bcan,
            ce_number=ce_number,
        )

        update_bcan.additional_properties = d
        return update_bcan

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
