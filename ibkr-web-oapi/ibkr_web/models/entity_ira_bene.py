from typing import TYPE_CHECKING, Any, Dict, List, Type, TypeVar, Union

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.entity_ira_bene_location import EntityIRABeneLocation


T = TypeVar("T", bound="EntityIRABene")


@_attrs_define
class EntityIRABene:
    """
    Attributes:
        name (Union[Unset, str]):
        entity_type (Union[Unset, str]):
        type (Union[Unset, str]):
        location (Union[Unset, EntityIRABeneLocation]):
        article_of_will (Union[Unset, str]):
    """

    name: Union[Unset, str] = UNSET
    entity_type: Union[Unset, str] = UNSET
    type: Union[Unset, str] = UNSET
    location: Union[Unset, "EntityIRABeneLocation"] = UNSET
    article_of_will: Union[Unset, str] = UNSET
    additional_properties: Dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> Dict[str, Any]:
        name = self.name

        entity_type = self.entity_type

        type = self.type

        location: Union[Unset, Dict[str, Any]] = UNSET
        if not isinstance(self.location, Unset):
            location = self.location.to_dict()

        article_of_will = self.article_of_will

        field_dict: Dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if name is not UNSET:
            field_dict["name"] = name
        if entity_type is not UNSET:
            field_dict["entityType"] = entity_type
        if type is not UNSET:
            field_dict["type"] = type
        if location is not UNSET:
            field_dict["location"] = location
        if article_of_will is not UNSET:
            field_dict["articleOfWill"] = article_of_will

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        from ..models.entity_ira_bene_location import EntityIRABeneLocation

        d = src_dict.copy()
        name = d.pop("name", UNSET)

        entity_type = d.pop("entityType", UNSET)

        type = d.pop("type", UNSET)

        _location = d.pop("location", UNSET)
        location: Union[Unset, EntityIRABeneLocation]
        if isinstance(_location, Unset):
            location = UNSET
        else:
            location = EntityIRABeneLocation.from_dict(_location)

        article_of_will = d.pop("articleOfWill", UNSET)

        entity_ira_bene = cls(
            name=name,
            entity_type=entity_type,
            type=type,
            location=location,
            article_of_will=article_of_will,
        )

        entity_ira_bene.additional_properties = d
        return entity_ira_bene

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
