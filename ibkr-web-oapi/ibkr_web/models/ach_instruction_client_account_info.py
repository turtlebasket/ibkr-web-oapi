from typing import Any, Dict, List, Type, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..models.ach_instruction_client_account_info_bank_account_type_code import (
    AchInstructionClientAccountInfoBankAccountTypeCode,
)

T = TypeVar("T", bound="AchInstructionClientAccountInfo")


@_attrs_define
class AchInstructionClientAccountInfo:
    """
    Attributes:
        bank_routing_number (str):  Example: 202012983.
        bank_account_number (str):  Example: -1811638121.
        bank_name (str):  Example: JPM Chase.
        bank_account_type_code (AchInstructionClientAccountInfoBankAccountTypeCode):
    """

    bank_routing_number: str
    bank_account_number: str
    bank_name: str
    bank_account_type_code: AchInstructionClientAccountInfoBankAccountTypeCode
    additional_properties: Dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> Dict[str, Any]:
        bank_routing_number = self.bank_routing_number

        bank_account_number = self.bank_account_number

        bank_name = self.bank_name

        bank_account_type_code = self.bank_account_type_code.value

        field_dict: Dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "bankRoutingNumber": bank_routing_number,
                "bankAccountNumber": bank_account_number,
                "bankName": bank_name,
                "bankAccountTypeCode": bank_account_type_code,
            }
        )

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        d = src_dict.copy()
        bank_routing_number = d.pop("bankRoutingNumber")

        bank_account_number = d.pop("bankAccountNumber")

        bank_name = d.pop("bankName")

        bank_account_type_code = AchInstructionClientAccountInfoBankAccountTypeCode(d.pop("bankAccountTypeCode"))

        ach_instruction_client_account_info = cls(
            bank_routing_number=bank_routing_number,
            bank_account_number=bank_account_number,
            bank_name=bank_name,
            bank_account_type_code=bank_account_type_code,
        )

        ach_instruction_client_account_info.additional_properties = d
        return ach_instruction_client_account_info

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
