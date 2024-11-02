from typing import Any, Dict, List, Type, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..models.traditional_bank_instruction_verification_bank_instruction_code import (
    TraditionalBankInstructionVerificationBankInstructionCode,
)

T = TypeVar("T", bound="TraditionalBankInstructionVerification")


@_attrs_define
class TraditionalBankInstructionVerification:
    """
    Attributes:
        client_instruction_id (float):  Example: 1012983.
        bank_instruction_code (TraditionalBankInstructionVerificationBankInstructionCode):  Example: USACH.
        bank_instruction_name (str):  Example: TestInstr.
        account_id (str):  Example: U453454.
        pending_instruction_id (float):  Example: 35354345.
        credit_amount_1 (float):  Example: 1.
        credit_amount_2 (float):  Example: 2.
    """

    client_instruction_id: float
    bank_instruction_code: TraditionalBankInstructionVerificationBankInstructionCode
    bank_instruction_name: str
    account_id: str
    pending_instruction_id: float
    credit_amount_1: float
    credit_amount_2: float
    additional_properties: Dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> Dict[str, Any]:
        client_instruction_id = self.client_instruction_id

        bank_instruction_code = self.bank_instruction_code.value

        bank_instruction_name = self.bank_instruction_name

        account_id = self.account_id

        pending_instruction_id = self.pending_instruction_id

        credit_amount_1 = self.credit_amount_1

        credit_amount_2 = self.credit_amount_2

        field_dict: Dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "clientInstructionId": client_instruction_id,
                "bankInstructionCode": bank_instruction_code,
                "bankInstructionName": bank_instruction_name,
                "accountId": account_id,
                "pendingInstructionId": pending_instruction_id,
                "creditAmount1": credit_amount_1,
                "creditAmount2": credit_amount_2,
            }
        )

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        d = src_dict.copy()
        client_instruction_id = d.pop("clientInstructionId")

        bank_instruction_code = TraditionalBankInstructionVerificationBankInstructionCode(d.pop("bankInstructionCode"))

        bank_instruction_name = d.pop("bankInstructionName")

        account_id = d.pop("accountId")

        pending_instruction_id = d.pop("pendingInstructionId")

        credit_amount_1 = d.pop("creditAmount1")

        credit_amount_2 = d.pop("creditAmount2")

        traditional_bank_instruction_verification = cls(
            client_instruction_id=client_instruction_id,
            bank_instruction_code=bank_instruction_code,
            bank_instruction_name=bank_instruction_name,
            account_id=account_id,
            pending_instruction_id=pending_instruction_id,
            credit_amount_1=credit_amount_1,
            credit_amount_2=credit_amount_2,
        )

        traditional_bank_instruction_verification.additional_properties = d
        return traditional_bank_instruction_verification

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
