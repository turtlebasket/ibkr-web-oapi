from typing import Any, Dict, List, Type, TypeVar, Union

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..models.exchange_access_asset_class import ExchangeAccessAssetClass
from ..models.exchange_access_exchange import ExchangeAccessExchange
from ..types import UNSET, Unset

T = TypeVar("T", bound="ExchangeAccess")


@_attrs_define
class ExchangeAccess:
    """
    Attributes:
        asset_class (Union[Unset, ExchangeAccessAssetClass]):
        exchange (Union[Unset, ExchangeAccessExchange]):
    """

    asset_class: Union[Unset, ExchangeAccessAssetClass] = UNSET
    exchange: Union[Unset, ExchangeAccessExchange] = UNSET
    additional_properties: Dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> Dict[str, Any]:
        asset_class: Union[Unset, str] = UNSET
        if not isinstance(self.asset_class, Unset):
            asset_class = self.asset_class.value

        exchange: Union[Unset, str] = UNSET
        if not isinstance(self.exchange, Unset):
            exchange = self.exchange.value

        field_dict: Dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if asset_class is not UNSET:
            field_dict["assetClass"] = asset_class
        if exchange is not UNSET:
            field_dict["exchange"] = exchange

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        d = src_dict.copy()
        _asset_class = d.pop("assetClass", UNSET)
        asset_class: Union[Unset, ExchangeAccessAssetClass]
        if isinstance(_asset_class, Unset):
            asset_class = UNSET
        else:
            asset_class = ExchangeAccessAssetClass(_asset_class)

        _exchange = d.pop("exchange", UNSET)
        exchange: Union[Unset, ExchangeAccessExchange]
        if isinstance(_exchange, Unset):
            exchange = UNSET
        else:
            exchange = ExchangeAccessExchange(_exchange)

        exchange_access = cls(
            asset_class=asset_class,
            exchange=exchange,
        )

        exchange_access.additional_properties = d
        return exchange_access

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
