from typing import TYPE_CHECKING, Any, Dict, List, Type, TypeVar, Union

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..models.account_support_type_type import AccountSupportTypeType
from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.administrator_contact_person_type import AdministratorContactPersonType
    from ..models.administrator_type import AdministratorType
    from ..models.primary_contributor_type import PrimaryContributorType


T = TypeVar("T", bound="AccountSupportType")


@_attrs_define
class AccountSupportType:
    """
    Attributes:
        business_description (Union[Unset, str]):
        primary_contributor (Union[Unset, PrimaryContributorType]):
        administrator (Union[Unset, AdministratorType]):
        administrator_contact_person (Union[Unset, AdministratorContactPersonType]):
        owners_reside_us (Union[Unset, bool]):
        solicit_owners_reside_us (Union[Unset, bool]):
        accept_owners_reside_us (Union[Unset, bool]):
        type (Union[Unset, AccountSupportTypeType]):
    """

    business_description: Union[Unset, str] = UNSET
    primary_contributor: Union[Unset, "PrimaryContributorType"] = UNSET
    administrator: Union[Unset, "AdministratorType"] = UNSET
    administrator_contact_person: Union[Unset, "AdministratorContactPersonType"] = UNSET
    owners_reside_us: Union[Unset, bool] = UNSET
    solicit_owners_reside_us: Union[Unset, bool] = UNSET
    accept_owners_reside_us: Union[Unset, bool] = UNSET
    type: Union[Unset, AccountSupportTypeType] = UNSET
    additional_properties: Dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> Dict[str, Any]:
        business_description = self.business_description

        primary_contributor: Union[Unset, Dict[str, Any]] = UNSET
        if not isinstance(self.primary_contributor, Unset):
            primary_contributor = self.primary_contributor.to_dict()

        administrator: Union[Unset, Dict[str, Any]] = UNSET
        if not isinstance(self.administrator, Unset):
            administrator = self.administrator.to_dict()

        administrator_contact_person: Union[Unset, Dict[str, Any]] = UNSET
        if not isinstance(self.administrator_contact_person, Unset):
            administrator_contact_person = self.administrator_contact_person.to_dict()

        owners_reside_us = self.owners_reside_us

        solicit_owners_reside_us = self.solicit_owners_reside_us

        accept_owners_reside_us = self.accept_owners_reside_us

        type: Union[Unset, str] = UNSET
        if not isinstance(self.type, Unset):
            type = self.type.value

        field_dict: Dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if business_description is not UNSET:
            field_dict["businessDescription"] = business_description
        if primary_contributor is not UNSET:
            field_dict["primaryContributor"] = primary_contributor
        if administrator is not UNSET:
            field_dict["administrator"] = administrator
        if administrator_contact_person is not UNSET:
            field_dict["administratorContactPerson"] = administrator_contact_person
        if owners_reside_us is not UNSET:
            field_dict["ownersResideUS"] = owners_reside_us
        if solicit_owners_reside_us is not UNSET:
            field_dict["solicitOwnersResideUS"] = solicit_owners_reside_us
        if accept_owners_reside_us is not UNSET:
            field_dict["acceptOwnersResideUS"] = accept_owners_reside_us
        if type is not UNSET:
            field_dict["type"] = type

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        from ..models.administrator_contact_person_type import AdministratorContactPersonType
        from ..models.administrator_type import AdministratorType
        from ..models.primary_contributor_type import PrimaryContributorType

        d = src_dict.copy()
        business_description = d.pop("businessDescription", UNSET)

        _primary_contributor = d.pop("primaryContributor", UNSET)
        primary_contributor: Union[Unset, PrimaryContributorType]
        if isinstance(_primary_contributor, Unset):
            primary_contributor = UNSET
        else:
            primary_contributor = PrimaryContributorType.from_dict(_primary_contributor)

        _administrator = d.pop("administrator", UNSET)
        administrator: Union[Unset, AdministratorType]
        if isinstance(_administrator, Unset):
            administrator = UNSET
        else:
            administrator = AdministratorType.from_dict(_administrator)

        _administrator_contact_person = d.pop("administratorContactPerson", UNSET)
        administrator_contact_person: Union[Unset, AdministratorContactPersonType]
        if isinstance(_administrator_contact_person, Unset):
            administrator_contact_person = UNSET
        else:
            administrator_contact_person = AdministratorContactPersonType.from_dict(_administrator_contact_person)

        owners_reside_us = d.pop("ownersResideUS", UNSET)

        solicit_owners_reside_us = d.pop("solicitOwnersResideUS", UNSET)

        accept_owners_reside_us = d.pop("acceptOwnersResideUS", UNSET)

        _type = d.pop("type", UNSET)
        type: Union[Unset, AccountSupportTypeType]
        if isinstance(_type, Unset):
            type = UNSET
        else:
            type = AccountSupportTypeType(_type)

        account_support_type = cls(
            business_description=business_description,
            primary_contributor=primary_contributor,
            administrator=administrator,
            administrator_contact_person=administrator_contact_person,
            owners_reside_us=owners_reside_us,
            solicit_owners_reside_us=solicit_owners_reside_us,
            accept_owners_reside_us=accept_owners_reside_us,
            type=type,
        )

        account_support_type.additional_properties = d
        return account_support_type

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
