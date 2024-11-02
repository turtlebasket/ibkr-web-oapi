from typing import TYPE_CHECKING, Any, Dict, List, Type, TypeVar, Union

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..models.legal_entity_identification_formation_type import LegalEntityIdentificationFormationType
from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.address import Address


T = TypeVar("T", bound="LegalEntityIdentification")


@_attrs_define
class LegalEntityIdentification:
    """
    Attributes:
        place_of_business_address (Union[Unset, Address]):
        mailing_address (Union[Unset, Address]):
        identification (Union[Unset, str]):
        identification_country (Union[Unset, str]):
        formation_country (Union[Unset, str]):
        formation_type (Union[Unset, LegalEntityIdentificationFormationType]):
        exchange_code (Union[Unset, str]):
        exchange_symbol (Union[Unset, str]):
        same_mail_address (Union[Unset, bool]):
    """

    place_of_business_address: Union[Unset, "Address"] = UNSET
    mailing_address: Union[Unset, "Address"] = UNSET
    identification: Union[Unset, str] = UNSET
    identification_country: Union[Unset, str] = UNSET
    formation_country: Union[Unset, str] = UNSET
    formation_type: Union[Unset, LegalEntityIdentificationFormationType] = UNSET
    exchange_code: Union[Unset, str] = UNSET
    exchange_symbol: Union[Unset, str] = UNSET
    same_mail_address: Union[Unset, bool] = UNSET
    additional_properties: Dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> Dict[str, Any]:
        place_of_business_address: Union[Unset, Dict[str, Any]] = UNSET
        if not isinstance(self.place_of_business_address, Unset):
            place_of_business_address = self.place_of_business_address.to_dict()

        mailing_address: Union[Unset, Dict[str, Any]] = UNSET
        if not isinstance(self.mailing_address, Unset):
            mailing_address = self.mailing_address.to_dict()

        identification = self.identification

        identification_country = self.identification_country

        formation_country = self.formation_country

        formation_type: Union[Unset, str] = UNSET
        if not isinstance(self.formation_type, Unset):
            formation_type = self.formation_type.value

        exchange_code = self.exchange_code

        exchange_symbol = self.exchange_symbol

        same_mail_address = self.same_mail_address

        field_dict: Dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if place_of_business_address is not UNSET:
            field_dict["placeOfBusinessAddress"] = place_of_business_address
        if mailing_address is not UNSET:
            field_dict["mailingAddress"] = mailing_address
        if identification is not UNSET:
            field_dict["identification"] = identification
        if identification_country is not UNSET:
            field_dict["identificationCountry"] = identification_country
        if formation_country is not UNSET:
            field_dict["formationCountry"] = formation_country
        if formation_type is not UNSET:
            field_dict["formationType"] = formation_type
        if exchange_code is not UNSET:
            field_dict["exchangeCode"] = exchange_code
        if exchange_symbol is not UNSET:
            field_dict["exchangeSymbol"] = exchange_symbol
        if same_mail_address is not UNSET:
            field_dict["sameMailAddress"] = same_mail_address

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        from ..models.address import Address

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

        identification = d.pop("identification", UNSET)

        identification_country = d.pop("identificationCountry", UNSET)

        formation_country = d.pop("formationCountry", UNSET)

        _formation_type = d.pop("formationType", UNSET)
        formation_type: Union[Unset, LegalEntityIdentificationFormationType]
        if isinstance(_formation_type, Unset):
            formation_type = UNSET
        else:
            formation_type = LegalEntityIdentificationFormationType(_formation_type)

        exchange_code = d.pop("exchangeCode", UNSET)

        exchange_symbol = d.pop("exchangeSymbol", UNSET)

        same_mail_address = d.pop("sameMailAddress", UNSET)

        legal_entity_identification = cls(
            place_of_business_address=place_of_business_address,
            mailing_address=mailing_address,
            identification=identification,
            identification_country=identification_country,
            formation_country=formation_country,
            formation_type=formation_type,
            exchange_code=exchange_code,
            exchange_symbol=exchange_symbol,
            same_mail_address=same_mail_address,
        )

        legal_entity_identification.additional_properties = d
        return legal_entity_identification

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
