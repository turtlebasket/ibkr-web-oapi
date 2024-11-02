import datetime
from typing import TYPE_CHECKING, Any, Dict, List, Type, TypeVar, Union

from attrs import define as _attrs_define
from attrs import field as _attrs_field
from dateutil.parser import isoparse

from ..models.trust_identification_registration_type import TrustIdentificationRegistrationType
from ..models.trust_identification_type_of_trust import TrustIdentificationTypeOfTrust
from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.address import Address
    from ..models.phone_info import PhoneInfo


T = TypeVar("T", bound="TrustIdentification")


@_attrs_define
class TrustIdentification:
    """
    Attributes:
        address (Union[Unset, Address]):
        mailing_address (Union[Unset, Address]):
        phones (Union[Unset, List['PhoneInfo']]):
        name (Union[Unset, str]):
        description (Union[Unset, str]):
        type_of_trust (Union[Unset, TrustIdentificationTypeOfTrust]):
        purpose_of_trust (Union[Unset, str]):
        date_formed (Union[Unset, datetime.date]):
        formation_country (Union[Unset, str]):
        formation_state (Union[Unset, str]):
        registration_number (Union[Unset, str]):
        registration_type (Union[Unset, TrustIdentificationRegistrationType]):
        registration_country (Union[Unset, str]):
        same_mail_address (Union[Unset, bool]):
        translated (Union[Unset, bool]):
    """

    address: Union[Unset, "Address"] = UNSET
    mailing_address: Union[Unset, "Address"] = UNSET
    phones: Union[Unset, List["PhoneInfo"]] = UNSET
    name: Union[Unset, str] = UNSET
    description: Union[Unset, str] = UNSET
    type_of_trust: Union[Unset, TrustIdentificationTypeOfTrust] = UNSET
    purpose_of_trust: Union[Unset, str] = UNSET
    date_formed: Union[Unset, datetime.date] = UNSET
    formation_country: Union[Unset, str] = UNSET
    formation_state: Union[Unset, str] = UNSET
    registration_number: Union[Unset, str] = UNSET
    registration_type: Union[Unset, TrustIdentificationRegistrationType] = UNSET
    registration_country: Union[Unset, str] = UNSET
    same_mail_address: Union[Unset, bool] = UNSET
    translated: Union[Unset, bool] = UNSET
    additional_properties: Dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> Dict[str, Any]:
        address: Union[Unset, Dict[str, Any]] = UNSET
        if not isinstance(self.address, Unset):
            address = self.address.to_dict()

        mailing_address: Union[Unset, Dict[str, Any]] = UNSET
        if not isinstance(self.mailing_address, Unset):
            mailing_address = self.mailing_address.to_dict()

        phones: Union[Unset, List[Dict[str, Any]]] = UNSET
        if not isinstance(self.phones, Unset):
            phones = []
            for phones_item_data in self.phones:
                phones_item = phones_item_data.to_dict()
                phones.append(phones_item)

        name = self.name

        description = self.description

        type_of_trust: Union[Unset, str] = UNSET
        if not isinstance(self.type_of_trust, Unset):
            type_of_trust = self.type_of_trust.value

        purpose_of_trust = self.purpose_of_trust

        date_formed: Union[Unset, str] = UNSET
        if not isinstance(self.date_formed, Unset):
            date_formed = self.date_formed.isoformat()

        formation_country = self.formation_country

        formation_state = self.formation_state

        registration_number = self.registration_number

        registration_type: Union[Unset, str] = UNSET
        if not isinstance(self.registration_type, Unset):
            registration_type = self.registration_type.value

        registration_country = self.registration_country

        same_mail_address = self.same_mail_address

        translated = self.translated

        field_dict: Dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if address is not UNSET:
            field_dict["address"] = address
        if mailing_address is not UNSET:
            field_dict["mailingAddress"] = mailing_address
        if phones is not UNSET:
            field_dict["phones"] = phones
        if name is not UNSET:
            field_dict["name"] = name
        if description is not UNSET:
            field_dict["description"] = description
        if type_of_trust is not UNSET:
            field_dict["typeOfTrust"] = type_of_trust
        if purpose_of_trust is not UNSET:
            field_dict["purposeOfTrust"] = purpose_of_trust
        if date_formed is not UNSET:
            field_dict["dateFormed"] = date_formed
        if formation_country is not UNSET:
            field_dict["formationCountry"] = formation_country
        if formation_state is not UNSET:
            field_dict["formationState"] = formation_state
        if registration_number is not UNSET:
            field_dict["registrationNumber"] = registration_number
        if registration_type is not UNSET:
            field_dict["registrationType"] = registration_type
        if registration_country is not UNSET:
            field_dict["registrationCountry"] = registration_country
        if same_mail_address is not UNSET:
            field_dict["sameMailAddress"] = same_mail_address
        if translated is not UNSET:
            field_dict["translated"] = translated

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        from ..models.address import Address
        from ..models.phone_info import PhoneInfo

        d = src_dict.copy()
        _address = d.pop("address", UNSET)
        address: Union[Unset, Address]
        if isinstance(_address, Unset):
            address = UNSET
        else:
            address = Address.from_dict(_address)

        _mailing_address = d.pop("mailingAddress", UNSET)
        mailing_address: Union[Unset, Address]
        if isinstance(_mailing_address, Unset):
            mailing_address = UNSET
        else:
            mailing_address = Address.from_dict(_mailing_address)

        phones = []
        _phones = d.pop("phones", UNSET)
        for phones_item_data in _phones or []:
            phones_item = PhoneInfo.from_dict(phones_item_data)

            phones.append(phones_item)

        name = d.pop("name", UNSET)

        description = d.pop("description", UNSET)

        _type_of_trust = d.pop("typeOfTrust", UNSET)
        type_of_trust: Union[Unset, TrustIdentificationTypeOfTrust]
        if isinstance(_type_of_trust, Unset):
            type_of_trust = UNSET
        else:
            type_of_trust = TrustIdentificationTypeOfTrust(_type_of_trust)

        purpose_of_trust = d.pop("purposeOfTrust", UNSET)

        _date_formed = d.pop("dateFormed", UNSET)
        date_formed: Union[Unset, datetime.date]
        if isinstance(_date_formed, Unset):
            date_formed = UNSET
        else:
            date_formed = isoparse(_date_formed).date()

        formation_country = d.pop("formationCountry", UNSET)

        formation_state = d.pop("formationState", UNSET)

        registration_number = d.pop("registrationNumber", UNSET)

        _registration_type = d.pop("registrationType", UNSET)
        registration_type: Union[Unset, TrustIdentificationRegistrationType]
        if isinstance(_registration_type, Unset):
            registration_type = UNSET
        else:
            registration_type = TrustIdentificationRegistrationType(_registration_type)

        registration_country = d.pop("registrationCountry", UNSET)

        same_mail_address = d.pop("sameMailAddress", UNSET)

        translated = d.pop("translated", UNSET)

        trust_identification = cls(
            address=address,
            mailing_address=mailing_address,
            phones=phones,
            name=name,
            description=description,
            type_of_trust=type_of_trust,
            purpose_of_trust=purpose_of_trust,
            date_formed=date_formed,
            formation_country=formation_country,
            formation_state=formation_state,
            registration_number=registration_number,
            registration_type=registration_type,
            registration_country=registration_country,
            same_mail_address=same_mail_address,
            translated=translated,
        )

        trust_identification.additional_properties = d
        return trust_identification

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
