from typing import TYPE_CHECKING, Any, Dict, List, Type, TypeVar, Union

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.day_quantity_limit import DayQuantityLimit
    from ..models.efp_quantity_limits import EFPQuantityLimits
    from ..models.order_quantity_limit import OrderQuantityLimit
    from ..models.order_value_limits import OrderValueLimits


T = TypeVar("T", bound="TradingLimits")


@_attrs_define
class TradingLimits:
    """
    Attributes:
        order_value_limits (Union[Unset, OrderValueLimits]):
        efp_quantity_limits (Union[Unset, EFPQuantityLimits]):
        order_quantity_limits (Union[Unset, List['OrderQuantityLimit']]):
        day_quantity_limits (Union[Unset, List['DayQuantityLimit']]):
    """

    order_value_limits: Union[Unset, "OrderValueLimits"] = UNSET
    efp_quantity_limits: Union[Unset, "EFPQuantityLimits"] = UNSET
    order_quantity_limits: Union[Unset, List["OrderQuantityLimit"]] = UNSET
    day_quantity_limits: Union[Unset, List["DayQuantityLimit"]] = UNSET
    additional_properties: Dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> Dict[str, Any]:
        order_value_limits: Union[Unset, Dict[str, Any]] = UNSET
        if not isinstance(self.order_value_limits, Unset):
            order_value_limits = self.order_value_limits.to_dict()

        efp_quantity_limits: Union[Unset, Dict[str, Any]] = UNSET
        if not isinstance(self.efp_quantity_limits, Unset):
            efp_quantity_limits = self.efp_quantity_limits.to_dict()

        order_quantity_limits: Union[Unset, List[Dict[str, Any]]] = UNSET
        if not isinstance(self.order_quantity_limits, Unset):
            order_quantity_limits = []
            for order_quantity_limits_item_data in self.order_quantity_limits:
                order_quantity_limits_item = order_quantity_limits_item_data.to_dict()
                order_quantity_limits.append(order_quantity_limits_item)

        day_quantity_limits: Union[Unset, List[Dict[str, Any]]] = UNSET
        if not isinstance(self.day_quantity_limits, Unset):
            day_quantity_limits = []
            for day_quantity_limits_item_data in self.day_quantity_limits:
                day_quantity_limits_item = day_quantity_limits_item_data.to_dict()
                day_quantity_limits.append(day_quantity_limits_item)

        field_dict: Dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if order_value_limits is not UNSET:
            field_dict["orderValueLimits"] = order_value_limits
        if efp_quantity_limits is not UNSET:
            field_dict["efpQuantityLimits"] = efp_quantity_limits
        if order_quantity_limits is not UNSET:
            field_dict["orderQuantityLimits"] = order_quantity_limits
        if day_quantity_limits is not UNSET:
            field_dict["dayQuantityLimits"] = day_quantity_limits

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        from ..models.day_quantity_limit import DayQuantityLimit
        from ..models.efp_quantity_limits import EFPQuantityLimits
        from ..models.order_quantity_limit import OrderQuantityLimit
        from ..models.order_value_limits import OrderValueLimits

        d = src_dict.copy()
        _order_value_limits = d.pop("orderValueLimits", UNSET)
        order_value_limits: Union[Unset, OrderValueLimits]
        if isinstance(_order_value_limits, Unset):
            order_value_limits = UNSET
        else:
            order_value_limits = OrderValueLimits.from_dict(_order_value_limits)

        _efp_quantity_limits = d.pop("efpQuantityLimits", UNSET)
        efp_quantity_limits: Union[Unset, EFPQuantityLimits]
        if isinstance(_efp_quantity_limits, Unset):
            efp_quantity_limits = UNSET
        else:
            efp_quantity_limits = EFPQuantityLimits.from_dict(_efp_quantity_limits)

        order_quantity_limits = []
        _order_quantity_limits = d.pop("orderQuantityLimits", UNSET)
        for order_quantity_limits_item_data in _order_quantity_limits or []:
            order_quantity_limits_item = OrderQuantityLimit.from_dict(order_quantity_limits_item_data)

            order_quantity_limits.append(order_quantity_limits_item)

        day_quantity_limits = []
        _day_quantity_limits = d.pop("dayQuantityLimits", UNSET)
        for day_quantity_limits_item_data in _day_quantity_limits or []:
            day_quantity_limits_item = DayQuantityLimit.from_dict(day_quantity_limits_item_data)

            day_quantity_limits.append(day_quantity_limits_item)

        trading_limits = cls(
            order_value_limits=order_value_limits,
            efp_quantity_limits=efp_quantity_limits,
            order_quantity_limits=order_quantity_limits,
            day_quantity_limits=day_quantity_limits,
        )

        trading_limits.additional_properties = d
        return trading_limits

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
