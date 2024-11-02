from typing import TYPE_CHECKING, Any, Dict, List, Type, TypeVar, Union, cast

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.associated_person_employment_details import AssociatedPersonEmploymentDetails
    from ..models.associated_person_identity_documents_item import AssociatedPersonIdentityDocumentsItem
    from ..models.associated_person_mailing import AssociatedPersonMailing
    from ..models.associated_person_phones import AssociatedPersonPhones
    from ..models.associated_person_residence import AssociatedPersonResidence
    from ..models.associated_person_subscribed_services_item import AssociatedPersonSubscribedServicesItem
    from ..models.associated_person_tax_treaty_details_item import AssociatedPersonTaxTreatyDetailsItem


T = TypeVar("T", bound="AssociatedPerson")


@_attrs_define
class AssociatedPerson:
    """
    Attributes:
        entity_id (Union[Unset, int]):
        external_code (Union[Unset, str]):
        first_name (Union[Unset, str]):
        middle_name (Union[Unset, str]):
        middle_initial (Union[Unset, str]):
        last_name (Union[Unset, str]):
        suffix (Union[Unset, str]):
        username (Union[Unset, str]):
        password_date (Union[Unset, str]):
        user_status (Union[Unset, str]):
        last_login (Union[Unset, str]):
        gender (Union[Unset, str]):
        marital_status (Union[Unset, str]):
        salutation (Union[Unset, str]):
        email (Union[Unset, str]):
        country_of_citizenship (Union[Unset, str]):
        country_of_birth (Union[Unset, str]):
        date_of_birth (Union[Unset, str]):
        moters_maiden_name (Union[Unset, str]):
        number_of_dependents (Union[Unset, int]):
        security_device (Union[Unset, str]):
        commercial (Union[Unset, str]):
        phones (Union[Unset, AssociatedPersonPhones]):
        residence (Union[Unset, AssociatedPersonResidence]):
        mailing (Union[Unset, AssociatedPersonMailing]):
        associations (Union[Unset, List[str]]):
        identity_documents (Union[Unset, List['AssociatedPersonIdentityDocumentsItem']]):
        employment_type (Union[Unset, str]):
        employment_details (Union[Unset, AssociatedPersonEmploymentDetails]):
        subscribed_services (Union[Unset, List['AssociatedPersonSubscribedServicesItem']]):
        tax_treaty_details (Union[Unset, List['AssociatedPersonTaxTreatyDetailsItem']]):
    """

    entity_id: Union[Unset, int] = UNSET
    external_code: Union[Unset, str] = UNSET
    first_name: Union[Unset, str] = UNSET
    middle_name: Union[Unset, str] = UNSET
    middle_initial: Union[Unset, str] = UNSET
    last_name: Union[Unset, str] = UNSET
    suffix: Union[Unset, str] = UNSET
    username: Union[Unset, str] = UNSET
    password_date: Union[Unset, str] = UNSET
    user_status: Union[Unset, str] = UNSET
    last_login: Union[Unset, str] = UNSET
    gender: Union[Unset, str] = UNSET
    marital_status: Union[Unset, str] = UNSET
    salutation: Union[Unset, str] = UNSET
    email: Union[Unset, str] = UNSET
    country_of_citizenship: Union[Unset, str] = UNSET
    country_of_birth: Union[Unset, str] = UNSET
    date_of_birth: Union[Unset, str] = UNSET
    moters_maiden_name: Union[Unset, str] = UNSET
    number_of_dependents: Union[Unset, int] = UNSET
    security_device: Union[Unset, str] = UNSET
    commercial: Union[Unset, str] = UNSET
    phones: Union[Unset, "AssociatedPersonPhones"] = UNSET
    residence: Union[Unset, "AssociatedPersonResidence"] = UNSET
    mailing: Union[Unset, "AssociatedPersonMailing"] = UNSET
    associations: Union[Unset, List[str]] = UNSET
    identity_documents: Union[Unset, List["AssociatedPersonIdentityDocumentsItem"]] = UNSET
    employment_type: Union[Unset, str] = UNSET
    employment_details: Union[Unset, "AssociatedPersonEmploymentDetails"] = UNSET
    subscribed_services: Union[Unset, List["AssociatedPersonSubscribedServicesItem"]] = UNSET
    tax_treaty_details: Union[Unset, List["AssociatedPersonTaxTreatyDetailsItem"]] = UNSET
    additional_properties: Dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> Dict[str, Any]:
        entity_id = self.entity_id

        external_code = self.external_code

        first_name = self.first_name

        middle_name = self.middle_name

        middle_initial = self.middle_initial

        last_name = self.last_name

        suffix = self.suffix

        username = self.username

        password_date = self.password_date

        user_status = self.user_status

        last_login = self.last_login

        gender = self.gender

        marital_status = self.marital_status

        salutation = self.salutation

        email = self.email

        country_of_citizenship = self.country_of_citizenship

        country_of_birth = self.country_of_birth

        date_of_birth = self.date_of_birth

        moters_maiden_name = self.moters_maiden_name

        number_of_dependents = self.number_of_dependents

        security_device = self.security_device

        commercial = self.commercial

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

        employment_type = self.employment_type

        employment_details: Union[Unset, Dict[str, Any]] = UNSET
        if not isinstance(self.employment_details, Unset):
            employment_details = self.employment_details.to_dict()

        subscribed_services: Union[Unset, List[Dict[str, Any]]] = UNSET
        if not isinstance(self.subscribed_services, Unset):
            subscribed_services = []
            for subscribed_services_item_data in self.subscribed_services:
                subscribed_services_item = subscribed_services_item_data.to_dict()
                subscribed_services.append(subscribed_services_item)

        tax_treaty_details: Union[Unset, List[Dict[str, Any]]] = UNSET
        if not isinstance(self.tax_treaty_details, Unset):
            tax_treaty_details = []
            for tax_treaty_details_item_data in self.tax_treaty_details:
                tax_treaty_details_item = tax_treaty_details_item_data.to_dict()
                tax_treaty_details.append(tax_treaty_details_item)

        field_dict: Dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if entity_id is not UNSET:
            field_dict["entityId"] = entity_id
        if external_code is not UNSET:
            field_dict["externalCode"] = external_code
        if first_name is not UNSET:
            field_dict["firstName"] = first_name
        if middle_name is not UNSET:
            field_dict["middleName"] = middle_name
        if middle_initial is not UNSET:
            field_dict["middleInitial"] = middle_initial
        if last_name is not UNSET:
            field_dict["lastName"] = last_name
        if suffix is not UNSET:
            field_dict["suffix"] = suffix
        if username is not UNSET:
            field_dict["username"] = username
        if password_date is not UNSET:
            field_dict["passwordDate"] = password_date
        if user_status is not UNSET:
            field_dict["userStatus"] = user_status
        if last_login is not UNSET:
            field_dict["lastLogin"] = last_login
        if gender is not UNSET:
            field_dict["gender"] = gender
        if marital_status is not UNSET:
            field_dict["maritalStatus"] = marital_status
        if salutation is not UNSET:
            field_dict["salutation"] = salutation
        if email is not UNSET:
            field_dict["email"] = email
        if country_of_citizenship is not UNSET:
            field_dict["countryOfCitizenship"] = country_of_citizenship
        if country_of_birth is not UNSET:
            field_dict["countryOfBirth"] = country_of_birth
        if date_of_birth is not UNSET:
            field_dict["dateOfBirth"] = date_of_birth
        if moters_maiden_name is not UNSET:
            field_dict["motersMaidenName"] = moters_maiden_name
        if number_of_dependents is not UNSET:
            field_dict["numberOfDependents"] = number_of_dependents
        if security_device is not UNSET:
            field_dict["securityDevice"] = security_device
        if commercial is not UNSET:
            field_dict["commercial"] = commercial
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
        if employment_type is not UNSET:
            field_dict["employmentType"] = employment_type
        if employment_details is not UNSET:
            field_dict["employmentDetails"] = employment_details
        if subscribed_services is not UNSET:
            field_dict["subscribedServices"] = subscribed_services
        if tax_treaty_details is not UNSET:
            field_dict["taxTreatyDetails"] = tax_treaty_details

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        from ..models.associated_person_employment_details import AssociatedPersonEmploymentDetails
        from ..models.associated_person_identity_documents_item import AssociatedPersonIdentityDocumentsItem
        from ..models.associated_person_mailing import AssociatedPersonMailing
        from ..models.associated_person_phones import AssociatedPersonPhones
        from ..models.associated_person_residence import AssociatedPersonResidence
        from ..models.associated_person_subscribed_services_item import AssociatedPersonSubscribedServicesItem
        from ..models.associated_person_tax_treaty_details_item import AssociatedPersonTaxTreatyDetailsItem

        d = src_dict.copy()
        entity_id = d.pop("entityId", UNSET)

        external_code = d.pop("externalCode", UNSET)

        first_name = d.pop("firstName", UNSET)

        middle_name = d.pop("middleName", UNSET)

        middle_initial = d.pop("middleInitial", UNSET)

        last_name = d.pop("lastName", UNSET)

        suffix = d.pop("suffix", UNSET)

        username = d.pop("username", UNSET)

        password_date = d.pop("passwordDate", UNSET)

        user_status = d.pop("userStatus", UNSET)

        last_login = d.pop("lastLogin", UNSET)

        gender = d.pop("gender", UNSET)

        marital_status = d.pop("maritalStatus", UNSET)

        salutation = d.pop("salutation", UNSET)

        email = d.pop("email", UNSET)

        country_of_citizenship = d.pop("countryOfCitizenship", UNSET)

        country_of_birth = d.pop("countryOfBirth", UNSET)

        date_of_birth = d.pop("dateOfBirth", UNSET)

        moters_maiden_name = d.pop("motersMaidenName", UNSET)

        number_of_dependents = d.pop("numberOfDependents", UNSET)

        security_device = d.pop("securityDevice", UNSET)

        commercial = d.pop("commercial", UNSET)

        _phones = d.pop("phones", UNSET)
        phones: Union[Unset, AssociatedPersonPhones]
        if isinstance(_phones, Unset):
            phones = UNSET
        else:
            phones = AssociatedPersonPhones.from_dict(_phones)

        _residence = d.pop("residence", UNSET)
        residence: Union[Unset, AssociatedPersonResidence]
        if isinstance(_residence, Unset):
            residence = UNSET
        else:
            residence = AssociatedPersonResidence.from_dict(_residence)

        _mailing = d.pop("mailing", UNSET)
        mailing: Union[Unset, AssociatedPersonMailing]
        if isinstance(_mailing, Unset):
            mailing = UNSET
        else:
            mailing = AssociatedPersonMailing.from_dict(_mailing)

        associations = cast(List[str], d.pop("associations", UNSET))

        identity_documents = []
        _identity_documents = d.pop("identityDocuments", UNSET)
        for identity_documents_item_data in _identity_documents or []:
            identity_documents_item = AssociatedPersonIdentityDocumentsItem.from_dict(identity_documents_item_data)

            identity_documents.append(identity_documents_item)

        employment_type = d.pop("employmentType", UNSET)

        _employment_details = d.pop("employmentDetails", UNSET)
        employment_details: Union[Unset, AssociatedPersonEmploymentDetails]
        if isinstance(_employment_details, Unset):
            employment_details = UNSET
        else:
            employment_details = AssociatedPersonEmploymentDetails.from_dict(_employment_details)

        subscribed_services = []
        _subscribed_services = d.pop("subscribedServices", UNSET)
        for subscribed_services_item_data in _subscribed_services or []:
            subscribed_services_item = AssociatedPersonSubscribedServicesItem.from_dict(subscribed_services_item_data)

            subscribed_services.append(subscribed_services_item)

        tax_treaty_details = []
        _tax_treaty_details = d.pop("taxTreatyDetails", UNSET)
        for tax_treaty_details_item_data in _tax_treaty_details or []:
            tax_treaty_details_item = AssociatedPersonTaxTreatyDetailsItem.from_dict(tax_treaty_details_item_data)

            tax_treaty_details.append(tax_treaty_details_item)

        associated_person = cls(
            entity_id=entity_id,
            external_code=external_code,
            first_name=first_name,
            middle_name=middle_name,
            middle_initial=middle_initial,
            last_name=last_name,
            suffix=suffix,
            username=username,
            password_date=password_date,
            user_status=user_status,
            last_login=last_login,
            gender=gender,
            marital_status=marital_status,
            salutation=salutation,
            email=email,
            country_of_citizenship=country_of_citizenship,
            country_of_birth=country_of_birth,
            date_of_birth=date_of_birth,
            moters_maiden_name=moters_maiden_name,
            number_of_dependents=number_of_dependents,
            security_device=security_device,
            commercial=commercial,
            phones=phones,
            residence=residence,
            mailing=mailing,
            associations=associations,
            identity_documents=identity_documents,
            employment_type=employment_type,
            employment_details=employment_details,
            subscribed_services=subscribed_services,
            tax_treaty_details=tax_treaty_details,
        )

        associated_person.additional_properties = d
        return associated_person

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
