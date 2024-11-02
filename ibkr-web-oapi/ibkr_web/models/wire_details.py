from typing import Any, Dict, List, Type, TypeVar, Union

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

T = TypeVar("T", bound="WireDetails")


@_attrs_define
class WireDetails:
    """
    Attributes:
        bank_name (Union[Unset, str]):
        bank_account_number (Union[Unset, str]):
        bank_code (Union[Unset, str]):
        routing_number (Union[Unset, str]):
        instruction (Union[Unset, str]):
        country_code (Union[Unset, str]):
        reference_number (Union[Unset, str]):
    """

    bank_name: Union[Unset, str] = UNSET
    bank_account_number: Union[Unset, str] = UNSET
    bank_code: Union[Unset, str] = UNSET
    routing_number: Union[Unset, str] = UNSET
    instruction: Union[Unset, str] = UNSET
    country_code: Union[Unset, str] = UNSET
    reference_number: Union[Unset, str] = UNSET
    additional_properties: Dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> Dict[str, Any]:
        bank_name = self.bank_name

        bank_account_number = self.bank_account_number

        bank_code = self.bank_code

        routing_number = self.routing_number

        instruction = self.instruction

        country_code = self.country_code

        reference_number = self.reference_number

        field_dict: Dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if bank_name is not UNSET:
            field_dict["bankName"] = bank_name
        if bank_account_number is not UNSET:
            field_dict["bankAccountNumber"] = bank_account_number
        if bank_code is not UNSET:
            field_dict["bankCode"] = bank_code
        if routing_number is not UNSET:
            field_dict["routingNumber"] = routing_number
        if instruction is not UNSET:
            field_dict["instruction"] = instruction
        if country_code is not UNSET:
            field_dict["countryCode"] = country_code
        if reference_number is not UNSET:
            field_dict["referenceNumber"] = reference_number

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        d = src_dict.copy()
        bank_name = d.pop("bankName", UNSET)

        bank_account_number = d.pop("bankAccountNumber", UNSET)

        bank_code = d.pop("bankCode", UNSET)

        routing_number = d.pop("routingNumber", UNSET)

        instruction = d.pop("instruction", UNSET)

        country_code = d.pop("countryCode", UNSET)

        reference_number = d.pop("referenceNumber", UNSET)

        wire_details = cls(
            bank_name=bank_name,
            bank_account_number=bank_account_number,
            bank_code=bank_code,
            routing_number=routing_number,
            instruction=instruction,
            country_code=country_code,
            reference_number=reference_number,
        )

        wire_details.additional_properties = d
        return wire_details

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
