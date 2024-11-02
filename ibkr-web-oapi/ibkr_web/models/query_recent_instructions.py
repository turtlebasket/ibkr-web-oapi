from typing import TYPE_CHECKING, Any, Dict, List, Type, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

if TYPE_CHECKING:
    from ..models.query_recent_instructions_transaction_history import QueryRecentInstructionsTransactionHistory


T = TypeVar("T", bound="QueryRecentInstructions")


@_attrs_define
class QueryRecentInstructions:
    """
    Attributes:
        client_instruction_id (float):  Example: 1012983.
        account_id (str):  Example: U32343.
        transaction_history (QueryRecentInstructionsTransactionHistory):
    """

    client_instruction_id: float
    account_id: str
    transaction_history: "QueryRecentInstructionsTransactionHistory"
    additional_properties: Dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> Dict[str, Any]:
        client_instruction_id = self.client_instruction_id

        account_id = self.account_id

        transaction_history = self.transaction_history.to_dict()

        field_dict: Dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "clientInstructionId": client_instruction_id,
                "accountId": account_id,
                "transactionHistory": transaction_history,
            }
        )

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        from ..models.query_recent_instructions_transaction_history import QueryRecentInstructionsTransactionHistory

        d = src_dict.copy()
        client_instruction_id = d.pop("clientInstructionId")

        account_id = d.pop("accountId")

        transaction_history = QueryRecentInstructionsTransactionHistory.from_dict(d.pop("transactionHistory"))

        query_recent_instructions = cls(
            client_instruction_id=client_instruction_id,
            account_id=account_id,
            transaction_history=transaction_history,
        )

        query_recent_instructions.additional_properties = d
        return query_recent_instructions

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
