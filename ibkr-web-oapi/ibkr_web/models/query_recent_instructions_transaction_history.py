from typing import Any, Dict, List, Type, TypeVar, Union

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

T = TypeVar("T", bound="QueryRecentInstructionsTransactionHistory")


@_attrs_define
class QueryRecentInstructionsTransactionHistory:
    """
    Attributes:
        days_to_go_back (float):  Example: 5.
        transaction_type (Union[Unset, str]):  Example: INTERNAL_CASH_TRANSFER.
    """

    days_to_go_back: float
    transaction_type: Union[Unset, str] = UNSET
    additional_properties: Dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> Dict[str, Any]:
        days_to_go_back = self.days_to_go_back

        transaction_type = self.transaction_type

        field_dict: Dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "daysToGoBack": days_to_go_back,
            }
        )
        if transaction_type is not UNSET:
            field_dict["transactionType"] = transaction_type

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        d = src_dict.copy()
        days_to_go_back = d.pop("daysToGoBack")

        transaction_type = d.pop("transactionType", UNSET)

        query_recent_instructions_transaction_history = cls(
            days_to_go_back=days_to_go_back,
            transaction_type=transaction_type,
        )

        query_recent_instructions_transaction_history.additional_properties = d
        return query_recent_instructions_transaction_history

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
