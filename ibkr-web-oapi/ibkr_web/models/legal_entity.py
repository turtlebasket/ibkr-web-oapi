from typing import TYPE_CHECKING, Any, Dict, List, Type, TypeVar, Union

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.address import Address
    from ..models.legal_entity_identification import LegalEntityIdentification
    from ..models.phone_info import PhoneInfo
    from ..models.tax_residency import TaxResidency


T = TypeVar("T", bound="LegalEntity")


@_attrs_define
class LegalEntity:
    """
    Attributes:
        name (Union[Unset, str]):
        address (Union[Unset, Address]):
        phones (Union[Unset, List['PhoneInfo']]):
        email (Union[Unset, str]):
        legal_entity_identification (Union[Unset, LegalEntityIdentification]):
        tax_residencies (Union[Unset, List['TaxResidency']]):
        id (Union[Unset, str]):
        external_id (Union[Unset, str]):
        us_tax_resident (Union[Unset, bool]):
        translated (Union[Unset, bool]):
    """

    name: Union[Unset, str] = UNSET
    address: Union[Unset, "Address"] = UNSET
    phones: Union[Unset, List["PhoneInfo"]] = UNSET
    email: Union[Unset, str] = UNSET
    legal_entity_identification: Union[Unset, "LegalEntityIdentification"] = UNSET
    tax_residencies: Union[Unset, List["TaxResidency"]] = UNSET
    id: Union[Unset, str] = UNSET
    external_id: Union[Unset, str] = UNSET
    us_tax_resident: Union[Unset, bool] = UNSET
    translated: Union[Unset, bool] = UNSET
    additional_properties: Dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> Dict[str, Any]:
        name = self.name

        address: Union[Unset, Dict[str, Any]] = UNSET
        if not isinstance(self.address, Unset):
            address = self.address.to_dict()

        phones: Union[Unset, List[Dict[str, Any]]] = UNSET
        if not isinstance(self.phones, Unset):
            phones = []
            for phones_item_data in self.phones:
                phones_item = phones_item_data.to_dict()
                phones.append(phones_item)

        email = self.email

        legal_entity_identification: Union[Unset, Dict[str, Any]] = UNSET
        if not isinstance(self.legal_entity_identification, Unset):
            legal_entity_identification = self.legal_entity_identification.to_dict()

        tax_residencies: Union[Unset, List[Dict[str, Any]]] = UNSET
        if not isinstance(self.tax_residencies, Unset):
            tax_residencies = []
            for tax_residencies_item_data in self.tax_residencies:
                tax_residencies_item = tax_residencies_item_data.to_dict()
                tax_residencies.append(tax_residencies_item)

        id = self.id

        external_id = self.external_id

        us_tax_resident = self.us_tax_resident

        translated = self.translated

        field_dict: Dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if name is not UNSET:
            field_dict["name"] = name
        if address is not UNSET:
            field_dict["address"] = address
        if phones is not UNSET:
            field_dict["phones"] = phones
        if email is not UNSET:
            field_dict["email"] = email
        if legal_entity_identification is not UNSET:
            field_dict["legalEntityIdentification"] = legal_entity_identification
        if tax_residencies is not UNSET:
            field_dict["taxResidencies"] = tax_residencies
        if id is not UNSET:
            field_dict["id"] = id
        if external_id is not UNSET:
            field_dict["externalId"] = external_id
        if us_tax_resident is not UNSET:
            field_dict["usTaxResident"] = us_tax_resident
        if translated is not UNSET:
            field_dict["translated"] = translated

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        from ..models.address import Address
        from ..models.legal_entity_identification import LegalEntityIdentification
        from ..models.phone_info import PhoneInfo
        from ..models.tax_residency import TaxResidency

        d = src_dict.copy()
        name = d.pop("name", UNSET)

        _address = d.pop("address", UNSET)
        address: Union[Unset, Address]
        if isinstance(_address, Unset):
            address = UNSET
        else:
            address = Address.from_dict(_address)

        phones = []
        _phones = d.pop("phones", UNSET)
        for phones_item_data in _phones or []:
            phones_item = PhoneInfo.from_dict(phones_item_data)

            phones.append(phones_item)

        email = d.pop("email", UNSET)

        _legal_entity_identification = d.pop("legalEntityIdentification", UNSET)
        legal_entity_identification: Union[Unset, LegalEntityIdentification]
        if isinstance(_legal_entity_identification, Unset):
            legal_entity_identification = UNSET
        else:
            legal_entity_identification = LegalEntityIdentification.from_dict(_legal_entity_identification)

        tax_residencies = []
        _tax_residencies = d.pop("taxResidencies", UNSET)
        for tax_residencies_item_data in _tax_residencies or []:
            tax_residencies_item = TaxResidency.from_dict(tax_residencies_item_data)

            tax_residencies.append(tax_residencies_item)

        id = d.pop("id", UNSET)

        external_id = d.pop("externalId", UNSET)

        us_tax_resident = d.pop("usTaxResident", UNSET)

        translated = d.pop("translated", UNSET)

        legal_entity = cls(
            name=name,
            address=address,
            phones=phones,
            email=email,
            legal_entity_identification=legal_entity_identification,
            tax_residencies=tax_residencies,
            id=id,
            external_id=external_id,
            us_tax_resident=us_tax_resident,
            translated=translated,
        )

        legal_entity.additional_properties = d
        return legal_entity

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
