from typing import Any, Dict, List, Type, TypeVar, Union

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

T = TypeVar("T", bound="EFPQuantityLimits")


@_attrs_define
class EFPQuantityLimits:
    """
    Attributes:
        max_nominal_efp_per_order (Union[Unset, int]):
        max_net_efp_trades (Union[Unset, int]):
        max_gross_efp_trades (Union[Unset, int]):
    """

    max_nominal_efp_per_order: Union[Unset, int] = UNSET
    max_net_efp_trades: Union[Unset, int] = UNSET
    max_gross_efp_trades: Union[Unset, int] = UNSET
    additional_properties: Dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> Dict[str, Any]:
        max_nominal_efp_per_order = self.max_nominal_efp_per_order

        max_net_efp_trades = self.max_net_efp_trades

        max_gross_efp_trades = self.max_gross_efp_trades

        field_dict: Dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if max_nominal_efp_per_order is not UNSET:
            field_dict["maxNominalEfpPerOrder"] = max_nominal_efp_per_order
        if max_net_efp_trades is not UNSET:
            field_dict["maxNetEfpTrades"] = max_net_efp_trades
        if max_gross_efp_trades is not UNSET:
            field_dict["maxGrossEfpTrades"] = max_gross_efp_trades

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        d = src_dict.copy()
        max_nominal_efp_per_order = d.pop("maxNominalEfpPerOrder", UNSET)

        max_net_efp_trades = d.pop("maxNetEfpTrades", UNSET)

        max_gross_efp_trades = d.pop("maxGrossEfpTrades", UNSET)

        efp_quantity_limits = cls(
            max_nominal_efp_per_order=max_nominal_efp_per_order,
            max_net_efp_trades=max_net_efp_trades,
            max_gross_efp_trades=max_gross_efp_trades,
        )

        efp_quantity_limits.additional_properties = d
        return efp_quantity_limits

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
