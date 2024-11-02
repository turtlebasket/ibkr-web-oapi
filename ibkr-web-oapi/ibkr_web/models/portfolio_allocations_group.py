from typing import TYPE_CHECKING, Any, Dict, List, Type, TypeVar, Union

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.portfolio_allocations_group_long import PortfolioAllocationsGroupLong
    from ..models.portfolio_allocations_group_short import PortfolioAllocationsGroupShort


T = TypeVar("T", bound="PortfolioAllocationsGroup")


@_attrs_define
class PortfolioAllocationsGroup:
    """Object containing values of positions sorted by long/short and Sector Group.

    Attributes:
        long (Union[Unset, PortfolioAllocationsGroupLong]): Object containing value of long positions in the account
            aggregated by Sector Group.
        short (Union[Unset, PortfolioAllocationsGroupShort]): Object containing value of short positions in the account
            aggregated by Sector Group.
    """

    long: Union[Unset, "PortfolioAllocationsGroupLong"] = UNSET
    short: Union[Unset, "PortfolioAllocationsGroupShort"] = UNSET
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
        from ..models.portfolio_allocations_group_long import PortfolioAllocationsGroupLong
        from ..models.portfolio_allocations_group_short import PortfolioAllocationsGroupShort

        d = src_dict.copy()
        _long = d.pop("long", UNSET)
        long: Union[Unset, PortfolioAllocationsGroupLong]
        if isinstance(_long, Unset):
            long = UNSET
        else:
            long = PortfolioAllocationsGroupLong.from_dict(_long)

        _short = d.pop("short", UNSET)
        short: Union[Unset, PortfolioAllocationsGroupShort]
        if isinstance(_short, Unset):
            short = UNSET
        else:
            short = PortfolioAllocationsGroupShort.from_dict(_short)

        portfolio_allocations_group = cls(
            long=long,
            short=short,
        )

        portfolio_allocations_group.additional_properties = d
        return portfolio_allocations_group

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
