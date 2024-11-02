from typing import Any, Dict, List, Type, TypeVar, Union

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

T = TypeVar("T", bound="DuplicateAccount")


@_attrs_define
class DuplicateAccount:
    """
    Attributes:
        reference_account_id (Union[Unset, str]):
        number_of_duplicates (Union[Unset, int]):
    """

    reference_account_id: Union[Unset, str] = UNSET
    number_of_duplicates: Union[Unset, int] = UNSET
    additional_properties: Dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> Dict[str, Any]:
        reference_account_id = self.reference_account_id

        number_of_duplicates = self.number_of_duplicates

        field_dict: Dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if reference_account_id is not UNSET:
            field_dict["referenceAccountId"] = reference_account_id
        if number_of_duplicates is not UNSET:
            field_dict["numberOfDuplicates"] = number_of_duplicates

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        d = src_dict.copy()
        reference_account_id = d.pop("referenceAccountId", UNSET)

        number_of_duplicates = d.pop("numberOfDuplicates", UNSET)

        duplicate_account = cls(
            reference_account_id=reference_account_id,
            number_of_duplicates=number_of_duplicates,
        )

        duplicate_account.additional_properties = d
        return duplicate_account

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