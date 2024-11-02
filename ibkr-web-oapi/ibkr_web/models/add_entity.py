from typing import TYPE_CHECKING, Any, Dict, List, Type, TypeVar, Union

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.add_relationship import AddRelationship
    from ..models.document import Document
    from ..models.individual import Individual
    from ..models.legal_entity import LegalEntity


T = TypeVar("T", bound="AddEntity")


@_attrs_define
class AddEntity:
    """
    Attributes:
        add_relationships (Union[Unset, List['AddRelationship']]):
        individual (Union[Unset, Individual]):
        legal_entity (Union[Unset, LegalEntity]):
        documents (Union[Unset, List['Document']]):
    """

    add_relationships: Union[Unset, List["AddRelationship"]] = UNSET
    individual: Union[Unset, "Individual"] = UNSET
    legal_entity: Union[Unset, "LegalEntity"] = UNSET
    documents: Union[Unset, List["Document"]] = UNSET
    additional_properties: Dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> Dict[str, Any]:
        add_relationships: Union[Unset, List[Dict[str, Any]]] = UNSET
        if not isinstance(self.add_relationships, Unset):
            add_relationships = []
            for add_relationships_item_data in self.add_relationships:
                add_relationships_item = add_relationships_item_data.to_dict()
                add_relationships.append(add_relationships_item)

        individual: Union[Unset, Dict[str, Any]] = UNSET
        if not isinstance(self.individual, Unset):
            individual = self.individual.to_dict()

        legal_entity: Union[Unset, Dict[str, Any]] = UNSET
        if not isinstance(self.legal_entity, Unset):
            legal_entity = self.legal_entity.to_dict()

        documents: Union[Unset, List[Dict[str, Any]]] = UNSET
        if not isinstance(self.documents, Unset):
            documents = []
            for documents_item_data in self.documents:
                documents_item = documents_item_data.to_dict()
                documents.append(documents_item)

        field_dict: Dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if add_relationships is not UNSET:
            field_dict["addRelationships"] = add_relationships
        if individual is not UNSET:
            field_dict["individual"] = individual
        if legal_entity is not UNSET:
            field_dict["legalEntity"] = legal_entity
        if documents is not UNSET:
            field_dict["documents"] = documents

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        from ..models.add_relationship import AddRelationship
        from ..models.document import Document
        from ..models.individual import Individual
        from ..models.legal_entity import LegalEntity

        d = src_dict.copy()
        add_relationships = []
        _add_relationships = d.pop("addRelationships", UNSET)
        for add_relationships_item_data in _add_relationships or []:
            add_relationships_item = AddRelationship.from_dict(add_relationships_item_data)

            add_relationships.append(add_relationships_item)

        _individual = d.pop("individual", UNSET)
        individual: Union[Unset, Individual]
        if isinstance(_individual, Unset):
            individual = UNSET
        else:
            individual = Individual.from_dict(_individual)

        _legal_entity = d.pop("legalEntity", UNSET)
        legal_entity: Union[Unset, LegalEntity]
        if isinstance(_legal_entity, Unset):
            legal_entity = UNSET
        else:
            legal_entity = LegalEntity.from_dict(_legal_entity)

        documents = []
        _documents = d.pop("documents", UNSET)
        for documents_item_data in _documents or []:
            documents_item = Document.from_dict(documents_item_data)

            documents.append(documents_item)

        add_entity = cls(
            add_relationships=add_relationships,
            individual=individual,
            legal_entity=legal_entity,
            documents=documents,
        )

        add_entity.additional_properties = d
        return add_entity

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
