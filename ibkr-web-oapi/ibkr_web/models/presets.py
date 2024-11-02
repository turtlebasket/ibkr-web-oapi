from typing import Any, Dict, List, Type, TypeVar, Union

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..models.presets_default_method_for_all import PresetsDefaultMethodForAll
from ..types import UNSET, Unset

T = TypeVar("T", bound="Presets")


@_attrs_define
class Presets:
    """
    Attributes:
        group_auto_close_positions (Union[Unset, bool]): Determines if allocation groups should prioritize closing
            positions over equal distribution.
        default_method_for_all (Union[Unset, PresetsDefaultMethodForAll]): Interactive Brokers supports two forms of
            allocation methods. Allocation methods that have calculations completed by Interactive Brokers, and a set of
            allocation methods calculated by the user and then specified. IB-computed allocation methods:
              * `A` - Available Equity
              * `E` - Equal
              * `N` - Net Liquidation Value

            User-specified allocation methods:
              * `C` - Cash Quantity
              * `P` - Percentage
              * `R` - Ratios
              * `S` - Shares
        profiles_auto_close_positions (Union[Unset, bool]): Determines if allocation profiles should prioritize closing
            positions over equal distribution.
        strict_credit_check (Union[Unset, bool]): Determines if the system should always check user credit before
            beginning the order process every time, or only at the time of order placement and execution.
        group_proportional_allocation (Union[Unset, bool]): Determines if the system should keep allocation groups
            proportional for scaling.
    """

    group_auto_close_positions: Union[Unset, bool] = UNSET
    default_method_for_all: Union[Unset, PresetsDefaultMethodForAll] = UNSET
    profiles_auto_close_positions: Union[Unset, bool] = UNSET
    strict_credit_check: Union[Unset, bool] = UNSET
    group_proportional_allocation: Union[Unset, bool] = UNSET
    additional_properties: Dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> Dict[str, Any]:
        group_auto_close_positions = self.group_auto_close_positions

        default_method_for_all: Union[Unset, str] = UNSET
        if not isinstance(self.default_method_for_all, Unset):
            default_method_for_all = self.default_method_for_all.value

        profiles_auto_close_positions = self.profiles_auto_close_positions

        strict_credit_check = self.strict_credit_check

        group_proportional_allocation = self.group_proportional_allocation

        field_dict: Dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if group_auto_close_positions is not UNSET:
            field_dict["group_auto_close_positions"] = group_auto_close_positions
        if default_method_for_all is not UNSET:
            field_dict["default_method_for_all"] = default_method_for_all
        if profiles_auto_close_positions is not UNSET:
            field_dict["profiles_auto_close_positions"] = profiles_auto_close_positions
        if strict_credit_check is not UNSET:
            field_dict["strict_credit_check"] = strict_credit_check
        if group_proportional_allocation is not UNSET:
            field_dict["group_proportional_allocation"] = group_proportional_allocation

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        d = src_dict.copy()
        group_auto_close_positions = d.pop("group_auto_close_positions", UNSET)

        _default_method_for_all = d.pop("default_method_for_all", UNSET)
        default_method_for_all: Union[Unset, PresetsDefaultMethodForAll]
        if isinstance(_default_method_for_all, Unset):
            default_method_for_all = UNSET
        else:
            default_method_for_all = PresetsDefaultMethodForAll(_default_method_for_all)

        profiles_auto_close_positions = d.pop("profiles_auto_close_positions", UNSET)

        strict_credit_check = d.pop("strict_credit_check", UNSET)

        group_proportional_allocation = d.pop("group_proportional_allocation", UNSET)

        presets = cls(
            group_auto_close_positions=group_auto_close_positions,
            default_method_for_all=default_method_for_all,
            profiles_auto_close_positions=profiles_auto_close_positions,
            strict_credit_check=strict_credit_check,
            group_proportional_allocation=group_proportional_allocation,
        )

        presets.additional_properties = d
        return presets

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
