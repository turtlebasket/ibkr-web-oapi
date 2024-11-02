from typing import TYPE_CHECKING, Any, Dict, List, Type, TypeVar, Union

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.associated_individual import AssociatedIndividual
    from ..models.legal_entity import LegalEntity


T = TypeVar("T", bound="AssociationTypeEntities")


@_attrs_define
class AssociationTypeEntities:
    """
    Attributes:
        individual (Union[Unset, List['AssociatedIndividual']]):
        legal_entity (Union[Unset, List['LegalEntity']]):
    """

    individual: Union[Unset, List["AssociatedIndividual"]] = UNSET
    legal_entity: Union[Unset, List["LegalEntity"]] = UNSET
    additional_properties: Dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> Dict[str, Any]:
        individual: Union[Unset, List[Dict[str, Any]]] = UNSET
        if not isinstance(self.individual, Unset):
            individual = []
            for individual_item_data in self.individual:
                individual_item = individual_item_data.to_dict()
                individual.append(individual_item)

        legal_entity: Union[Unset, List[Dict[str, Any]]] = UNSET
        if not isinstance(self.legal_entity, Unset):
            legal_entity = []
            for legal_entity_item_data in self.legal_entity:
                legal_entity_item = legal_entity_item_data.to_dict()
                legal_entity.append(legal_entity_item)

        field_dict: Dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if individual is not UNSET:
            field_dict["individual"] = individual
        if legal_entity is not UNSET:
            field_dict["legalEntity"] = legal_entity

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        from ..models.associated_individual import AssociatedIndividual
        from ..models.legal_entity import LegalEntity

        d = src_dict.copy()
        individual = []
        _individual = d.pop("individual", UNSET)
        for individual_item_data in _individual or []:
            individual_item = AssociatedIndividual.from_dict(individual_item_data)

            individual.append(individual_item)

        legal_entity = []
        _legal_entity = d.pop("legalEntity", UNSET)
        for legal_entity_item_data in _legal_entity or []:
            legal_entity_item = LegalEntity.from_dict(legal_entity_item_data)

            legal_entity.append(legal_entity_item)

        association_type_entities = cls(
            individual=individual,
            legal_entity=legal_entity,
        )

        association_type_entities.additional_properties = d
        return association_type_entities

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
