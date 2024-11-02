from typing import TYPE_CHECKING, Any, Dict, List, Type, TypeVar, Union

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.individual import Individual
    from ..models.legal_entity import LegalEntity


T = TypeVar("T", bound="TrusteeEntityType")


@_attrs_define
class TrusteeEntityType:
    """
    Attributes:
        legal_entity (Union[Unset, LegalEntity]):
        employees (Union[Unset, List['Individual']]):
    """

    legal_entity: Union[Unset, "LegalEntity"] = UNSET
    employees: Union[Unset, List["Individual"]] = UNSET
    additional_properties: Dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> Dict[str, Any]:
        legal_entity: Union[Unset, Dict[str, Any]] = UNSET
        if not isinstance(self.legal_entity, Unset):
            legal_entity = self.legal_entity.to_dict()

        employees: Union[Unset, List[Dict[str, Any]]] = UNSET
        if not isinstance(self.employees, Unset):
            employees = []
            for employees_item_data in self.employees:
                employees_item = employees_item_data.to_dict()
                employees.append(employees_item)

        field_dict: Dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if legal_entity is not UNSET:
            field_dict["legalEntity"] = legal_entity
        if employees is not UNSET:
            field_dict["employees"] = employees

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        from ..models.individual import Individual
        from ..models.legal_entity import LegalEntity

        d = src_dict.copy()
        _legal_entity = d.pop("legalEntity", UNSET)
        legal_entity: Union[Unset, LegalEntity]
        if isinstance(_legal_entity, Unset):
            legal_entity = UNSET
        else:
            legal_entity = LegalEntity.from_dict(_legal_entity)

        employees = []
        _employees = d.pop("employees", UNSET)
        for employees_item_data in _employees or []:
            employees_item = Individual.from_dict(employees_item_data)

            employees.append(employees_item)

        trustee_entity_type = cls(
            legal_entity=legal_entity,
            employees=employees,
        )

        trustee_entity_type.additional_properties = d
        return trustee_entity_type

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
