from typing import Any, Dict, List, Type, TypeVar, Union

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

T = TypeVar("T", bound="HighWaterMarkConfigurationType")


@_attrs_define
class HighWaterMarkConfigurationType:
    """
    Attributes:
        number_of_periods (Union[Unset, int]):
        prorate_for_withdrawals (Union[Unset, bool]):
    """

    number_of_periods: Union[Unset, int] = UNSET
    prorate_for_withdrawals: Union[Unset, bool] = UNSET
    additional_properties: Dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> Dict[str, Any]:
        number_of_periods = self.number_of_periods

        prorate_for_withdrawals = self.prorate_for_withdrawals

        field_dict: Dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if number_of_periods is not UNSET:
            field_dict["numberOfPeriods"] = number_of_periods
        if prorate_for_withdrawals is not UNSET:
            field_dict["prorateForWithdrawals"] = prorate_for_withdrawals

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        d = src_dict.copy()
        number_of_periods = d.pop("numberOfPeriods", UNSET)

        prorate_for_withdrawals = d.pop("prorateForWithdrawals", UNSET)

        high_water_mark_configuration_type = cls(
            number_of_periods=number_of_periods,
            prorate_for_withdrawals=prorate_for_withdrawals,
        )

        high_water_mark_configuration_type.additional_properties = d
        return high_water_mark_configuration_type

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
