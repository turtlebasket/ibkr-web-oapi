import datetime
from typing import TYPE_CHECKING, Any, Dict, List, Type, TypeVar, Union

from attrs import define as _attrs_define
from attrs import field as _attrs_field
from dateutil.parser import isoparse

from ..models.ira_contingent_beneficiary_entity_entity_type import IRAContingentBeneficiaryEntityEntityType
from ..models.ira_contingent_beneficiary_entity_relationship import IRAContingentBeneficiaryEntityRelationship
from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.address import Address
    from ..models.individual import Individual
    from ..models.title import Title


T = TypeVar("T", bound="IRAContingentBeneficiaryEntity")


@_attrs_define
class IRAContingentBeneficiaryEntity:
    """
    Attributes:
        name (Union[Unset, str]):
        address (Union[Unset, Address]):
        id (Union[Unset, str]):
        external_id (Union[Unset, str]):
        ownership_percentage (Union[Unset, float]):
        title (Union[Unset, Title]):
        relationship (Union[Unset, IRAContingentBeneficiaryEntityRelationship]):
        executor (Union[Unset, Individual]):
        execution_date (Union[Unset, datetime.date]):
        article_of_will (Union[Unset, str]):
        entity_type (Union[Unset, IRAContingentBeneficiaryEntityEntityType]):
    """

    name: Union[Unset, str] = UNSET
    address: Union[Unset, "Address"] = UNSET
    id: Union[Unset, str] = UNSET
    external_id: Union[Unset, str] = UNSET
    ownership_percentage: Union[Unset, float] = UNSET
    title: Union[Unset, "Title"] = UNSET
    relationship: Union[Unset, IRAContingentBeneficiaryEntityRelationship] = UNSET
    executor: Union[Unset, "Individual"] = UNSET
    execution_date: Union[Unset, datetime.date] = UNSET
    article_of_will: Union[Unset, str] = UNSET
    entity_type: Union[Unset, IRAContingentBeneficiaryEntityEntityType] = UNSET
    additional_properties: Dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> Dict[str, Any]:
        name = self.name

        address: Union[Unset, Dict[str, Any]] = UNSET
        if not isinstance(self.address, Unset):
            address = self.address.to_dict()

        id = self.id

        external_id = self.external_id

        ownership_percentage = self.ownership_percentage

        title: Union[Unset, Dict[str, Any]] = UNSET
        if not isinstance(self.title, Unset):
            title = self.title.to_dict()

        relationship: Union[Unset, str] = UNSET
        if not isinstance(self.relationship, Unset):
            relationship = self.relationship.value

        executor: Union[Unset, Dict[str, Any]] = UNSET
        if not isinstance(self.executor, Unset):
            executor = self.executor.to_dict()

        execution_date: Union[Unset, str] = UNSET
        if not isinstance(self.execution_date, Unset):
            execution_date = self.execution_date.isoformat()

        article_of_will = self.article_of_will

        entity_type: Union[Unset, str] = UNSET
        if not isinstance(self.entity_type, Unset):
            entity_type = self.entity_type.value

        field_dict: Dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if name is not UNSET:
            field_dict["name"] = name
        if address is not UNSET:
            field_dict["address"] = address
        if id is not UNSET:
            field_dict["id"] = id
        if external_id is not UNSET:
            field_dict["externalId"] = external_id
        if ownership_percentage is not UNSET:
            field_dict["ownershipPercentage"] = ownership_percentage
        if title is not UNSET:
            field_dict["title"] = title
        if relationship is not UNSET:
            field_dict["relationship"] = relationship
        if executor is not UNSET:
            field_dict["executor"] = executor
        if execution_date is not UNSET:
            field_dict["executionDate"] = execution_date
        if article_of_will is not UNSET:
            field_dict["articleOfWill"] = article_of_will
        if entity_type is not UNSET:
            field_dict["entityType"] = entity_type

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        from ..models.address import Address
        from ..models.individual import Individual
        from ..models.title import Title

        d = src_dict.copy()
        name = d.pop("name", UNSET)

        _address = d.pop("address", UNSET)
        address: Union[Unset, Address]
        if isinstance(_address, Unset):
            address = UNSET
        else:
            address = Address.from_dict(_address)

        id = d.pop("id", UNSET)

        external_id = d.pop("externalId", UNSET)

        ownership_percentage = d.pop("ownershipPercentage", UNSET)

        _title = d.pop("title", UNSET)
        title: Union[Unset, Title]
        if isinstance(_title, Unset):
            title = UNSET
        else:
            title = Title.from_dict(_title)

        _relationship = d.pop("relationship", UNSET)
        relationship: Union[Unset, IRAContingentBeneficiaryEntityRelationship]
        if isinstance(_relationship, Unset):
            relationship = UNSET
        else:
            relationship = IRAContingentBeneficiaryEntityRelationship(_relationship)

        _executor = d.pop("executor", UNSET)
        executor: Union[Unset, Individual]
        if isinstance(_executor, Unset):
            executor = UNSET
        else:
            executor = Individual.from_dict(_executor)

        _execution_date = d.pop("executionDate", UNSET)
        execution_date: Union[Unset, datetime.date]
        if isinstance(_execution_date, Unset):
            execution_date = UNSET
        else:
            execution_date = isoparse(_execution_date).date()

        article_of_will = d.pop("articleOfWill", UNSET)

        _entity_type = d.pop("entityType", UNSET)
        entity_type: Union[Unset, IRAContingentBeneficiaryEntityEntityType]
        if isinstance(_entity_type, Unset):
            entity_type = UNSET
        else:
            entity_type = IRAContingentBeneficiaryEntityEntityType(_entity_type)

        ira_contingent_beneficiary_entity = cls(
            name=name,
            address=address,
            id=id,
            external_id=external_id,
            ownership_percentage=ownership_percentage,
            title=title,
            relationship=relationship,
            executor=executor,
            execution_date=execution_date,
            article_of_will=article_of_will,
            entity_type=entity_type,
        )

        ira_contingent_beneficiary_entity.additional_properties = d
        return ira_contingent_beneficiary_entity

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
