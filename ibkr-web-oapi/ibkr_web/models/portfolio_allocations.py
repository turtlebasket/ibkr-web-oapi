from typing import TYPE_CHECKING, Any, Dict, List, Type, TypeVar, Union

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.portfolio_allocations_asset_class import PortfolioAllocationsAssetClass
    from ..models.portfolio_allocations_group import PortfolioAllocationsGroup
    from ..models.portfolio_allocations_sector import PortfolioAllocationsSector


T = TypeVar("T", bound="PortfolioAllocations")


@_attrs_define
class PortfolioAllocations:
    """
    Attributes:
        asset_class (Union[Unset, PortfolioAllocationsAssetClass]): Object containing values of positions sorted by
            long/short and asset class.
        group (Union[Unset, PortfolioAllocationsGroup]): Object containing values of positions sorted by long/short and
            Sector Group.
        sector (Union[Unset, PortfolioAllocationsSector]): Object containing values of positions sorted by long/short
            and Sector.
    """

    asset_class: Union[Unset, "PortfolioAllocationsAssetClass"] = UNSET
    group: Union[Unset, "PortfolioAllocationsGroup"] = UNSET
    sector: Union[Unset, "PortfolioAllocationsSector"] = UNSET
    additional_properties: Dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> Dict[str, Any]:
        asset_class: Union[Unset, Dict[str, Any]] = UNSET
        if not isinstance(self.asset_class, Unset):
            asset_class = self.asset_class.to_dict()

        group: Union[Unset, Dict[str, Any]] = UNSET
        if not isinstance(self.group, Unset):
            group = self.group.to_dict()

        sector: Union[Unset, Dict[str, Any]] = UNSET
        if not isinstance(self.sector, Unset):
            sector = self.sector.to_dict()

        field_dict: Dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if asset_class is not UNSET:
            field_dict["assetClass"] = asset_class
        if group is not UNSET:
            field_dict["group"] = group
        if sector is not UNSET:
            field_dict["sector"] = sector

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        from ..models.portfolio_allocations_asset_class import PortfolioAllocationsAssetClass
        from ..models.portfolio_allocations_group import PortfolioAllocationsGroup
        from ..models.portfolio_allocations_sector import PortfolioAllocationsSector

        d = src_dict.copy()
        _asset_class = d.pop("assetClass", UNSET)
        asset_class: Union[Unset, PortfolioAllocationsAssetClass]
        if isinstance(_asset_class, Unset):
            asset_class = UNSET
        else:
            asset_class = PortfolioAllocationsAssetClass.from_dict(_asset_class)

        _group = d.pop("group", UNSET)
        group: Union[Unset, PortfolioAllocationsGroup]
        if isinstance(_group, Unset):
            group = UNSET
        else:
            group = PortfolioAllocationsGroup.from_dict(_group)

        _sector = d.pop("sector", UNSET)
        sector: Union[Unset, PortfolioAllocationsSector]
        if isinstance(_sector, Unset):
            sector = UNSET
        else:
            sector = PortfolioAllocationsSector.from_dict(_sector)

        portfolio_allocations = cls(
            asset_class=asset_class,
            group=group,
            sector=sector,
        )

        portfolio_allocations.additional_properties = d
        return portfolio_allocations

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
