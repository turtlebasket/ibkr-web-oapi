from typing import Any, Dict, List, Type, TypeVar, Union

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..models.order_quantity_limit_asset import OrderQuantityLimitAsset
from ..types import UNSET, Unset

T = TypeVar("T", bound="OrderQuantityLimit")


@_attrs_define
class OrderQuantityLimit:
    """
    Attributes:
        asset (Union[Unset, OrderQuantityLimitAsset]):
        quantity (Union[Unset, int]):
    """

    asset: Union[Unset, OrderQuantityLimitAsset] = UNSET
    quantity: Union[Unset, int] = UNSET
    additional_properties: Dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> Dict[str, Any]:
        asset: Union[Unset, str] = UNSET
        if not isinstance(self.asset, Unset):
            asset = self.asset.value

        quantity = self.quantity

        field_dict: Dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if asset is not UNSET:
            field_dict["asset"] = asset
        if quantity is not UNSET:
            field_dict["quantity"] = quantity

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        d = src_dict.copy()
        _asset = d.pop("asset", UNSET)
        asset: Union[Unset, OrderQuantityLimitAsset]
        if isinstance(_asset, Unset):
            asset = UNSET
        else:
            asset = OrderQuantityLimitAsset(_asset)

        quantity = d.pop("quantity", UNSET)

        order_quantity_limit = cls(
            asset=asset,
            quantity=quantity,
        )

        order_quantity_limit.additional_properties = d
        return order_quantity_limit

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
