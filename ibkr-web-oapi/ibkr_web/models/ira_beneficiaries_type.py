from typing import TYPE_CHECKING, Any, Dict, List, Type, TypeVar, Union

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.ira_contingent_beneficiary import IRAContingentBeneficiary
    from ..models.ira_contingent_beneficiary_entity import IRAContingentBeneficiaryEntity
    from ..models.ira_primary_beneficiary import IRAPrimaryBeneficiary
    from ..models.ira_primary_beneficiary_entity import IRAPrimaryBeneficiaryEntity


T = TypeVar("T", bound="IRABeneficiariesType")


@_attrs_define
class IRABeneficiariesType:
    """
    Attributes:
        primary_beneficiaries (Union[Unset, List['IRAPrimaryBeneficiary']]):
        primary_beneficiary_entities (Union[Unset, List['IRAPrimaryBeneficiaryEntity']]):
        contingent_beneficiaries (Union[Unset, List['IRAContingentBeneficiary']]):
        contingent_beneficiary_entities (Union[Unset, List['IRAContingentBeneficiaryEntity']]):
        spouse_primary_beneficary (Union[Unset, bool]):
        successor (Union[Unset, bool]):
    """

    primary_beneficiaries: Union[Unset, List["IRAPrimaryBeneficiary"]] = UNSET
    primary_beneficiary_entities: Union[Unset, List["IRAPrimaryBeneficiaryEntity"]] = UNSET
    contingent_beneficiaries: Union[Unset, List["IRAContingentBeneficiary"]] = UNSET
    contingent_beneficiary_entities: Union[Unset, List["IRAContingentBeneficiaryEntity"]] = UNSET
    spouse_primary_beneficary: Union[Unset, bool] = UNSET
    successor: Union[Unset, bool] = UNSET
    additional_properties: Dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> Dict[str, Any]:
        primary_beneficiaries: Union[Unset, List[Dict[str, Any]]] = UNSET
        if not isinstance(self.primary_beneficiaries, Unset):
            primary_beneficiaries = []
            for primary_beneficiaries_item_data in self.primary_beneficiaries:
                primary_beneficiaries_item = primary_beneficiaries_item_data.to_dict()
                primary_beneficiaries.append(primary_beneficiaries_item)

        primary_beneficiary_entities: Union[Unset, List[Dict[str, Any]]] = UNSET
        if not isinstance(self.primary_beneficiary_entities, Unset):
            primary_beneficiary_entities = []
            for primary_beneficiary_entities_item_data in self.primary_beneficiary_entities:
                primary_beneficiary_entities_item = primary_beneficiary_entities_item_data.to_dict()
                primary_beneficiary_entities.append(primary_beneficiary_entities_item)

        contingent_beneficiaries: Union[Unset, List[Dict[str, Any]]] = UNSET
        if not isinstance(self.contingent_beneficiaries, Unset):
            contingent_beneficiaries = []
            for contingent_beneficiaries_item_data in self.contingent_beneficiaries:
                contingent_beneficiaries_item = contingent_beneficiaries_item_data.to_dict()
                contingent_beneficiaries.append(contingent_beneficiaries_item)

        contingent_beneficiary_entities: Union[Unset, List[Dict[str, Any]]] = UNSET
        if not isinstance(self.contingent_beneficiary_entities, Unset):
            contingent_beneficiary_entities = []
            for contingent_beneficiary_entities_item_data in self.contingent_beneficiary_entities:
                contingent_beneficiary_entities_item = contingent_beneficiary_entities_item_data.to_dict()
                contingent_beneficiary_entities.append(contingent_beneficiary_entities_item)

        spouse_primary_beneficary = self.spouse_primary_beneficary

        successor = self.successor

        field_dict: Dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if primary_beneficiaries is not UNSET:
            field_dict["primaryBeneficiaries"] = primary_beneficiaries
        if primary_beneficiary_entities is not UNSET:
            field_dict["primaryBeneficiaryEntities"] = primary_beneficiary_entities
        if contingent_beneficiaries is not UNSET:
            field_dict["contingentBeneficiaries"] = contingent_beneficiaries
        if contingent_beneficiary_entities is not UNSET:
            field_dict["contingentBeneficiaryEntities"] = contingent_beneficiary_entities
        if spouse_primary_beneficary is not UNSET:
            field_dict["spousePrimaryBeneficary"] = spouse_primary_beneficary
        if successor is not UNSET:
            field_dict["successor"] = successor

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        from ..models.ira_contingent_beneficiary import IRAContingentBeneficiary
        from ..models.ira_contingent_beneficiary_entity import IRAContingentBeneficiaryEntity
        from ..models.ira_primary_beneficiary import IRAPrimaryBeneficiary
        from ..models.ira_primary_beneficiary_entity import IRAPrimaryBeneficiaryEntity

        d = src_dict.copy()
        primary_beneficiaries = []
        _primary_beneficiaries = d.pop("primaryBeneficiaries", UNSET)
        for primary_beneficiaries_item_data in _primary_beneficiaries or []:
            primary_beneficiaries_item = IRAPrimaryBeneficiary.from_dict(primary_beneficiaries_item_data)

            primary_beneficiaries.append(primary_beneficiaries_item)

        primary_beneficiary_entities = []
        _primary_beneficiary_entities = d.pop("primaryBeneficiaryEntities", UNSET)
        for primary_beneficiary_entities_item_data in _primary_beneficiary_entities or []:
            primary_beneficiary_entities_item = IRAPrimaryBeneficiaryEntity.from_dict(
                primary_beneficiary_entities_item_data
            )

            primary_beneficiary_entities.append(primary_beneficiary_entities_item)

        contingent_beneficiaries = []
        _contingent_beneficiaries = d.pop("contingentBeneficiaries", UNSET)
        for contingent_beneficiaries_item_data in _contingent_beneficiaries or []:
            contingent_beneficiaries_item = IRAContingentBeneficiary.from_dict(contingent_beneficiaries_item_data)

            contingent_beneficiaries.append(contingent_beneficiaries_item)

        contingent_beneficiary_entities = []
        _contingent_beneficiary_entities = d.pop("contingentBeneficiaryEntities", UNSET)
        for contingent_beneficiary_entities_item_data in _contingent_beneficiary_entities or []:
            contingent_beneficiary_entities_item = IRAContingentBeneficiaryEntity.from_dict(
                contingent_beneficiary_entities_item_data
            )

            contingent_beneficiary_entities.append(contingent_beneficiary_entities_item)

        spouse_primary_beneficary = d.pop("spousePrimaryBeneficary", UNSET)

        successor = d.pop("successor", UNSET)

        ira_beneficiaries_type = cls(
            primary_beneficiaries=primary_beneficiaries,
            primary_beneficiary_entities=primary_beneficiary_entities,
            contingent_beneficiaries=contingent_beneficiaries,
            contingent_beneficiary_entities=contingent_beneficiary_entities,
            spouse_primary_beneficary=spouse_primary_beneficary,
            successor=successor,
        )

        ira_beneficiaries_type.additional_properties = d
        return ira_beneficiaries_type

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
