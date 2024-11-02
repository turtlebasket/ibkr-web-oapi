from typing import Any, Dict, List, Type, TypeVar, Union

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..models.asset_experience_asset_class import AssetExperienceAssetClass
from ..models.asset_experience_knowledge_level import AssetExperienceKnowledgeLevel
from ..types import UNSET, Unset

T = TypeVar("T", bound="AssetExperience")


@_attrs_define
class AssetExperience:
    """
    Attributes:
        asset_class (Union[Unset, AssetExperienceAssetClass]):
        years_trading (Union[Unset, int]):
        trades_per_year (Union[Unset, int]):
        knowledge_level (Union[Unset, AssetExperienceKnowledgeLevel]):
    """

    asset_class: Union[Unset, AssetExperienceAssetClass] = UNSET
    years_trading: Union[Unset, int] = UNSET
    trades_per_year: Union[Unset, int] = UNSET
    knowledge_level: Union[Unset, AssetExperienceKnowledgeLevel] = UNSET
    additional_properties: Dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> Dict[str, Any]:
        asset_class: Union[Unset, str] = UNSET
        if not isinstance(self.asset_class, Unset):
            asset_class = self.asset_class.value

        years_trading = self.years_trading

        trades_per_year = self.trades_per_year

        knowledge_level: Union[Unset, str] = UNSET
        if not isinstance(self.knowledge_level, Unset):
            knowledge_level = self.knowledge_level.value

        field_dict: Dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if asset_class is not UNSET:
            field_dict["assetClass"] = asset_class
        if years_trading is not UNSET:
            field_dict["yearsTrading"] = years_trading
        if trades_per_year is not UNSET:
            field_dict["tradesPerYear"] = trades_per_year
        if knowledge_level is not UNSET:
            field_dict["knowledgeLevel"] = knowledge_level

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        d = src_dict.copy()
        _asset_class = d.pop("assetClass", UNSET)
        asset_class: Union[Unset, AssetExperienceAssetClass]
        if isinstance(_asset_class, Unset):
            asset_class = UNSET
        else:
            asset_class = AssetExperienceAssetClass(_asset_class)

        years_trading = d.pop("yearsTrading", UNSET)

        trades_per_year = d.pop("tradesPerYear", UNSET)

        _knowledge_level = d.pop("knowledgeLevel", UNSET)
        knowledge_level: Union[Unset, AssetExperienceKnowledgeLevel]
        if isinstance(_knowledge_level, Unset):
            knowledge_level = UNSET
        else:
            knowledge_level = AssetExperienceKnowledgeLevel(_knowledge_level)

        asset_experience = cls(
            asset_class=asset_class,
            years_trading=years_trading,
            trades_per_year=trades_per_year,
            knowledge_level=knowledge_level,
        )

        asset_experience.additional_properties = d
        return asset_experience

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
