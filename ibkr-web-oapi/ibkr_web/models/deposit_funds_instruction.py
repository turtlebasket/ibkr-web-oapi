from typing import TYPE_CHECKING, Any, Dict, List, Type, TypeVar, Union

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..models.deposit_funds_instruction_bank_instruction_method import DepositFundsInstructionBankInstructionMethod
from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.deposit_funds_instruction_ira_deposit_detail import DepositFundsInstructionIraDepositDetail
    from ..models.recurring_instruction_detail import RecurringInstructionDetail


T = TypeVar("T", bound="DepositFundsInstruction")


@_attrs_define
class DepositFundsInstruction:
    """
    Attributes:
        client_instruction_id (float):  Example: 1012983.
        account_id (str):  Example: U46377.
        currency (str):  Example: USD.
        amount (float):  Example: 100.
        bank_instruction_method (DepositFundsInstructionBankInstructionMethod):  Example: WIRE.
        sending_institution (Union[Unset, str]):  Example: Sending Institution name.
        identifier (Union[Unset, str]):  Example: indentifier.
        special_instruction (Union[Unset, str]):  Example: U46377.
        bank_instruction_name (Union[Unset, str]):  Example: Instruction.
        sender_institution_name (Union[Unset, str]):  Example: Senders Institution name.
        ira_deposit_detail (Union[Unset, DepositFundsInstructionIraDepositDetail]):
        recurring_instruction_detail (Union[Unset, RecurringInstructionDetail]):
    """

    client_instruction_id: float
    account_id: str
    currency: str
    amount: float
    bank_instruction_method: DepositFundsInstructionBankInstructionMethod
    sending_institution: Union[Unset, str] = UNSET
    identifier: Union[Unset, str] = UNSET
    special_instruction: Union[Unset, str] = UNSET
    bank_instruction_name: Union[Unset, str] = UNSET
    sender_institution_name: Union[Unset, str] = UNSET
    ira_deposit_detail: Union[Unset, "DepositFundsInstructionIraDepositDetail"] = UNSET
    recurring_instruction_detail: Union[Unset, "RecurringInstructionDetail"] = UNSET
    additional_properties: Dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> Dict[str, Any]:
        client_instruction_id = self.client_instruction_id

        account_id = self.account_id

        currency = self.currency

        amount = self.amount

        bank_instruction_method = self.bank_instruction_method.value

        sending_institution = self.sending_institution

        identifier = self.identifier

        special_instruction = self.special_instruction

        bank_instruction_name = self.bank_instruction_name

        sender_institution_name = self.sender_institution_name

        ira_deposit_detail: Union[Unset, Dict[str, Any]] = UNSET
        if not isinstance(self.ira_deposit_detail, Unset):
            ira_deposit_detail = self.ira_deposit_detail.to_dict()

        recurring_instruction_detail: Union[Unset, Dict[str, Any]] = UNSET
        if not isinstance(self.recurring_instruction_detail, Unset):
            recurring_instruction_detail = self.recurring_instruction_detail.to_dict()

        field_dict: Dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "clientInstructionId": client_instruction_id,
                "accountId": account_id,
                "currency": currency,
                "amount": amount,
                "bankInstructionMethod": bank_instruction_method,
            }
        )
        if sending_institution is not UNSET:
            field_dict["sendingInstitution"] = sending_institution
        if identifier is not UNSET:
            field_dict["identifier"] = identifier
        if special_instruction is not UNSET:
            field_dict["specialInstruction"] = special_instruction
        if bank_instruction_name is not UNSET:
            field_dict["bankInstructionName"] = bank_instruction_name
        if sender_institution_name is not UNSET:
            field_dict["senderInstitutionName"] = sender_institution_name
        if ira_deposit_detail is not UNSET:
            field_dict["iraDepositDetail"] = ira_deposit_detail
        if recurring_instruction_detail is not UNSET:
            field_dict["recurringInstructionDetail"] = recurring_instruction_detail

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        from ..models.deposit_funds_instruction_ira_deposit_detail import DepositFundsInstructionIraDepositDetail
        from ..models.recurring_instruction_detail import RecurringInstructionDetail

        d = src_dict.copy()
        client_instruction_id = d.pop("clientInstructionId")

        account_id = d.pop("accountId")

        currency = d.pop("currency")

        amount = d.pop("amount")

        bank_instruction_method = DepositFundsInstructionBankInstructionMethod(d.pop("bankInstructionMethod"))

        sending_institution = d.pop("sendingInstitution", UNSET)

        identifier = d.pop("identifier", UNSET)

        special_instruction = d.pop("specialInstruction", UNSET)

        bank_instruction_name = d.pop("bankInstructionName", UNSET)

        sender_institution_name = d.pop("senderInstitutionName", UNSET)

        _ira_deposit_detail = d.pop("iraDepositDetail", UNSET)
        ira_deposit_detail: Union[Unset, DepositFundsInstructionIraDepositDetail]
        if isinstance(_ira_deposit_detail, Unset):
            ira_deposit_detail = UNSET
        else:
            ira_deposit_detail = DepositFundsInstructionIraDepositDetail.from_dict(_ira_deposit_detail)

        _recurring_instruction_detail = d.pop("recurringInstructionDetail", UNSET)
        recurring_instruction_detail: Union[Unset, RecurringInstructionDetail]
        if isinstance(_recurring_instruction_detail, Unset):
            recurring_instruction_detail = UNSET
        else:
            recurring_instruction_detail = RecurringInstructionDetail.from_dict(_recurring_instruction_detail)

        deposit_funds_instruction = cls(
            client_instruction_id=client_instruction_id,
            account_id=account_id,
            currency=currency,
            amount=amount,
            bank_instruction_method=bank_instruction_method,
            sending_institution=sending_institution,
            identifier=identifier,
            special_instruction=special_instruction,
            bank_instruction_name=bank_instruction_name,
            sender_institution_name=sender_institution_name,
            ira_deposit_detail=ira_deposit_detail,
            recurring_instruction_detail=recurring_instruction_detail,
        )

        deposit_funds_instruction.additional_properties = d
        return deposit_funds_instruction

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
