from typing import TYPE_CHECKING, Any, Dict, List, Type, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..models.ach_instruction_ach_type import AchInstructionAchType
from ..models.ach_instruction_bank_instruction_code import AchInstructionBankInstructionCode

if TYPE_CHECKING:
    from ..models.ach_instruction_client_account_info import AchInstructionClientAccountInfo


T = TypeVar("T", bound="AchInstruction")


@_attrs_define
class AchInstruction:
    """
    Attributes:
        client_instruction_id (float):  Example: 1012983.
        bank_instruction_code (AchInstructionBankInstructionCode):  Example: USACH.
        ach_type (AchInstructionAchType):  Example: DEBIT_CREDIT.
        bank_instruction_name (str):  Example: TestInstr.
        currency (str):  Example: USD.
        account_id (str):  Example: U223454.
        client_account_info (AchInstructionClientAccountInfo):
    """

    client_instruction_id: float
    bank_instruction_code: AchInstructionBankInstructionCode
    ach_type: AchInstructionAchType
    bank_instruction_name: str
    currency: str
    account_id: str
    client_account_info: "AchInstructionClientAccountInfo"
    additional_properties: Dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> Dict[str, Any]:
        client_instruction_id = self.client_instruction_id

        bank_instruction_code = self.bank_instruction_code.value

        ach_type = self.ach_type.value

        bank_instruction_name = self.bank_instruction_name

        currency = self.currency

        account_id = self.account_id

        client_account_info = self.client_account_info.to_dict()

        field_dict: Dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "clientInstructionId": client_instruction_id,
                "bankInstructionCode": bank_instruction_code,
                "achType": ach_type,
                "bankInstructionName": bank_instruction_name,
                "currency": currency,
                "accountId": account_id,
                "clientAccountInfo": client_account_info,
            }
        )

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        from ..models.ach_instruction_client_account_info import AchInstructionClientAccountInfo

        d = src_dict.copy()
        client_instruction_id = d.pop("clientInstructionId")

        bank_instruction_code = AchInstructionBankInstructionCode(d.pop("bankInstructionCode"))

        ach_type = AchInstructionAchType(d.pop("achType"))

        bank_instruction_name = d.pop("bankInstructionName")

        currency = d.pop("currency")

        account_id = d.pop("accountId")

        client_account_info = AchInstructionClientAccountInfo.from_dict(d.pop("clientAccountInfo"))

        ach_instruction = cls(
            client_instruction_id=client_instruction_id,
            bank_instruction_code=bank_instruction_code,
            ach_type=ach_type,
            bank_instruction_name=bank_instruction_name,
            currency=currency,
            account_id=account_id,
            client_account_info=client_account_info,
        )

        ach_instruction.additional_properties = d
        return ach_instruction

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
