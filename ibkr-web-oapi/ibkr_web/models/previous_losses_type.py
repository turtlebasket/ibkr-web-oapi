from typing import Any, Dict, List, Type, TypeVar, Union

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

T = TypeVar("T", bound="PreviousLossesType")


@_attrs_define
class PreviousLossesType:
    """
    Attributes:
        loss (Union[Unset, int]):
        quarter (Union[Unset, int]):
        year (Union[Unset, int]):
        currency (Union[Unset, str]):
    """

    loss: Union[Unset, int] = UNSET
    quarter: Union[Unset, int] = UNSET
    year: Union[Unset, int] = UNSET
    currency: Union[Unset, str] = UNSET
    additional_properties: Dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> Dict[str, Any]:
        loss = self.loss

        quarter = self.quarter

        year = self.year

        currency = self.currency

        field_dict: Dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if loss is not UNSET:
            field_dict["loss"] = loss
        if quarter is not UNSET:
            field_dict["quarter"] = quarter
        if year is not UNSET:
            field_dict["year"] = year
        if currency is not UNSET:
            field_dict["currency"] = currency

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        d = src_dict.copy()
        loss = d.pop("loss", UNSET)

        quarter = d.pop("quarter", UNSET)

        year = d.pop("year", UNSET)

        currency = d.pop("currency", UNSET)

        previous_losses_type = cls(
            loss=loss,
            quarter=quarter,
            year=year,
            currency=currency,
        )

        previous_losses_type.additional_properties = d
        return previous_losses_type

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
