from typing import Any, Dict, List, Type, TypeVar, Union

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

T = TypeVar("T", bound="ResidenceAddress")


@_attrs_define
class ResidenceAddress:
    r"""Provide the residential address where the applicant physically resides. <br><ul><li>If the mailing address is
    different from the address provided in Residence element, THEN you will also include MailingAddress
    element.</li><li>Post Office Box is not accepted for Residential Address.</li><li>Our system validates street_1 and
    street_2 included within Residence attribute to ensure Post Office Box address is not provided.</li><li>An error
    will be thrown if the below combinations are included within street_1 OR street_2:</li><ul><li>PB</li><li>PO
    Box</li><li>Post Office Box</li><li>P.O. Box</li><li>In care of</li><li>General Delivery</li><li>Regular Expression
    to validate street_1 and street_2:</li></ul></ul>English: (?:P(?:ost(?:al)?)?[\.\-
    \s]*(?:(?:O(?:ffice)?[\.\s]*)?B(?:ox|in|\b|\d)|o(?:ffice|\b)(?:[-\s]*\d)|code)|box[-\s]*\d)<br>Chinese Simplified:
    PO Box    (?i)\b((邮政信箱) [0-9]*)\bChinese Traditional: PO Box   (?i)\b((郵政信箱) [0-9]*)\b

        Example:
            {"street1": "1 Tester Street", "city": "London", "state": "GB-ENG" ,"country":"GBR","postalCode": "SW10 9QL"},

        Attributes:
            street1 (Union[Unset, str]): Street which applicant resides
            street2 (Union[Unset, str]): Street which applicant resides
            city (Union[Unset, str]): City which the applicant resides.
            state (Union[Unset, str]): State/Province which the applicant resides.
            country (Union[Unset, str]): Country which the applicant resides.
            postal_code (Union[Unset, str]): Postal / Zip code.For countries that do not provide postal code, please enter
                00000
    """

    street1: Union[Unset, str] = UNSET
    street2: Union[Unset, str] = UNSET
    city: Union[Unset, str] = UNSET
    state: Union[Unset, str] = UNSET
    country: Union[Unset, str] = UNSET
    postal_code: Union[Unset, str] = UNSET
    additional_properties: Dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> Dict[str, Any]:
        street1 = self.street1

        street2 = self.street2

        city = self.city

        state = self.state

        country = self.country

        postal_code = self.postal_code

        field_dict: Dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if street1 is not UNSET:
            field_dict["street1"] = street1
        if street2 is not UNSET:
            field_dict["street2"] = street2
        if city is not UNSET:
            field_dict["city"] = city
        if state is not UNSET:
            field_dict["state"] = state
        if country is not UNSET:
            field_dict["country"] = country
        if postal_code is not UNSET:
            field_dict["postalCode"] = postal_code

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        d = src_dict.copy()
        street1 = d.pop("street1", UNSET)

        street2 = d.pop("street2", UNSET)

        city = d.pop("city", UNSET)

        state = d.pop("state", UNSET)

        country = d.pop("country", UNSET)

        postal_code = d.pop("postalCode", UNSET)

        residence_address = cls(
            street1=street1,
            street2=street2,
            city=city,
            state=state,
            country=country,
            postal_code=postal_code,
        )

        residence_address.additional_properties = d
        return residence_address

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
