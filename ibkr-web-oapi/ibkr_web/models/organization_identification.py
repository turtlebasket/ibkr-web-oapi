from typing import TYPE_CHECKING, Any, Dict, List, Type, TypeVar, Union

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.address import Address
    from ..models.phone_info import PhoneInfo


T = TypeVar("T", bound="OrganizationIdentification")


@_attrs_define
class OrganizationIdentification:
    """
    Attributes:
        place_of_business_address (Union[Unset, Address]):
        mailing_address (Union[Unset, Address]):
        phones (Union[Unset, List['PhoneInfo']]):
        name (Union[Unset, str]):
        business_description (Union[Unset, str]):
        website_address (Union[Unset, str]):
        identification (Union[Unset, str]):
        identification_country (Union[Unset, str]):
        formation_country (Union[Unset, str]):
        formation_state (Union[Unset, str]):
        same_mail_address (Union[Unset, bool]):
        translated (Union[Unset, bool]):
    """

    place_of_business_address: Union[Unset, "Address"] = UNSET
    mailing_address: Union[Unset, "Address"] = UNSET
    phones: Union[Unset, List["PhoneInfo"]] = UNSET
    name: Union[Unset, str] = UNSET
    business_description: Union[Unset, str] = UNSET
    website_address: Union[Unset, str] = UNSET
    identification: Union[Unset, str] = UNSET
    identification_country: Union[Unset, str] = UNSET
    formation_country: Union[Unset, str] = UNSET
    formation_state: Union[Unset, str] = UNSET
    same_mail_address: Union[Unset, bool] = UNSET
    translated: Union[Unset, bool] = UNSET
    additional_properties: Dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> Dict[str, Any]:
        place_of_business_address: Union[Unset, Dict[str, Any]] = UNSET
        if not isinstance(self.place_of_business_address, Unset):
            place_of_business_address = self.place_of_business_address.to_dict()

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

        business_description = self.business_description

        website_address = self.website_address

        identification = self.identification

        identification_country = self.identification_country

        formation_country = self.formation_country

        formation_state = self.formation_state

        same_mail_address = self.same_mail_address

        translated = self.translated

        field_dict: Dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if place_of_business_address is not UNSET:
            field_dict["placeOfBusinessAddress"] = place_of_business_address
        if mailing_address is not UNSET:
            field_dict["mailingAddress"] = mailing_address
        if phones is not UNSET:
            field_dict["phones"] = phones
        if name is not UNSET:
            field_dict["name"] = name
        if business_description is not UNSET:
            field_dict["businessDescription"] = business_description
        if website_address is not UNSET:
            field_dict["websiteAddress"] = website_address
        if identification is not UNSET:
            field_dict["identification"] = identification
        if identification_country is not UNSET:
            field_dict["identificationCountry"] = identification_country
        if formation_country is not UNSET:
            field_dict["formationCountry"] = formation_country
        if formation_state is not UNSET:
            field_dict["formationState"] = formation_state
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
        _place_of_business_address = d.pop("placeOfBusinessAddress", UNSET)
        place_of_business_address: Union[Unset, Address]
        if isinstance(_place_of_business_address, Unset):
            place_of_business_address = UNSET
        else:
            place_of_business_address = Address.from_dict(_place_of_business_address)

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

        business_description = d.pop("businessDescription", UNSET)

        website_address = d.pop("websiteAddress", UNSET)

        identification = d.pop("identification", UNSET)

        identification_country = d.pop("identificationCountry", UNSET)

        formation_country = d.pop("formationCountry", UNSET)

        formation_state = d.pop("formationState", UNSET)

        same_mail_address = d.pop("sameMailAddress", UNSET)

        translated = d.pop("translated", UNSET)

        organization_identification = cls(
            place_of_business_address=place_of_business_address,
            mailing_address=mailing_address,
            phones=phones,
            name=name,
            business_description=business_description,
            website_address=website_address,
            identification=identification,
            identification_country=identification_country,
            formation_country=formation_country,
            formation_state=formation_state,
            same_mail_address=same_mail_address,
            translated=translated,
        )

        organization_identification.additional_properties = d
        return organization_identification

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
