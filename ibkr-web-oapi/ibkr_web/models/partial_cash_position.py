from typing import Any, Dict, List, Type, TypeVar, Union

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

T = TypeVar("T", bound="PartialCashPosition")


@_attrs_define
class PartialCashPosition:
    """
    Attributes:
        amount (Union[Unset, float]):
        margin_loan (Union[Unset, bool]):
        full_cash (Union[Unset, bool]):
    """

    amount: Union[Unset, float] = UNSET
    margin_loan: Union[Unset, bool] = UNSET
    full_cash: Union[Unset, bool] = UNSET
    additional_properties: Dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> Dict[str, Any]:
        amount = self.amount

        margin_loan = self.margin_loan

        full_cash = self.full_cash

        field_dict: Dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if amount is not UNSET:
            field_dict["amount"] = amount
        if margin_loan is not UNSET:
            field_dict["marginLoan"] = margin_loan
        if full_cash is not UNSET:
            field_dict["fullCash"] = full_cash

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        d = src_dict.copy()
        amount = d.pop("amount", UNSET)

        margin_loan = d.pop("marginLoan", UNSET)

        full_cash = d.pop("fullCash", UNSET)

        partial_cash_position = cls(
            amount=amount,
            margin_loan=margin_loan,
            full_cash=full_cash,
        )

        partial_cash_position.additional_properties = d
        return partial_cash_position

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
