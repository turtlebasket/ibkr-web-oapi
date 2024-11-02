import datetime
from typing import TYPE_CHECKING, Any, Dict, List, Type, TypeVar, Union

from attrs import define as _attrs_define
from attrs import field as _attrs_field
from dateutil.parser import isoparse

from ..models.recurring_transaction_currency import RecurringTransactionCurrency
from ..models.recurring_transaction_frequency import RecurringTransactionFrequency
from ..models.recurring_transaction_method import RecurringTransactionMethod
from ..models.recurring_transaction_type import RecurringTransactionType
from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.ach_instruction import ACHInstruction
    from ..models.ira_withdrawal_details import IRAWithdrawalDetails


T = TypeVar("T", bound="RecurringTransaction")


@_attrs_define
class RecurringTransaction:
    """
    Attributes:
        ach_instruction (Union[Unset, ACHInstruction]):
        ira_withdrawal_details (Union[Unset, IRAWithdrawalDetails]):
        type (Union[Unset, RecurringTransactionType]):
        method (Union[Unset, RecurringTransactionMethod]):
        instruction (Union[Unset, str]):
        frequency (Union[Unset, RecurringTransactionFrequency]):
        start_date (Union[Unset, datetime.date]):
        end_date (Union[Unset, datetime.date]):
        name (Union[Unset, str]):
        amount (Union[Unset, float]):
        currency (Union[Unset, RecurringTransactionCurrency]):
        ib_account (Union[Unset, str]):
    """

    ach_instruction: Union[Unset, "ACHInstruction"] = UNSET
    ira_withdrawal_details: Union[Unset, "IRAWithdrawalDetails"] = UNSET
    type: Union[Unset, RecurringTransactionType] = UNSET
    method: Union[Unset, RecurringTransactionMethod] = UNSET
    instruction: Union[Unset, str] = UNSET
    frequency: Union[Unset, RecurringTransactionFrequency] = UNSET
    start_date: Union[Unset, datetime.date] = UNSET
    end_date: Union[Unset, datetime.date] = UNSET
    name: Union[Unset, str] = UNSET
    amount: Union[Unset, float] = UNSET
    currency: Union[Unset, RecurringTransactionCurrency] = UNSET
    ib_account: Union[Unset, str] = UNSET
    additional_properties: Dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> Dict[str, Any]:
        ach_instruction: Union[Unset, Dict[str, Any]] = UNSET
        if not isinstance(self.ach_instruction, Unset):
            ach_instruction = self.ach_instruction.to_dict()

        ira_withdrawal_details: Union[Unset, Dict[str, Any]] = UNSET
        if not isinstance(self.ira_withdrawal_details, Unset):
            ira_withdrawal_details = self.ira_withdrawal_details.to_dict()

        type: Union[Unset, str] = UNSET
        if not isinstance(self.type, Unset):
            type = self.type.value

        method: Union[Unset, str] = UNSET
        if not isinstance(self.method, Unset):
            method = self.method.value

        instruction = self.instruction

        frequency: Union[Unset, str] = UNSET
        if not isinstance(self.frequency, Unset):
            frequency = self.frequency.value

        start_date: Union[Unset, str] = UNSET
        if not isinstance(self.start_date, Unset):
            start_date = self.start_date.isoformat()

        end_date: Union[Unset, str] = UNSET
        if not isinstance(self.end_date, Unset):
            end_date = self.end_date.isoformat()

        name = self.name

        amount = self.amount

        currency: Union[Unset, str] = UNSET
        if not isinstance(self.currency, Unset):
            currency = self.currency.value

        ib_account = self.ib_account

        field_dict: Dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if ach_instruction is not UNSET:
            field_dict["achInstruction"] = ach_instruction
        if ira_withdrawal_details is not UNSET:
            field_dict["iraWithdrawalDetails"] = ira_withdrawal_details
        if type is not UNSET:
            field_dict["type"] = type
        if method is not UNSET:
            field_dict["method"] = method
        if instruction is not UNSET:
            field_dict["instruction"] = instruction
        if frequency is not UNSET:
            field_dict["frequency"] = frequency
        if start_date is not UNSET:
            field_dict["startDate"] = start_date
        if end_date is not UNSET:
            field_dict["endDate"] = end_date
        if name is not UNSET:
            field_dict["name"] = name
        if amount is not UNSET:
            field_dict["amount"] = amount
        if currency is not UNSET:
            field_dict["currency"] = currency
        if ib_account is not UNSET:
            field_dict["ibAccount"] = ib_account

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        from ..models.ach_instruction import ACHInstruction
        from ..models.ira_withdrawal_details import IRAWithdrawalDetails

        d = src_dict.copy()
        _ach_instruction = d.pop("achInstruction", UNSET)
        ach_instruction: Union[Unset, ACHInstruction]
        if isinstance(_ach_instruction, Unset):
            ach_instruction = UNSET
        else:
            ach_instruction = ACHInstruction.from_dict(_ach_instruction)

        _ira_withdrawal_details = d.pop("iraWithdrawalDetails", UNSET)
        ira_withdrawal_details: Union[Unset, IRAWithdrawalDetails]
        if isinstance(_ira_withdrawal_details, Unset):
            ira_withdrawal_details = UNSET
        else:
            ira_withdrawal_details = IRAWithdrawalDetails.from_dict(_ira_withdrawal_details)

        _type = d.pop("type", UNSET)
        type: Union[Unset, RecurringTransactionType]
        if isinstance(_type, Unset):
            type = UNSET
        else:
            type = RecurringTransactionType(_type)

        _method = d.pop("method", UNSET)
        method: Union[Unset, RecurringTransactionMethod]
        if isinstance(_method, Unset):
            method = UNSET
        else:
            method = RecurringTransactionMethod(_method)

        instruction = d.pop("instruction", UNSET)

        _frequency = d.pop("frequency", UNSET)
        frequency: Union[Unset, RecurringTransactionFrequency]
        if isinstance(_frequency, Unset):
            frequency = UNSET
        else:
            frequency = RecurringTransactionFrequency(_frequency)

        _start_date = d.pop("startDate", UNSET)
        start_date: Union[Unset, datetime.date]
        if isinstance(_start_date, Unset):
            start_date = UNSET
        else:
            start_date = isoparse(_start_date).date()

        _end_date = d.pop("endDate", UNSET)
        end_date: Union[Unset, datetime.date]
        if isinstance(_end_date, Unset):
            end_date = UNSET
        else:
            end_date = isoparse(_end_date).date()

        name = d.pop("name", UNSET)

        amount = d.pop("amount", UNSET)

        _currency = d.pop("currency", UNSET)
        currency: Union[Unset, RecurringTransactionCurrency]
        if isinstance(_currency, Unset):
            currency = UNSET
        else:
            currency = RecurringTransactionCurrency(_currency)

        ib_account = d.pop("ibAccount", UNSET)

        recurring_transaction = cls(
            ach_instruction=ach_instruction,
            ira_withdrawal_details=ira_withdrawal_details,
            type=type,
            method=method,
            instruction=instruction,
            frequency=frequency,
            start_date=start_date,
            end_date=end_date,
            name=name,
            amount=amount,
            currency=currency,
            ib_account=ib_account,
        )

        recurring_transaction.additional_properties = d
        return recurring_transaction

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
