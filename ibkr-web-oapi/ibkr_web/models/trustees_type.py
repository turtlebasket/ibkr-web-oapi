from typing import TYPE_CHECKING, Any, Dict, List, Type, TypeVar, Union

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.trustee_entity_type import TrusteeEntityType
    from ..models.trustee_individual import TrusteeIndividual


T = TypeVar("T", bound="TrusteesType")


@_attrs_define
class TrusteesType:
    """
    Attributes:
        individuals (Union[Unset, List['TrusteeIndividual']]):
        entities (Union[Unset, List['TrusteeEntityType']]):
    """

    individuals: Union[Unset, List["TrusteeIndividual"]] = UNSET
    entities: Union[Unset, List["TrusteeEntityType"]] = UNSET
    additional_properties: Dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> Dict[str, Any]:
        individuals: Union[Unset, List[Dict[str, Any]]] = UNSET
        if not isinstance(self.individuals, Unset):
            individuals = []
            for individuals_item_data in self.individuals:
                individuals_item = individuals_item_data.to_dict()
                individuals.append(individuals_item)

        entities: Union[Unset, List[Dict[str, Any]]] = UNSET
        if not isinstance(self.entities, Unset):
            entities = []
            for entities_item_data in self.entities:
                entities_item = entities_item_data.to_dict()
                entities.append(entities_item)

        field_dict: Dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if individuals is not UNSET:
            field_dict["individuals"] = individuals
        if entities is not UNSET:
            field_dict["entities"] = entities

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        from ..models.trustee_entity_type import TrusteeEntityType
        from ..models.trustee_individual import TrusteeIndividual

        d = src_dict.copy()
        individuals = []
        _individuals = d.pop("individuals", UNSET)
        for individuals_item_data in _individuals or []:
            individuals_item = TrusteeIndividual.from_dict(individuals_item_data)

            individuals.append(individuals_item)

        entities = []
        _entities = d.pop("entities", UNSET)
        for entities_item_data in _entities or []:
            entities_item = TrusteeEntityType.from_dict(entities_item_data)

            entities.append(entities_item)

        trustees_type = cls(
            individuals=individuals,
            entities=entities,
        )

        trustees_type.additional_properties = d
        return trustees_type

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
