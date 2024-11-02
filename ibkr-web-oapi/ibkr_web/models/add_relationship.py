from typing import Any, Dict, List, Type, TypeVar, Union

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..models.add_relationship_name import AddRelationshipName
from ..types import UNSET, Unset

T = TypeVar("T", bound="AddRelationship")


@_attrs_define
class AddRelationship:
    """
    Attributes:
        name (Union[Unset, AddRelationshipName]):
        ownership_percentage (Union[Unset, int]):
    """

    name: Union[Unset, AddRelationshipName] = UNSET
    ownership_percentage: Union[Unset, int] = UNSET
    additional_properties: Dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> Dict[str, Any]:
        name: Union[Unset, str] = UNSET
        if not isinstance(self.name, Unset):
            name = self.name.value

        ownership_percentage = self.ownership_percentage

        field_dict: Dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if name is not UNSET:
            field_dict["name"] = name
        if ownership_percentage is not UNSET:
            field_dict["ownershipPercentage"] = ownership_percentage

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        d = src_dict.copy()
        _name = d.pop("name", UNSET)
        name: Union[Unset, AddRelationshipName]
        if isinstance(_name, Unset):
            name = UNSET
        else:
            name = AddRelationshipName(_name)

        ownership_percentage = d.pop("ownershipPercentage", UNSET)

        add_relationship = cls(
            name=name,
            ownership_percentage=ownership_percentage,
        )

        add_relationship.additional_properties = d
        return add_relationship

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
