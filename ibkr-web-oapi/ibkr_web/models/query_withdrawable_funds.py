from typing import Any, Dict, List, Type, TypeVar, Union

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

T = TypeVar("T", bound="QueryWithdrawableFunds")


@_attrs_define
class QueryWithdrawableFunds:
    """
    Attributes:
        bank_routing_number (Union[Unset, str]):  Example: 122199983.
        bank_client_account_number (Union[Unset, str]):  Example: 9876543210.
    """

    bank_routing_number: Union[Unset, str] = UNSET
    bank_client_account_number: Union[Unset, str] = UNSET
    additional_properties: Dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> Dict[str, Any]:
        bank_routing_number = self.bank_routing_number

        bank_client_account_number = self.bank_client_account_number

        field_dict: Dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if bank_routing_number is not UNSET:
            field_dict["bankRoutingNumber"] = bank_routing_number
        if bank_client_account_number is not UNSET:
            field_dict["bankClientAccountNumber"] = bank_client_account_number

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        d = src_dict.copy()
        bank_routing_number = d.pop("bankRoutingNumber", UNSET)

        bank_client_account_number = d.pop("bankClientAccountNumber", UNSET)

        query_withdrawable_funds = cls(
            bank_routing_number=bank_routing_number,
            bank_client_account_number=bank_client_account_number,
        )

        query_withdrawable_funds.additional_properties = d
        return query_withdrawable_funds

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
