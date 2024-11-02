from typing import Any, Dict, List, Type, TypeVar, Union

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

T = TypeVar("T", bound="PortfolioSummaryNetliquidationS")


@_attrs_define
class PortfolioSummaryNetliquidationS:
    """
    Attributes:
        amount (Union[Unset, float]): Numerical data for the associated key.
        currency (Union[Unset, float]): The currency in which the value of the 'amount' field is denominated.
        is_null (Union[Unset, bool]): Indicates whether the associated key's value does not exist, as opposed to a value
            of zero.
        severity (Union[Unset, int]): severity
        timestamp (Union[Unset, int]): Unix epoch timestamp of returned data in milliseconds.
        value (Union[Unset, str]): String and boolean (non-numerical) data for the associated key.
    """

    amount: Union[Unset, float] = UNSET
    currency: Union[Unset, float] = UNSET
    is_null: Union[Unset, bool] = UNSET
    severity: Union[Unset, int] = UNSET
    timestamp: Union[Unset, int] = UNSET
    value: Union[Unset, str] = UNSET
    additional_properties: Dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> Dict[str, Any]:
        amount = self.amount

        currency = self.currency

        is_null = self.is_null

        severity = self.severity

        timestamp = self.timestamp

        value = self.value

        field_dict: Dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if amount is not UNSET:
            field_dict["amount"] = amount
        if currency is not UNSET:
            field_dict["currency"] = currency
        if is_null is not UNSET:
            field_dict["isNull"] = is_null
        if severity is not UNSET:
            field_dict["severity"] = severity
        if timestamp is not UNSET:
            field_dict["timestamp"] = timestamp
        if value is not UNSET:
            field_dict["value"] = value

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        d = src_dict.copy()
        amount = d.pop("amount", UNSET)

        currency = d.pop("currency", UNSET)

        is_null = d.pop("isNull", UNSET)

        severity = d.pop("severity", UNSET)

        timestamp = d.pop("timestamp", UNSET)

        value = d.pop("value", UNSET)

        portfolio_summary_netliquidation_s = cls(
            amount=amount,
            currency=currency,
            is_null=is_null,
            severity=severity,
            timestamp=timestamp,
            value=value,
        )

        portfolio_summary_netliquidation_s.additional_properties = d
        return portfolio_summary_netliquidation_s

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
