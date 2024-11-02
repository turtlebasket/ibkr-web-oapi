from typing import Any, Dict, List, Type, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..models.edda_instruction_debtor_identification_document_type import (
    EddaInstructionDebtorIdentificationDocumentType,
)

T = TypeVar("T", bound="EddaInstruction")


@_attrs_define
class EddaInstruction:
    """
    Attributes:
        client_instruction_id (float):  Example: 1012983.
        bank_instruction_name (str):  Example: Instruction Name.
        currency (str):  Example: CNH.
        account_id (str):  Example: U2323232.
        bank_branch_code (str):  Example: 003.
        bank_account_number (str):  Example: 132456.
        bank_clearing_code (str):  Example: 003.
        debtor_identification_document_type (EddaInstructionDebtorIdentificationDocumentType):  Example: hkId.
    """

    client_instruction_id: float
    bank_instruction_name: str
    currency: str
    account_id: str
    bank_branch_code: str
    bank_account_number: str
    bank_clearing_code: str
    debtor_identification_document_type: EddaInstructionDebtorIdentificationDocumentType
    additional_properties: Dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> Dict[str, Any]:
        client_instruction_id = self.client_instruction_id

        bank_instruction_name = self.bank_instruction_name

        currency = self.currency

        account_id = self.account_id

        bank_branch_code = self.bank_branch_code

        bank_account_number = self.bank_account_number

        bank_clearing_code = self.bank_clearing_code

        debtor_identification_document_type = self.debtor_identification_document_type.value

        field_dict: Dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "clientInstructionId": client_instruction_id,
                "bankInstructionName": bank_instruction_name,
                "currency": currency,
                "accountId": account_id,
                "bankBranchCode": bank_branch_code,
                "bankAccountNumber": bank_account_number,
                "bankClearingCode": bank_clearing_code,
                "debtorIdentificationDocumentType": debtor_identification_document_type,
            }
        )

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        d = src_dict.copy()
        client_instruction_id = d.pop("clientInstructionId")

        bank_instruction_name = d.pop("bankInstructionName")

        currency = d.pop("currency")

        account_id = d.pop("accountId")

        bank_branch_code = d.pop("bankBranchCode")

        bank_account_number = d.pop("bankAccountNumber")

        bank_clearing_code = d.pop("bankClearingCode")

        debtor_identification_document_type = EddaInstructionDebtorIdentificationDocumentType(
            d.pop("debtorIdentificationDocumentType")
        )

        edda_instruction = cls(
            client_instruction_id=client_instruction_id,
            bank_instruction_name=bank_instruction_name,
            currency=currency,
            account_id=account_id,
            bank_branch_code=bank_branch_code,
            bank_account_number=bank_account_number,
            bank_clearing_code=bank_clearing_code,
            debtor_identification_document_type=debtor_identification_document_type,
        )

        edda_instruction.additional_properties = d
        return edda_instruction

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
