from typing import TYPE_CHECKING, Any, Dict, List, Type, TypeVar, Union, cast

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.associated_entity_identity_documents_item import AssociatedEntityIdentityDocumentsItem
    from ..models.associated_entity_mailing import AssociatedEntityMailing
    from ..models.associated_entity_phones import AssociatedEntityPhones
    from ..models.associated_entity_residence import AssociatedEntityResidence
    from ..models.associated_entity_tax_treaty_details_item import AssociatedEntityTaxTreatyDetailsItem
    from ..models.associated_person import AssociatedPerson


T = TypeVar("T", bound="AssociatedEntity")


@_attrs_define
class AssociatedEntity:
    """
    Attributes:
        entity_id (Union[Unset, int]):
        external_code (Union[Unset, str]):
        name (Union[Unset, str]):
        email (Union[Unset, str]):
        organization_country (Union[Unset, str]):
        phones (Union[Unset, AssociatedEntityPhones]):
        residence (Union[Unset, AssociatedEntityResidence]):
        mailing (Union[Unset, AssociatedEntityMailing]):
        associations (Union[Unset, List[str]]):
        identity_documents (Union[Unset, List['AssociatedEntityIdentityDocumentsItem']]):
        tax_treaty_details (Union[Unset, List['AssociatedEntityTaxTreatyDetailsItem']]):
        associated_persons (Union[Unset, List['AssociatedPerson']]):
    """

    entity_id: Union[Unset, int] = UNSET
    external_code: Union[Unset, str] = UNSET
    name: Union[Unset, str] = UNSET
    email: Union[Unset, str] = UNSET
    organization_country: Union[Unset, str] = UNSET
    phones: Union[Unset, "AssociatedEntityPhones"] = UNSET
    residence: Union[Unset, "AssociatedEntityResidence"] = UNSET
    mailing: Union[Unset, "AssociatedEntityMailing"] = UNSET
    associations: Union[Unset, List[str]] = UNSET
    identity_documents: Union[Unset, List["AssociatedEntityIdentityDocumentsItem"]] = UNSET
    tax_treaty_details: Union[Unset, List["AssociatedEntityTaxTreatyDetailsItem"]] = UNSET
    associated_persons: Union[Unset, List["AssociatedPerson"]] = UNSET
    additional_properties: Dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> Dict[str, Any]:
        entity_id = self.entity_id

        external_code = self.external_code

        name = self.name

        email = self.email

        organization_country = self.organization_country

        phones: Union[Unset, Dict[str, Any]] = UNSET
        if not isinstance(self.phones, Unset):
            phones = self.phones.to_dict()

        residence: Union[Unset, Dict[str, Any]] = UNSET
        if not isinstance(self.residence, Unset):
            residence = self.residence.to_dict()

        mailing: Union[Unset, Dict[str, Any]] = UNSET
        if not isinstance(self.mailing, Unset):
            mailing = self.mailing.to_dict()

        associations: Union[Unset, List[str]] = UNSET
        if not isinstance(self.associations, Unset):
            associations = self.associations

        identity_documents: Union[Unset, List[Dict[str, Any]]] = UNSET
        if not isinstance(self.identity_documents, Unset):
            identity_documents = []
            for identity_documents_item_data in self.identity_documents:
                identity_documents_item = identity_documents_item_data.to_dict()
                identity_documents.append(identity_documents_item)

        tax_treaty_details: Union[Unset, List[Dict[str, Any]]] = UNSET
        if not isinstance(self.tax_treaty_details, Unset):
            tax_treaty_details = []
            for tax_treaty_details_item_data in self.tax_treaty_details:
                tax_treaty_details_item = tax_treaty_details_item_data.to_dict()
                tax_treaty_details.append(tax_treaty_details_item)

        associated_persons: Union[Unset, List[Dict[str, Any]]] = UNSET
        if not isinstance(self.associated_persons, Unset):
            associated_persons = []
            for associated_persons_item_data in self.associated_persons:
                associated_persons_item = associated_persons_item_data.to_dict()
                associated_persons.append(associated_persons_item)

        field_dict: Dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if entity_id is not UNSET:
            field_dict["entityId"] = entity_id
        if external_code is not UNSET:
            field_dict["externalCode"] = external_code
        if name is not UNSET:
            field_dict["name"] = name
        if email is not UNSET:
            field_dict["email"] = email
        if organization_country is not UNSET:
            field_dict["organizationCountry"] = organization_country
        if phones is not UNSET:
            field_dict["phones"] = phones
        if residence is not UNSET:
            field_dict["residence"] = residence
        if mailing is not UNSET:
            field_dict["mailing"] = mailing
        if associations is not UNSET:
            field_dict["associations"] = associations
        if identity_documents is not UNSET:
            field_dict["identityDocuments"] = identity_documents
        if tax_treaty_details is not UNSET:
            field_dict["taxTreatyDetails"] = tax_treaty_details
        if associated_persons is not UNSET:
            field_dict["AssociatedPersons"] = associated_persons

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        from ..models.associated_entity_identity_documents_item import AssociatedEntityIdentityDocumentsItem
        from ..models.associated_entity_mailing import AssociatedEntityMailing
        from ..models.associated_entity_phones import AssociatedEntityPhones
        from ..models.associated_entity_residence import AssociatedEntityResidence
        from ..models.associated_entity_tax_treaty_details_item import AssociatedEntityTaxTreatyDetailsItem
        from ..models.associated_person import AssociatedPerson

        d = src_dict.copy()
        entity_id = d.pop("entityId", UNSET)

        external_code = d.pop("externalCode", UNSET)

        name = d.pop("name", UNSET)

        email = d.pop("email", UNSET)

        organization_country = d.pop("organizationCountry", UNSET)

        _phones = d.pop("phones", UNSET)
        phones: Union[Unset, AssociatedEntityPhones]
        if isinstance(_phones, Unset):
            phones = UNSET
        else:
            phones = AssociatedEntityPhones.from_dict(_phones)

        _residence = d.pop("residence", UNSET)
        residence: Union[Unset, AssociatedEntityResidence]
        if isinstance(_residence, Unset):
            residence = UNSET
        else:
            residence = AssociatedEntityResidence.from_dict(_residence)

        _mailing = d.pop("mailing", UNSET)
        mailing: Union[Unset, AssociatedEntityMailing]
        if isinstance(_mailing, Unset):
            mailing = UNSET
        else:
            mailing = AssociatedEntityMailing.from_dict(_mailing)

        associations = cast(List[str], d.pop("associations", UNSET))

        identity_documents = []
        _identity_documents = d.pop("identityDocuments", UNSET)
        for identity_documents_item_data in _identity_documents or []:
            identity_documents_item = AssociatedEntityIdentityDocumentsItem.from_dict(identity_documents_item_data)

            identity_documents.append(identity_documents_item)

        tax_treaty_details = []
        _tax_treaty_details = d.pop("taxTreatyDetails", UNSET)
        for tax_treaty_details_item_data in _tax_treaty_details or []:
            tax_treaty_details_item = AssociatedEntityTaxTreatyDetailsItem.from_dict(tax_treaty_details_item_data)

            tax_treaty_details.append(tax_treaty_details_item)

        associated_persons = []
        _associated_persons = d.pop("AssociatedPersons", UNSET)
        for associated_persons_item_data in _associated_persons or []:
            associated_persons_item = AssociatedPerson.from_dict(associated_persons_item_data)

            associated_persons.append(associated_persons_item)

        associated_entity = cls(
            entity_id=entity_id,
            external_code=external_code,
            name=name,
            email=email,
            organization_country=organization_country,
            phones=phones,
            residence=residence,
            mailing=mailing,
            associations=associations,
            identity_documents=identity_documents,
            tax_treaty_details=tax_treaty_details,
            associated_persons=associated_persons,
        )

        associated_entity.additional_properties = d
        return associated_entity

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
