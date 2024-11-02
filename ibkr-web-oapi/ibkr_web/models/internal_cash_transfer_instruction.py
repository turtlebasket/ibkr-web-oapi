import datetime
from typing import Any, Dict, List, Type, TypeVar, Union

from attrs import define as _attrs_define
from attrs import field as _attrs_field
from dateutil.parser import isoparse

from ..types import UNSET, Unset

T = TypeVar("T", bound="InternalCashTransferInstruction")


@_attrs_define
class InternalCashTransferInstruction:
    """
    Attributes:
        client_instruction_id (float):  Example: 1012983.
        source_account_id (str):  Example: U46377.
        target_account_id (str):  Example: U15667.
        amount (float):  Example: 123.
        currency (str):  Example: GBP.
        date_time_to_occur (Union[Unset, datetime.datetime]):
    """

    client_instruction_id: float
    source_account_id: str
    target_account_id: str
    amount: float
    currency: str
    date_time_to_occur: Union[Unset, datetime.datetime] = UNSET
    additional_properties: Dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> Dict[str, Any]:
        client_instruction_id = self.client_instruction_id

        source_account_id = self.source_account_id

        target_account_id = self.target_account_id

        amount = self.amount

        currency = self.currency

        date_time_to_occur: Union[Unset, str] = UNSET
        if not isinstance(self.date_time_to_occur, Unset):
            date_time_to_occur = self.date_time_to_occur.isoformat()

        field_dict: Dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "clientInstructionId": client_instruction_id,
                "sourceAccountId": source_account_id,
                "targetAccountId": target_account_id,
                "amount": amount,
                "currency": currency,
            }
        )
        if date_time_to_occur is not UNSET:
            field_dict["dateTimeToOccur"] = date_time_to_occur

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        d = src_dict.copy()
        client_instruction_id = d.pop("clientInstructionId")

        source_account_id = d.pop("sourceAccountId")

        target_account_id = d.pop("targetAccountId")

        amount = d.pop("amount")

        currency = d.pop("currency")

        _date_time_to_occur = d.pop("dateTimeToOccur", UNSET)
        date_time_to_occur: Union[Unset, datetime.datetime]
        if isinstance(_date_time_to_occur, Unset):
            date_time_to_occur = UNSET
        else:
            date_time_to_occur = isoparse(_date_time_to_occur)

        internal_cash_transfer_instruction = cls(
            client_instruction_id=client_instruction_id,
            source_account_id=source_account_id,
            target_account_id=target_account_id,
            amount=amount,
            currency=currency,
            date_time_to_occur=date_time_to_occur,
        )

        internal_cash_transfer_instruction.additional_properties = d
        return internal_cash_transfer_instruction

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
