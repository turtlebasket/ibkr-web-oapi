from typing import TYPE_CHECKING, Any, Dict, List, Type, TypeVar, Union

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.portfolio_allocations_asset_class_long import PortfolioAllocationsAssetClassLong
    from ..models.portfolio_allocations_asset_class_short import PortfolioAllocationsAssetClassShort


T = TypeVar("T", bound="PortfolioAllocationsAssetClass")


@_attrs_define
class PortfolioAllocationsAssetClass:
    """Object containing values of positions sorted by long/short and asset class.

    Attributes:
        long (Union[Unset, PortfolioAllocationsAssetClassLong]): Object containing value of long positions in the
            account aggregated by asset class.
        short (Union[Unset, PortfolioAllocationsAssetClassShort]): Object containing value of short positions in the
            account aggregated by asset class.
    """

    long: Union[Unset, "PortfolioAllocationsAssetClassLong"] = UNSET
    short: Union[Unset, "PortfolioAllocationsAssetClassShort"] = UNSET
    additional_properties: Dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> Dict[str, Any]:
        long: Union[Unset, Dict[str, Any]] = UNSET
        if not isinstance(self.long, Unset):
            long = self.long.to_dict()

        short: Union[Unset, Dict[str, Any]] = UNSET
        if not isinstance(self.short, Unset):
            short = self.short.to_dict()

        field_dict: Dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if long is not UNSET:
            field_dict["long"] = long
        if short is not UNSET:
            field_dict["short"] = short

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        from ..models.portfolio_allocations_asset_class_long import PortfolioAllocationsAssetClassLong
        from ..models.portfolio_allocations_asset_class_short import PortfolioAllocationsAssetClassShort

        d = src_dict.copy()
        _long = d.pop("long", UNSET)
        long: Union[Unset, PortfolioAllocationsAssetClassLong]
        if isinstance(_long, Unset):
            long = UNSET
        else:
            long = PortfolioAllocationsAssetClassLong.from_dict(_long)

        _short = d.pop("short", UNSET)
        short: Union[Unset, PortfolioAllocationsAssetClassShort]
        if isinstance(_short, Unset):
            short = UNSET
        else:
            short = PortfolioAllocationsAssetClassShort.from_dict(_short)

        portfolio_allocations_asset_class = cls(
            long=long,
            short=short,
        )

        portfolio_allocations_asset_class.additional_properties = d
        return portfolio_allocations_asset_class

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
