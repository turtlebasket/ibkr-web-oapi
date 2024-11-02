from typing import TYPE_CHECKING, Any, Dict, List, Type, TypeVar, Union

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.individual import Individual
    from ..models.legal_entity import LegalEntity


T = TypeVar("T", bound="CustodianType")


@_attrs_define
class CustodianType:
    """
    Attributes:
        individual (Union[Unset, Individual]):
        legal_entity (Union[Unset, LegalEntity]):
        employee (Union[Unset, Individual]):
    """

    individual: Union[Unset, "Individual"] = UNSET
    legal_entity: Union[Unset, "LegalEntity"] = UNSET
    employee: Union[Unset, "Individual"] = UNSET
    additional_properties: Dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> Dict[str, Any]:
        individual: Union[Unset, Dict[str, Any]] = UNSET
        if not isinstance(self.individual, Unset):
            individual = self.individual.to_dict()

        legal_entity: Union[Unset, Dict[str, Any]] = UNSET
        if not isinstance(self.legal_entity, Unset):
            legal_entity = self.legal_entity.to_dict()

        employee: Union[Unset, Dict[str, Any]] = UNSET
        if not isinstance(self.employee, Unset):
            employee = self.employee.to_dict()

        field_dict: Dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if individual is not UNSET:
            field_dict["individual"] = individual
        if legal_entity is not UNSET:
            field_dict["legalEntity"] = legal_entity
        if employee is not UNSET:
            field_dict["employee"] = employee

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        from ..models.individual import Individual
        from ..models.legal_entity import LegalEntity

        d = src_dict.copy()
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

        _employee = d.pop("employee", UNSET)
        employee: Union[Unset, Individual]
        if isinstance(_employee, Unset):
            employee = UNSET
        else:
            employee = Individual.from_dict(_employee)

        custodian_type = cls(
            individual=individual,
            legal_entity=legal_entity,
            employee=employee,
        )

        custodian_type.additional_properties = d
        return custodian_type

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
