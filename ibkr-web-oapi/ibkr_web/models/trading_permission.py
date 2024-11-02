from typing import Any, Dict, List, Type, TypeVar, Union

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..models.trading_permission_asset_class import TradingPermissionAssetClass
from ..models.trading_permission_country import TradingPermissionCountry
from ..models.trading_permission_product import TradingPermissionProduct
from ..types import UNSET, Unset

T = TypeVar("T", bound="TradingPermission")


@_attrs_define
class TradingPermission:
    """
    Attributes:
        asset_class (Union[Unset, TradingPermissionAssetClass]):
        exchange_group (Union[Unset, str]):
        country (Union[Unset, TradingPermissionCountry]):
        product (Union[Unset, TradingPermissionProduct]):
    """

    asset_class: Union[Unset, TradingPermissionAssetClass] = UNSET
    exchange_group: Union[Unset, str] = UNSET
    country: Union[Unset, TradingPermissionCountry] = UNSET
    product: Union[Unset, TradingPermissionProduct] = UNSET
    additional_properties: Dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> Dict[str, Any]:
        asset_class: Union[Unset, str] = UNSET
        if not isinstance(self.asset_class, Unset):
            asset_class = self.asset_class.value

        exchange_group = self.exchange_group

        country: Union[Unset, str] = UNSET
        if not isinstance(self.country, Unset):
            country = self.country.value

        product: Union[Unset, str] = UNSET
        if not isinstance(self.product, Unset):
            product = self.product.value

        field_dict: Dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if asset_class is not UNSET:
            field_dict["assetClass"] = asset_class
        if exchange_group is not UNSET:
            field_dict["exchangeGroup"] = exchange_group
        if country is not UNSET:
            field_dict["country"] = country
        if product is not UNSET:
            field_dict["product"] = product

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        d = src_dict.copy()
        _asset_class = d.pop("assetClass", UNSET)
        asset_class: Union[Unset, TradingPermissionAssetClass]
        if isinstance(_asset_class, Unset):
            asset_class = UNSET
        else:
            asset_class = TradingPermissionAssetClass(_asset_class)

        exchange_group = d.pop("exchangeGroup", UNSET)

        _country = d.pop("country", UNSET)
        country: Union[Unset, TradingPermissionCountry]
        if isinstance(_country, Unset):
            country = UNSET
        else:
            country = TradingPermissionCountry(_country)

        _product = d.pop("product", UNSET)
        product: Union[Unset, TradingPermissionProduct]
        if isinstance(_product, Unset):
            product = UNSET
        else:
            product = TradingPermissionProduct(_product)

        trading_permission = cls(
            asset_class=asset_class,
            exchange_group=exchange_group,
            country=country,
            product=product,
        )

        trading_permission.additional_properties = d
        return trading_permission

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
