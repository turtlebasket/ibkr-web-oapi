from typing import Any, Dict, List, Type, TypeVar, Union

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..models.allocate_van_currency import AllocateVANCurrency
from ..types import UNSET, Unset

T = TypeVar("T", bound="AllocateVAN")


@_attrs_define
class AllocateVAN:
    """
    Attributes:
        reference_account_id (Union[Unset, str]):
        currency (Union[Unset, AllocateVANCurrency]):
        country_code (Union[Unset, str]):
    """

    reference_account_id: Union[Unset, str] = UNSET
    currency: Union[Unset, AllocateVANCurrency] = UNSET
    country_code: Union[Unset, str] = UNSET
    additional_properties: Dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> Dict[str, Any]:
        reference_account_id = self.reference_account_id

        currency: Union[Unset, str] = UNSET
        if not isinstance(self.currency, Unset):
            currency = self.currency.value

        country_code = self.country_code

        field_dict: Dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if reference_account_id is not UNSET:
            field_dict["referenceAccountId"] = reference_account_id
        if currency is not UNSET:
            field_dict["currency"] = currency
        if country_code is not UNSET:
            field_dict["countryCode"] = country_code

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        d = src_dict.copy()
        reference_account_id = d.pop("referenceAccountId", UNSET)

        _currency = d.pop("currency", UNSET)
        currency: Union[Unset, AllocateVANCurrency]
        if isinstance(_currency, Unset):
            currency = UNSET
        else:
            currency = AllocateVANCurrency(_currency)

        country_code = d.pop("countryCode", UNSET)

        allocate_van = cls(
            reference_account_id=reference_account_id,
            currency=currency,
            country_code=country_code,
        )

        allocate_van.additional_properties = d
        return allocate_van

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
