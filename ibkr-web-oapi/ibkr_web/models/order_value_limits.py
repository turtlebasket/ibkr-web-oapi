from typing import Any, Dict, List, Type, TypeVar, Union

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

T = TypeVar("T", bound="OrderValueLimits")


@_attrs_define
class OrderValueLimits:
    """
    Attributes:
        max_order_value (Union[Unset, float]):
        max_gross_value (Union[Unset, float]):
        max_net_value (Union[Unset, float]):
        net_contract_limit (Union[Unset, float]):
    """

    max_order_value: Union[Unset, float] = UNSET
    max_gross_value: Union[Unset, float] = UNSET
    max_net_value: Union[Unset, float] = UNSET
    net_contract_limit: Union[Unset, float] = UNSET
    additional_properties: Dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> Dict[str, Any]:
        max_order_value = self.max_order_value

        max_gross_value = self.max_gross_value

        max_net_value = self.max_net_value

        net_contract_limit = self.net_contract_limit

        field_dict: Dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if max_order_value is not UNSET:
            field_dict["maxOrderValue"] = max_order_value
        if max_gross_value is not UNSET:
            field_dict["maxGrossValue"] = max_gross_value
        if max_net_value is not UNSET:
            field_dict["maxNetValue"] = max_net_value
        if net_contract_limit is not UNSET:
            field_dict["netContractLimit"] = net_contract_limit

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        d = src_dict.copy()
        max_order_value = d.pop("maxOrderValue", UNSET)

        max_gross_value = d.pop("maxGrossValue", UNSET)

        max_net_value = d.pop("maxNetValue", UNSET)

        net_contract_limit = d.pop("netContractLimit", UNSET)

        order_value_limits = cls(
            max_order_value=max_order_value,
            max_gross_value=max_gross_value,
            max_net_value=max_net_value,
            net_contract_limit=net_contract_limit,
        )

        order_value_limits.additional_properties = d
        return order_value_limits

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
