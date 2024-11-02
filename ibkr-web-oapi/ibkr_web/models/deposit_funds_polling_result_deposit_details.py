from typing import Any, Dict, List, Type, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

T = TypeVar("T", bound="DepositFundsPollingResultDepositDetails")


@_attrs_define
class DepositFundsPollingResultDepositDetails:
    """
    Attributes:
        amount (float):
        currency (str):
        when_available (str):
    """

    amount: float
    currency: str
    when_available: str
    additional_properties: Dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> Dict[str, Any]:
        amount = self.amount

        currency = self.currency

        when_available = self.when_available

        field_dict: Dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "amount": amount,
                "currency": currency,
                "whenAvailable": when_available,
            }
        )

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        d = src_dict.copy()
        amount = d.pop("amount")

        currency = d.pop("currency")

        when_available = d.pop("whenAvailable")

        deposit_funds_polling_result_deposit_details = cls(
            amount=amount,
            currency=currency,
            when_available=when_available,
        )

        deposit_funds_polling_result_deposit_details.additional_properties = d
        return deposit_funds_polling_result_deposit_details

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
