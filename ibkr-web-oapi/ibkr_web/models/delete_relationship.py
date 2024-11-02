from typing import Any, Dict, List, Type, TypeVar, Union

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..models.delete_relationship_name import DeleteRelationshipName
from ..types import UNSET, Unset

T = TypeVar("T", bound="DeleteRelationship")


@_attrs_define
class DeleteRelationship:
    """
    Attributes:
        name (Union[Unset, DeleteRelationshipName]):
    """

    name: Union[Unset, DeleteRelationshipName] = UNSET
    additional_properties: Dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> Dict[str, Any]:
        name: Union[Unset, str] = UNSET
        if not isinstance(self.name, Unset):
            name = self.name.value

        field_dict: Dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if name is not UNSET:
            field_dict["name"] = name

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        d = src_dict.copy()
        _name = d.pop("name", UNSET)
        name: Union[Unset, DeleteRelationshipName]
        if isinstance(_name, Unset):
            name = UNSET
        else:
            name = DeleteRelationshipName(_name)

        delete_relationship = cls(
            name=name,
        )

        delete_relationship.additional_properties = d
        return delete_relationship

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
