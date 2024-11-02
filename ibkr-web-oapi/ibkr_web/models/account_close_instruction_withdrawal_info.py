from typing import Any, Dict, List, Type, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..models.account_close_instruction_withdrawal_info_bank_instruction_method import (
    AccountCloseInstructionWithdrawalInfoBankInstructionMethod,
)

T = TypeVar("T", bound="AccountCloseInstructionWithdrawalInfo")


@_attrs_define
class AccountCloseInstructionWithdrawalInfo:
    """
    Attributes:
        bank_instruction_name (str):  Example: Bank Instruction Name.
        bank_instruction_method (AccountCloseInstructionWithdrawalInfoBankInstructionMethod):  Example: WIRE.
    """

    bank_instruction_name: str
    bank_instruction_method: AccountCloseInstructionWithdrawalInfoBankInstructionMethod
    additional_properties: Dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> Dict[str, Any]:
        bank_instruction_name = self.bank_instruction_name

        bank_instruction_method = self.bank_instruction_method.value

        field_dict: Dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "bankInstructionName": bank_instruction_name,
                "bankInstructionMethod": bank_instruction_method,
            }
        )

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        d = src_dict.copy()
        bank_instruction_name = d.pop("bankInstructionName")

        bank_instruction_method = AccountCloseInstructionWithdrawalInfoBankInstructionMethod(
            d.pop("bankInstructionMethod")
        )

        account_close_instruction_withdrawal_info = cls(
            bank_instruction_name=bank_instruction_name,
            bank_instruction_method=bank_instruction_method,
        )

        account_close_instruction_withdrawal_info.additional_properties = d
        return account_close_instruction_withdrawal_info

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
