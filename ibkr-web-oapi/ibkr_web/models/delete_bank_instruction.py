from typing import Any, Dict, List, Type, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..models.delete_bank_instruction_bank_instruction_method import DeleteBankInstructionBankInstructionMethod

T = TypeVar("T", bound="DeleteBankInstruction")


@_attrs_define
class DeleteBankInstruction:
    """
    Attributes:
        client_instruction_id (float):  Example: 1012983.
        account_id (str):  Example: U32343.
        bank_instruction_name (str):  Example: Test-instruction.
        bank_instruction_method (DeleteBankInstructionBankInstructionMethod):  Example: WIRE.
        currency (str):  Example: USD.
    """

    client_instruction_id: float
    account_id: str
    bank_instruction_name: str
    bank_instruction_method: DeleteBankInstructionBankInstructionMethod
    currency: str
    additional_properties: Dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> Dict[str, Any]:
        client_instruction_id = self.client_instruction_id

        account_id = self.account_id

        bank_instruction_name = self.bank_instruction_name

        bank_instruction_method = self.bank_instruction_method.value

        currency = self.currency

        field_dict: Dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "clientInstructionId": client_instruction_id,
                "accountId": account_id,
                "bankInstructionName": bank_instruction_name,
                "bankInstructionMethod": bank_instruction_method,
                "currency": currency,
            }
        )

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        d = src_dict.copy()
        client_instruction_id = d.pop("clientInstructionId")

        account_id = d.pop("accountId")

        bank_instruction_name = d.pop("bankInstructionName")

        bank_instruction_method = DeleteBankInstructionBankInstructionMethod(d.pop("bankInstructionMethod"))

        currency = d.pop("currency")

        delete_bank_instruction = cls(
            client_instruction_id=client_instruction_id,
            account_id=account_id,
            bank_instruction_name=bank_instruction_name,
            bank_instruction_method=bank_instruction_method,
            currency=currency,
        )

        delete_bank_instruction.additional_properties = d
        return delete_bank_instruction

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
