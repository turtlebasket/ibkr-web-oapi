from typing import Any, Dict, List, Type, TypeVar, Union

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

T = TypeVar("T", bound="QueryRecentRecurringEvents")


@_attrs_define
class QueryRecentRecurringEvents:
    """
    Attributes:
        client_instruction_id (float):  Example: 1012983.
        ib_reference_id (str):  Example: -343872793.
        number_of_transactions (Union[Unset, float]):  Example: 15.
    """

    client_instruction_id: float
    ib_reference_id: str
    number_of_transactions: Union[Unset, float] = UNSET
    additional_properties: Dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> Dict[str, Any]:
        client_instruction_id = self.client_instruction_id

        ib_reference_id = self.ib_reference_id

        number_of_transactions = self.number_of_transactions

        field_dict: Dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "clientInstructionId": client_instruction_id,
                "ibReferenceId": ib_reference_id,
            }
        )
        if number_of_transactions is not UNSET:
            field_dict["numberOfTransactions"] = number_of_transactions

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        d = src_dict.copy()
        client_instruction_id = d.pop("clientInstructionId")

        ib_reference_id = d.pop("ibReferenceId")

        number_of_transactions = d.pop("numberOfTransactions", UNSET)

        query_recent_recurring_events = cls(
            client_instruction_id=client_instruction_id,
            ib_reference_id=ib_reference_id,
            number_of_transactions=number_of_transactions,
        )

        query_recent_recurring_events.additional_properties = d
        return query_recent_recurring_events

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
