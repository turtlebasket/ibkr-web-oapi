from typing import TYPE_CHECKING, Any, Dict, List, Type, TypeVar, Union

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.live_orders_response_orders_item import LiveOrdersResponseOrdersItem


T = TypeVar("T", bound="LiveOrdersResponse")


@_attrs_define
class LiveOrdersResponse:
    """
    Attributes:
        orders (Union[Unset, List['LiveOrdersResponseOrdersItem']]): Array of orders that are currently working, or were
            filled/cancelled in the current brokerage session.
        snapshot (Union[Unset, bool]): Whether the response is a snapshot.
    """

    orders: Union[Unset, List["LiveOrdersResponseOrdersItem"]] = UNSET
    snapshot: Union[Unset, bool] = UNSET
    additional_properties: Dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> Dict[str, Any]:
        orders: Union[Unset, List[Dict[str, Any]]] = UNSET
        if not isinstance(self.orders, Unset):
            orders = []
            for orders_item_data in self.orders:
                orders_item = orders_item_data.to_dict()
                orders.append(orders_item)

        snapshot = self.snapshot

        field_dict: Dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if orders is not UNSET:
            field_dict["orders"] = orders
        if snapshot is not UNSET:
            field_dict["snapshot"] = snapshot

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        from ..models.live_orders_response_orders_item import LiveOrdersResponseOrdersItem

        d = src_dict.copy()
        orders = []
        _orders = d.pop("orders", UNSET)
        for orders_item_data in _orders or []:
            orders_item = LiveOrdersResponseOrdersItem.from_dict(orders_item_data)

            orders.append(orders_item)

        snapshot = d.pop("snapshot", UNSET)

        live_orders_response = cls(
            orders=orders,
            snapshot=snapshot,
        )

        live_orders_response.additional_properties = d
        return live_orders_response

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
