import datetime
from typing import TYPE_CHECKING, Any, Dict, List, Type, TypeVar, Union

from attrs import define as _attrs_define
from attrs import field as _attrs_field
from dateutil.parser import isoparse

from ..models.withdraw_funds_instruction_bank_instruction_method import WithdrawFundsInstructionBankInstructionMethod
from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.recurring_instruction_detail import RecurringInstructionDetail
    from ..models.withdraw_funds_instruction_ira_withdrawal_detail import WithdrawFundsInstructionIraWithdrawalDetail


T = TypeVar("T", bound="WithdrawFundsInstruction")


@_attrs_define
class WithdrawFundsInstruction:
    """
    Attributes:
        client_instruction_id (float):  Example: 1012983.
        account_id (str):  Example: U46377.
        currency (str):  Example: USD.
        amount (float):  Example: 100.
        bank_instruction_name (str):  Example: Instruction.
        bank_instruction_method (WithdrawFundsInstructionBankInstructionMethod):  Example: WIRE.
        date_time_to_occur (Union[Unset, datetime.datetime]):
        ira_withdrawal_detail (Union[Unset, WithdrawFundsInstructionIraWithdrawalDetail]):
        recurring_instruction_detail (Union[Unset, RecurringInstructionDetail]):
    """

    client_instruction_id: float
    account_id: str
    currency: str
    amount: float
    bank_instruction_name: str
    bank_instruction_method: WithdrawFundsInstructionBankInstructionMethod
    date_time_to_occur: Union[Unset, datetime.datetime] = UNSET
    ira_withdrawal_detail: Union[Unset, "WithdrawFundsInstructionIraWithdrawalDetail"] = UNSET
    recurring_instruction_detail: Union[Unset, "RecurringInstructionDetail"] = UNSET
    additional_properties: Dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> Dict[str, Any]:
        client_instruction_id = self.client_instruction_id

        account_id = self.account_id

        currency = self.currency

        amount = self.amount

        bank_instruction_name = self.bank_instruction_name

        bank_instruction_method = self.bank_instruction_method.value

        date_time_to_occur: Union[Unset, str] = UNSET
        if not isinstance(self.date_time_to_occur, Unset):
            date_time_to_occur = self.date_time_to_occur.isoformat()

        ira_withdrawal_detail: Union[Unset, Dict[str, Any]] = UNSET
        if not isinstance(self.ira_withdrawal_detail, Unset):
            ira_withdrawal_detail = self.ira_withdrawal_detail.to_dict()

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
                "bankInstructionName": bank_instruction_name,
                "bankInstructionMethod": bank_instruction_method,
            }
        )
        if date_time_to_occur is not UNSET:
            field_dict["dateTimeToOccur"] = date_time_to_occur
        if ira_withdrawal_detail is not UNSET:
            field_dict["iraWithdrawalDetail"] = ira_withdrawal_detail
        if recurring_instruction_detail is not UNSET:
            field_dict["recurringInstructionDetail"] = recurring_instruction_detail

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        from ..models.recurring_instruction_detail import RecurringInstructionDetail
        from ..models.withdraw_funds_instruction_ira_withdrawal_detail import (
            WithdrawFundsInstructionIraWithdrawalDetail,
        )

        d = src_dict.copy()
        client_instruction_id = d.pop("clientInstructionId")

        account_id = d.pop("accountId")

        currency = d.pop("currency")

        amount = d.pop("amount")

        bank_instruction_name = d.pop("bankInstructionName")

        bank_instruction_method = WithdrawFundsInstructionBankInstructionMethod(d.pop("bankInstructionMethod"))

        _date_time_to_occur = d.pop("dateTimeToOccur", UNSET)
        date_time_to_occur: Union[Unset, datetime.datetime]
        if isinstance(_date_time_to_occur, Unset):
            date_time_to_occur = UNSET
        else:
            date_time_to_occur = isoparse(_date_time_to_occur)

        _ira_withdrawal_detail = d.pop("iraWithdrawalDetail", UNSET)
        ira_withdrawal_detail: Union[Unset, WithdrawFundsInstructionIraWithdrawalDetail]
        if isinstance(_ira_withdrawal_detail, Unset):
            ira_withdrawal_detail = UNSET
        else:
            ira_withdrawal_detail = WithdrawFundsInstructionIraWithdrawalDetail.from_dict(_ira_withdrawal_detail)

        _recurring_instruction_detail = d.pop("recurringInstructionDetail", UNSET)
        recurring_instruction_detail: Union[Unset, RecurringInstructionDetail]
        if isinstance(_recurring_instruction_detail, Unset):
            recurring_instruction_detail = UNSET
        else:
            recurring_instruction_detail = RecurringInstructionDetail.from_dict(_recurring_instruction_detail)

        withdraw_funds_instruction = cls(
            client_instruction_id=client_instruction_id,
            account_id=account_id,
            currency=currency,
            amount=amount,
            bank_instruction_name=bank_instruction_name,
            bank_instruction_method=bank_instruction_method,
            date_time_to_occur=date_time_to_occur,
            ira_withdrawal_detail=ira_withdrawal_detail,
            recurring_instruction_detail=recurring_instruction_detail,
        )

        withdraw_funds_instruction.additional_properties = d
        return withdraw_funds_instruction

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
